# Deployment Guide

## Local run
1. Install Python 3.11+.
2. Create and activate a virtual environment.
3. Install requirements.txt from the complete project bundle.
4. Run the data generator, SQLite builder, benchmark, QA, report builder, and tests.
5. Start the local API with: uvicorn src.web_app:app --host 127.0.0.1 --port 8000.
6. Verify /health returns status=ok and llm=false; ask “What is MRR?” and reconcile the answer with the benchmark output.

## Static dashboard
The HTML dashboard is self-contained and can be hosted on GitHub Pages. Verify the final public URL and chart rendering after publication.

## Public API warning
The demo is not production-hardened. Before exposing it publicly, add authentication, authorization, tenant isolation, rate limits, audit logs, HTTPS, monitoring, and request-size controls. Keep the database read-only for question answering.

No hosted API or website deployment is claimed by this build.
