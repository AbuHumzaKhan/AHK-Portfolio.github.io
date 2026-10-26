"""Build the SQLite analytics database from generated CSV data."""
from pathlib import Path
import sqlite3
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def build(data_dir:Path=ROOT/"data",db_path:Path=ROOT/"data"/"ai_product_analytics.sqlite")->Path:
    if db_path.exists(): db_path.unlink()
    with sqlite3.connect(db_path) as con:
        con.executescript((ROOT/"sql"/"schema.sql").read_text(encoding="utf-8"))
        pd.read_csv(data_dir/"ai_requests.csv").to_sql("ai_requests",con,index=False,if_exists="append")
        pd.read_csv(data_dir/"interaction_events.csv").to_sql("interaction_events",con,index=False,if_exists="append")
        errors=con.execute("PRAGMA foreign_key_check").fetchall()
        if errors: raise RuntimeError(f"Foreign key errors: {errors[:3]}")
    return db_path
if __name__=="__main__": print(build())
