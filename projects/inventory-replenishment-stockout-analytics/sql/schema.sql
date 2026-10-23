PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS products (
  sku TEXT PRIMARY KEY, product_name TEXT NOT NULL, category TEXT NOT NULL,
  base_daily_demand INTEGER NOT NULL CHECK(base_daily_demand >= 0),
  unit_cost_inr REAL NOT NULL CHECK(unit_cost_inr >= 0),
  unit_price_inr REAL NOT NULL CHECK(unit_price_inr >= 0),
  supplier_lead_time_days INTEGER NOT NULL CHECK(supplier_lead_time_days > 0),
  pack_size INTEGER NOT NULL CHECK(pack_size > 0),
  safety_stock_units INTEGER NOT NULL CHECK(safety_stock_units >= 0),
  reorder_point_units INTEGER NOT NULL CHECK(reorder_point_units >= 0)
);
CREATE TABLE IF NOT EXISTS warehouses (
  warehouse_id TEXT PRIMARY KEY, warehouse_name TEXT NOT NULL,
  demand_multiplier REAL NOT NULL CHECK(demand_multiplier > 0)
);
CREATE TABLE IF NOT EXISTS inventory_daily (
  date TEXT NOT NULL, sku TEXT NOT NULL REFERENCES products(sku),
  warehouse_id TEXT NOT NULL REFERENCES warehouses(warehouse_id),
  opening_stock_units INTEGER NOT NULL CHECK(opening_stock_units >= 0),
  receipts_units INTEGER NOT NULL CHECK(receipts_units >= 0),
  demand_units INTEGER NOT NULL CHECK(demand_units >= 0),
  fulfilled_units INTEGER NOT NULL CHECK(fulfilled_units >= 0),
  lost_units INTEGER NOT NULL CHECK(lost_units >= 0),
  closing_stock_units INTEGER NOT NULL CHECK(closing_stock_units >= 0),
  stockout_flag INTEGER NOT NULL CHECK(stockout_flag IN (0,1)),
  inventory_value_inr REAL NOT NULL CHECK(inventory_value_inr >= 0),
  inventory_position_units INTEGER NOT NULL CHECK(inventory_position_units >= 0),
  reorder_point_units INTEGER NOT NULL CHECK(reorder_point_units >= 0),
  PRIMARY KEY(date,sku,warehouse_id),
  CHECK(demand_units = fulfilled_units + lost_units)
);
CREATE TABLE IF NOT EXISTS purchase_orders (
  po_id TEXT PRIMARY KEY, order_date TEXT NOT NULL,
  sku TEXT NOT NULL REFERENCES products(sku),
  warehouse_id TEXT NOT NULL REFERENCES warehouses(warehouse_id),
  quantity_units INTEGER NOT NULL CHECK(quantity_units > 0),
  unit_cost_inr REAL NOT NULL CHECK(unit_cost_inr >= 0),
  expected_receipt_date TEXT NOT NULL, planned_actual_receipt_date TEXT NOT NULL,
  received_date TEXT, status TEXT NOT NULL CHECK(status IN ('Received','Open'))
);
CREATE INDEX IF NOT EXISTS idx_inventory_date ON inventory_daily(date);
CREATE INDEX IF NOT EXISTS idx_inventory_sku_wh ON inventory_daily(sku,warehouse_id);
CREATE INDEX IF NOT EXISTS idx_po_order_date ON purchase_orders(order_date);