# Initial Findings — Inventory Replenishment & Stockout Analytics

**Build date:** 2026-10-23  
**Observation window:** 2026-07-03 to 2026-09-30  
**Provenance:** Deterministic synthetic data, seed 20261023.

## Executive summary
- Demand totaled 138,329 units; 136,221 units were fulfilled and 2,108 units were unmet.
- Unit fill rate was 98.48%; 2.19% of SKU–warehouse–days had at least one unit of unmet demand.
- Potential lost sales value was INR 3,261,211.31, calculated as unmet units × synthetic list price. This is not booked revenue or a forecast.
- Ending on-hand inventory value was INR 13,488,172.55.
- 747 simulated POs were created; 687 were received within the observation window. On-time rate among received POs was 62.30%.
- Estimated carrying cost was INR 655,607.44 using an illustrative 20% annual rate.

## Priorities to investigate
1. Sports has the highest category stockout-day rate (2.75%). Review SKU-level demand variability and safety-stock assumptions.
2. North Hub has the lowest fill rate (97.61%) and 1,205 unmet units. Check local demand and replenishment parameters.
3. SKU-033 (Skipping Rope) has the highest unmet volume (220 units) and 96.58% fill rate. Review this SKU–warehouse combination before increasing stock broadly.

## Recommendations
- Prioritize SKU–warehouse pairs using unmet units, fill rate, and stockout-day frequency together.
- Re-estimate demand and lead-time distributions from real operating history before changing reorder points.
- Track supplier delays separately from demand spikes.
- Run sensitivity tests on safety stock and order quantities before recommending inventory investment.

## Guardrails
This is a simulated scenario. It excludes returns, transfers, backorders, substitutions, promotions, shrinkage, taxes, and financing. The replenishment logic is a teaching heuristic, and category/warehouse differences are not causal evidence about real operations.