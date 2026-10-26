# Deployment Guide

## Local report

Open reports/dashboard.html in a modern browser. It is self-contained and does not require an API or paid service. reports/dashboard_preview.html is a compact static preview.

## GitHub Pages

1. Create a public repository named Marketing-Campaign-Performance-Analytics if a standalone repository is required. Repository creation is not exposed through the current connected GitHub operations, so use GitHub's web interface for that step.
2. Upload the project contents while preserving relative paths.
3. In Settings → Pages, select the main branch and the root folder (or the folder chosen for the static site).
4. Wait for the Pages workflow to complete.
5. Open the actual Pages URL and verify the dashboard, layout, charts, and mobile behavior before describing it as deployed.

The project showcase is also committed under projects/marketing-campaign-performance-analytics/ in the existing AHK-Portfolio.github.io repository. A commit alone does not prove that GitHub Pages has deployed the files.

## Power BI

The project contains DAX, Power Query M, model instructions, and an SVG preview. A native .pbix was not generated. Build and validate the model in Power BI Desktop, reconcile totals to outputs/metrics_summary.json, save the .pbix, and publish to Power BI Service only if account permissions allow.

## Release checklist

- Regenerate data with python python/generate_data.py.
- Recompute metrics with python python/analyze_campaigns.py.
- Run python -m unittest discover -s tests -v.
- Execute sql/qa_checks.sql and reconcile totals.
- Open the Excel workbook in Excel 2019+ and confirm formula recalculation.
- Verify the hosted URL and report rendering before claiming deployment.