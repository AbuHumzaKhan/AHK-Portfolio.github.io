"""Build a local SQLite database from the synthetic CSV sources."""
from pathlib import Path
import sqlite3
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
TABLES = ["accounts", "invoices", "usage_daily", "support_tickets"]
def build(data_dir: Path = ROOT / "data", db_path: Path = ROOT / "data" / "agent_demo.sqlite") -> Path:
    if db_path.exists(): db_path.unlink()
    with sqlite3.connect(db_path) as con:
        con.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
        for table in TABLES:
            df = pd.read_csv(data_dir / f"{table}.csv")
            df.to_sql(table, con, if_exists="append", index=False)
        con.execute("PRAGMA foreign_key_check")
    return db_path
if __name__ == "__main__":
    print(build())
