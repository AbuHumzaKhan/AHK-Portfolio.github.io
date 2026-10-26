# Deployment Guide

## Reproduce locally
1. Install Python 3.11+ and create a virtual environment.
2. Install requirements.txt from the full project bundle.
3. Run data generation, SQLite build, sample-seed generation, metric analysis, and pytest.
4. Open reports/ai_product_dashboard.html in a browser; it is self-contained and requires no CDN.
5. In Power BI Desktop, import both CSVs, apply the supplied M transformations, create a one-to-many relationship from AI Requests[request_id] to Interaction Events[request_id], add DAX measures, and reconcile values to outputs/metrics_summary.json.

## Publishing
The HTML report can be hosted as a static page. Verify the final URL and rendering after publication. The native .pbix file is not included; save and validate it manually in Power BI Desktop before claiming a PBIX deliverable.

No hosted website or Power BI Service deployment is claimed. All event records and token prices are synthetic.
