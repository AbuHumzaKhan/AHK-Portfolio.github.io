from __future__ import annotations
import json
import pandas as pd
from .config import DATA, OUTPUTS, REPORTS, EXCEL
from .simulation import generate_data
from .analysis import summarize
from .sql_store import write_sqlite, write_seed_sql
from .excel_report import create_excel
from .dashboard import create_charts
from .findings import write_findings, write_data_dictionary, write_qa


def main() -> None:
    for folder in [DATA, OUTPUTS, REPORTS, EXCEL]:
        folder.mkdir(parents=True, exist_ok=True)
    data = generate_data()
    for name, df in data.items():
        df.to_csv(DATA / f"{name}.csv", index=False)
    data["inventory_daily"].head(30).to_csv(DATA / "sample" / "inventory_daily_sample.csv", index=False)
    summaries = summarize(data)
    write_sqlite(data)
    write_seed_sql(data)
    create_excel(data, summaries)
    create_charts(summaries)
    write_findings(summaries)
    write_data_dictionary()
    write_qa(data, summaries)
    qa = pd.read_csv(OUTPUTS / "qa_checks.csv")
    print(json.dumps({"kpis": summaries["kpis"], "qa_passed": int(qa["passed"].sum()), "qa_total": len(qa), "files_generated": True}, indent=2))


if __name__ == "__main__":
    main()
