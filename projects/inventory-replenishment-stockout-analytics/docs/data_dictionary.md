# Data Dictionary

## products
One row per synthetic SKU: sku, product_name, category, base_daily_demand, unit_cost_inr, unit_price_inr, supplier_lead_time_days, pack_size, safety_stock_units, reorder_point_units.

## warehouses
One row per synthetic warehouse: warehouse_id, warehouse_name, demand_multiplier.

## inventory_daily
Grain: one row per date × SKU × warehouse (9,720 rows). Fields include date, sku, warehouse_id, opening_stock_units, receipts_units, demand_units, fulfilled_units, lost_units, closing_stock_units, stockout_flag, inventory_value_inr, inventory_position_units, and reorder_point_units. Opening stock includes receipts received on that date.

## purchase_orders
One row per simulated PO: po_id, order_date, sku, warehouse_id, quantity_units, unit_cost_inr, expected_receipt_date, planned_actual_receipt_date, received_date, and status.

## Derived measures
- Fill rate = fulfilled units / demand units.
- Stockout-day rate = SKU–warehouse–days with lost demand / all SKU–warehouse–days.
- Potential lost sales value = lost units × synthetic list price; it is a proxy, not actual revenue.
- On-time PO rate = received POs received on or before expected date / all received POs.
- Estimated carrying cost = sum of daily inventory value × 20% / 365; 20% is an illustrative assumption.