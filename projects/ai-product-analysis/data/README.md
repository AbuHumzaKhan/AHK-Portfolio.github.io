# Data regeneration

The full CSVs are generated locally; they are not committed into this portfolio showcase folder. From the project root, run:

1. python -m src.generate_data
2. python -m src.build_database
3. python -m src.analyze_product

The full downloadable project bundle also contains the automated test suite. The generator creates 3,000 synthetic requests and associated interaction events using seed 20261026. No real product telemetry, prompt content, or user identifiers are used. Token prices are illustrative scenario assumptions.
