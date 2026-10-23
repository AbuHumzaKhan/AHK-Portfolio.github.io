from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
REPORTS = ROOT / "reports"
EXCEL = ROOT / "excel"
DB_PATH = ROOT / "inventory_analytics.sqlite"
SEED = 20261023
START_DATE = pd.Timestamp("2026-07-03")
DAYS = 90
