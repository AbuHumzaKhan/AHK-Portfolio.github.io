-- Executive KPIs
SELECT SUM(demand_units) demand_units, SUM(fulfilled_units) fulfilled_units,
       SUM(lost_units) lost_units,
       ROUND(100.0*SUM(fulfilled_units)/NULLIF(SUM(demand_units),0),2) fill_rate_pct,
       ROUND(100.0*SUM(stockout_flag)/COUNT(*),2) stockout_day_rate_pct
FROM inventory_daily;

-- Category comparison
SELECT p.category, SUM(i.demand_units) demand_units, SUM(i.lost_units) lost_units,
       ROUND(100.0*SUM(i.fulfilled_units)/NULLIF(SUM(i.demand_units),0),2) fill_rate_pct,
       ROUND(100.0*SUM(i.stockout_flag)/COUNT(*),2) stockout_day_rate_pct,
       ROUND(SUM(i.lost_units*p.unit_price_inr),2) potential_lost_sales_inr
FROM inventory_daily i JOIN products p USING(sku)
GROUP BY p.category ORDER BY stockout_day_rate_pct DESC;

-- Warehouse service levels
SELECT w.warehouse_name, SUM(i.demand_units) demand_units, SUM(i.lost_units) lost_units,
       ROUND(100.0*SUM(i.fulfilled_units)/NULLIF(SUM(i.demand_units),0),2) fill_rate_pct
FROM inventory_daily i JOIN warehouses w USING(warehouse_id)
GROUP BY w.warehouse_name ORDER BY fill_rate_pct;

-- Priority SKUs
SELECT p.sku,p.product_name,p.category,SUM(i.lost_units) lost_units,
       ROUND(100.0*SUM(i.fulfilled_units)/NULLIF(SUM(i.demand_units),0),2) fill_rate_pct,
       ROUND(SUM(i.lost_units*p.unit_price_inr),2) potential_lost_sales_inr
FROM inventory_daily i JOIN products p USING(sku)
GROUP BY p.sku,p.product_name,p.category
ORDER BY lost_units DESC LIMIT 15;

-- Purchase-order timeliness among received POs
SELECT ROUND(100.0*AVG(CASE WHEN received_date <= expected_receipt_date THEN 1.0 ELSE 0.0 END),2) on_time_pct
FROM purchase_orders WHERE status='Received';