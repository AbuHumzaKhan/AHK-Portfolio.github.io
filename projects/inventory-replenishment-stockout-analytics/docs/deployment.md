# Deployment and Run Instructions

The full runnable project package is provided in the downloadable project ZIP delivered with this conversation. After extracting it:

1. Create a Python virtual environment.
2. Install dependencies from requirements.txt.
3. Run the pipeline with python -m src.run_pipeline.
4. Run tests with python -m unittest discover -s tests -v.
5. Open reports/inventory_dashboard.html in a browser.

The pipeline regenerates synthetic CSVs, the SQLite database, Excel reports, dashboard assets, findings, and QA results.

For optional GitHub Pages hosting, place the dashboard HTML and its SVG assets in a published folder, enable Pages in repository Settings, wait for the deployment to finish, and verify the live page and image requests. Do not claim deployment until the URL has been tested.