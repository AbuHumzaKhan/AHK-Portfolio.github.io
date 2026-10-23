from __future__ import annotations
import math
from collections import defaultdict
import numpy as np
import pandas as pd
from .config import SEED, START_DATE, DAYS

def generate_data() -> dict[str, pd.DataFrame]:
    """Generate deterministic synthetic inventory, demand, and replenishment data."""
    rng = np.random.default_rng(SEED)
    categories = {
        "Electronics": ["USB-C Hub", "Wireless Mouse", "Keyboard", "Webcam", "Power Bank", "HDMI Adapter", "Headset", "SSD Drive"],
        "Home": ["Storage Box", "Desk Lamp", "Water Bottle", "Laundry Basket", "Kitchen Scale", "Bed Sheet", "Door Mat"],
        "Office": ["Notebook Pack", "Gel Pen Set", "File Folder", "Desk Organizer", "Printer Paper", "Stapler", "Marker Set"],
        "Personal Care": ["Shampoo", "Face Wash", "Hand Cream", "Toothbrush Pack", "Sunscreen", "Body Lotion", "Travel Kit"],
        "Sports": ["Yoga Mat", "Resistance Band", "Sports Bottle", "Skipping Rope", "Gym Towel", "Fitness Gloves", "Foam Roller"],
    }
    warehouse_specs = [
        ("WH-NORTH", "North Hub", 1.10),
        ("WH-CENTRAL", "Central Hub", 1.00),
        ("WH-SOUTH", "South Hub", 0.92),
    ]
    warehouses = pd.DataFrame(warehouse_specs, columns=["warehouse_id", "warehouse_name", "demand_multiplier"])

    products_rows = []
    sku_num = 1
    for category, names in categories.items():
        for name in names:
            base_demand = int(rng.integers(5, 24))
            unit_cost = round(float(rng.uniform(70, 2400)), 2)
            margin = float(rng.uniform(0.18, 0.52))
            unit_price = round(unit_cost * (1 + margin), 2)
            lead_time = int(rng.integers(3, 10))
            pack_size = int(rng.choice([6, 8, 10, 12, 20]))
            daily_std = math.sqrt(base_demand) * float(rng.uniform(0.9, 1.35))
            safety_stock = int(math.ceil(1.65 * daily_std * math.sqrt(lead_time)))
            reorder_point = int(math.ceil(base_demand * lead_time + safety_stock))
            products_rows.append({
                "sku": f"SKU-{sku_num:03d}", "product_name": name, "category": category,
                "base_daily_demand": base_demand, "unit_cost_inr": unit_cost,
                "unit_price_inr": unit_price, "supplier_lead_time_days": lead_time,
                "pack_size": pack_size, "safety_stock_units": safety_stock,
                "reorder_point_units": reorder_point,
            })
            sku_num += 1
    products = pd.DataFrame(products_rows)

    dates = pd.date_range(START_DATE, periods=DAYS, freq="D")
    po_rows: list[dict] = []
    po_by_arrival: dict[tuple[str, str, pd.Timestamp], list[dict]] = defaultdict(list)
    daily_rows: list[dict] = []
    po_counter = 1
    demand_weekday_factor = {0: 1.08, 1: 1.03, 2: 1.00, 3: 1.02, 4: 1.12, 5: 1.18, 6: 0.82}

    for p in products.to_dict("records"):
        for w in warehouses.to_dict("records"):
            avg_demand = p["base_daily_demand"] * w["demand_multiplier"]
            opening = int(max(p["pack_size"], p["reorder_point_units"] * rng.uniform(0.72, 1.35)))
            outstanding: list[dict] = []
            for date in dates:
                receipts = 0
                arrivals_today = po_by_arrival.get((p["sku"], w["warehouse_id"], date), [])
                for po in arrivals_today:
                    receipts += int(po["quantity_units"])
                    po["received_date"] = date.date().isoformat()
                    po["status"] = "Received"
                opening_stock = opening + receipts
                weekday_factor = demand_weekday_factor[date.weekday()]
                month_factor = 1.0 + 0.08 * math.sin((date.day / 31) * math.pi * 2)
                demand = int(rng.poisson(max(0.1, avg_demand * weekday_factor * month_factor)))
                fulfilled = min(demand, opening_stock)
                lost = demand - fulfilled
                closing = opening_stock - fulfilled
                stockout_flag = int(lost > 0)
                inventory_value = round(closing * p["unit_cost_inr"], 2)
                outstanding = [po for po in outstanding if po["status"] != "Received"]
                inventory_position = closing + sum(int(po["quantity_units"]) for po in outstanding)

                daily_rows.append({
                    "date": date.date().isoformat(), "sku": p["sku"], "warehouse_id": w["warehouse_id"],
                    "opening_stock_units": opening_stock, "receipts_units": receipts,
                    "demand_units": demand, "fulfilled_units": fulfilled, "lost_units": lost,
                    "closing_stock_units": closing, "stockout_flag": stockout_flag,
                    "inventory_value_inr": inventory_value, "inventory_position_units": inventory_position,
                    "reorder_point_units": p["reorder_point_units"],
                })
                opening = closing

                if inventory_position <= p["reorder_point_units"] and not any(po["status"] == "Open" for po in outstanding):
                    target_qty = max(p["pack_size"], int(math.ceil(max(avg_demand * 14, p["reorder_point_units"] * 1.15) / p["pack_size"]) * p["pack_size"]))
                    delay = int(rng.choice([0, 1, 2], p=[0.62, 0.25, 0.13]))
                    expected = date + pd.Timedelta(days=p["supplier_lead_time_days"])
                    actual = expected + pd.Timedelta(days=delay)
                    po = {
                        "po_id": f"PO-{po_counter:05d}", "order_date": date.date().isoformat(),
                        "sku": p["sku"], "warehouse_id": w["warehouse_id"],
                        "quantity_units": target_qty, "unit_cost_inr": p["unit_cost_inr"],
                        "expected_receipt_date": expected.date().isoformat(),
                        "planned_actual_receipt_date": actual.date().isoformat(),
                        "received_date": None, "status": "Open",
                    }
                    po_counter += 1
                    po_rows.append(po)
                    outstanding.append(po)
                    po_by_arrival[(p["sku"], w["warehouse_id"], actual)].append(po)

    daily = pd.DataFrame(daily_rows)
    purchase_orders = pd.DataFrame(po_rows)
    # Keep dates that are not received by the end of the observation window as open.
    if not purchase_orders.empty:
        purchase_orders["received_date"] = purchase_orders["received_date"].where(purchase_orders["received_date"].notna(), None)
        purchase_orders["status"] = purchase_orders["received_date"].apply(lambda x: "Received" if pd.notna(x) else "Open")
    return {"products": products, "warehouses": warehouses, "inventory_daily": daily, "purchase_orders": purchase_orders}
