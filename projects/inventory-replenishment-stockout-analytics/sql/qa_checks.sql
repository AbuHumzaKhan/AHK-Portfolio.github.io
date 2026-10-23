-- These checks should return zero rows.
SELECT date,sku,warehouse_id,COUNT(*) row_count FROM inventory_daily
GROUP BY date,sku,warehouse_id HAVING COUNT(*) > 1;
SELECT * FROM inventory_daily
WHERE demand_units <> fulfilled_units + lost_units
   OR stockout_flag <> CASE WHEN lost_units > 0 THEN 1 ELSE 0 END
   OR opening_stock_units < 0 OR fulfilled_units < 0 OR lost_units < 0 OR closing_stock_units < 0;
SELECT i.sku FROM inventory_daily i LEFT JOIN products p USING(sku) WHERE p.sku IS NULL;
SELECT i.warehouse_id FROM inventory_daily i LEFT JOIN warehouses w USING(warehouse_id) WHERE w.warehouse_id IS NULL;