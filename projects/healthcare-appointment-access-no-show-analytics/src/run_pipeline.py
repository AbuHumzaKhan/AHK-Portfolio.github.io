"""Run the full project build in reproducible order from the project root."""
from pathlib import Path
import subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
for script in ["src/generate_data.py", "src/analyze.py", "src/build_project.py"]:
    print(f"\n>>> python {script}", flush=True)
    subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, check=True)
print("\nBuild complete. Run: python -m unittest discover -s tests -v")
