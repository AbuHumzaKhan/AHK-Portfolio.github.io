"""Standard-library checks for data, SQL, and artifact consistency."""
import csv,json,sqlite3,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read_csv(p):
    with p.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.daily=read_csv(ROOT/'data'/'campaign_daily_performance.csv')
        cls.campaigns=read_csv(ROOT/'data'/'campaigns.csv')
        cls.metrics=json.loads((ROOT/'outputs'/'metrics_summary.json').read_text(encoding='utf-8'))
        cls.db=sqlite3.connect(ROOT/'data'/'marketing_campaigns.sqlite')
    @classmethod
    def tearDownClass(cls): cls.db.close()
    def test_expected_rows_and_grain(self):
        self.assertEqual(len(self.daily),672)
        self.assertEqual(len({(r['date'],r['campaign_id']) for r in self.daily}),672)
    def test_date_range(self):
        dates=sorted(r['date'] for r in self.daily)
        self.assertEqual((dates[0],dates[-1]),('2026-07-06','2026-09-27'))
    def test_campaign_count_and_coverage(self):
        ids={r['campaign_id'] for r in self.campaigns}
        self.assertEqual(len(ids),8)
        self.assertTrue(all(r['campaign_id'] in ids for r in self.daily))
    def test_nonnegative_and_click_bounds(self):
        for r in self.daily:
            self.assertLessEqual(int(r['clicks']),int(r['impressions']))
            for k in ['impressions','clicks','spend_usd','conversions','revenue_usd','daily_budget_usd']:
                self.assertGreaterEqual(float(r[k]),0)
    def test_sqlite_reconciles_to_csv(self):
        db=self.db.execute('SELECT COUNT(*),SUM(impressions),SUM(clicks),ROUND(SUM(spend_usd),2),SUM(conversions),ROUND(SUM(revenue_usd),2) FROM campaign_daily_performance').fetchone()
        self.assertEqual(db[0],len(self.daily))
        self.assertEqual(db[1],sum(int(r['impressions']) for r in self.daily))
        self.assertEqual(db[2],sum(int(r['clicks']) for r in self.daily))
        self.assertAlmostEqual(db[3],sum(float(r['spend_usd']) for r in self.daily),places=2)
        self.assertEqual(db[4],sum(int(r['conversions']) for r in self.daily))
        self.assertAlmostEqual(db[5],sum(float(r['revenue_usd']) for r in self.daily),places=2)
    def test_database_integrity(self):
        self.assertEqual(self.db.execute('PRAGMA integrity_check').fetchone()[0],'ok')
        self.assertEqual(self.db.execute('PRAGMA foreign_key_check').fetchall(),[])
    def test_sql_qa_passes(self):
        sql=(ROOT/'sql'/'qa_checks.sql').read_text(encoding='utf-8')
        for statement in [s.strip() for s in sql.split(';') if 'SELECT' in s.upper()]:
            row=self.db.execute(statement).fetchone()
            self.assertEqual(row[1],0,row[0])
    def test_business_queries_execute(self):
        sql=(ROOT/'sql'/'business_queries.sql').read_text(encoding='utf-8')
        sql='\n'.join(line for line in sql.splitlines() if not line.strip().startswith('--'))
        statements=[s.strip() for s in sql.split(';') if s.strip()]
        self.assertEqual(len(statements),5)
        for statement in statements: self.db.execute(statement).fetchall()
    def test_metrics_match_source(self):
        m=self.metrics['overall']
        self.assertEqual(m['rows'],len(self.daily))
        self.assertEqual(m['impressions'],sum(int(r['impressions']) for r in self.daily))
        self.assertEqual(m['clicks'],sum(int(r['clicks']) for r in self.daily))
        self.assertEqual(m['conversions'],sum(int(r['conversions']) for r in self.daily))
        self.assertAlmostEqual(m['roas'],m['revenue_usd']/m['spend_usd'],places=8)
    def test_dashboard_and_workbook_exist(self):
        self.assertTrue((ROOT/'reports'/'dashboard.html').exists())
        self.assertTrue((ROOT/'excel'/'Marketing_Campaign_Performance_Analysis.xlsx').exists())
        self.assertTrue((ROOT/'reports'/'dashboard_preview.svg').exists())
if __name__=='__main__': unittest.main(verbosity=2)