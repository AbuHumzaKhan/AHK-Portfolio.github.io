# Methodology

The pipeline creates one synthetic record per e-commerce order using a fixed random seed. Delivery time varies by shipping method, zone, carrier and operational disruption. SLA thresholds are assigned by service promise and route zone.

The analysis is intentionally descriptive:
- No predictive model.
- No causal inference.
- No real customer/company data.
- Carrier ranking is not a contractual recommendation by itself.
- Premium-service breach rates should be interpreted with their stricter SLA definitions.

For production use, the same framework should be connected to order-management, carrier scan events, promised-date logic, customer support and finance/refund systems.
