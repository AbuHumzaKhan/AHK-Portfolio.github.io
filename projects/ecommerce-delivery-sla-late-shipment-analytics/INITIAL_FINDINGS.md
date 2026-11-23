# Initial Findings - E-Commerce Delivery SLA & Late Shipment Analytics

Generated: 2026-11-23

## Executive results

| KPI | Result |
|---|---:|
| Orders | 24,000 |
| SLA breach rate | 12.60% |
| Late orders | 3,023 |
| Average delivery | 2.84 days |
| Late-order value | INR 38.52 lakh |
| Modeled refund exposure | INR 1.34 lakh |

## Carrier
BlueDartX is the best modeled carrier by SLA breach rate at approximately 8.82%; RapidGo is the weakest at approximately 16.91%.

## Service level
Standard delivery has the lowest modeled breach rate. Express and Same Day show substantially higher breach rates because the promise window is tighter.

## Management actions
1. Prioritize carrier-city combinations by volume and breach rate.
2. Create dedicated capacity/cutoff controls for premium services.
3. Monitor late-order value alongside late-order count.
4. Track first-attempt failures as a separate operational KPI.
5. Validate carrier conclusions with controlled allocation before contractual changes.

## Limitations
These are synthetic descriptive findings. No causal effect of carrier choice is claimed, and refund amounts are modeled rather than sourced from a finance system.
