# E-Commerce Delivery SLA & Late Shipment Analytics

Portfolio project by Abu Humza Khan.

This project analyzes a synthetic 24,000-order e-commerce delivery operation to support carrier, city, service-level and customer-impact decisions.

## Business problem
Operations leadership needs to reduce late deliveries without blindly moving orders to premium services. The analysis identifies SLA breach hotspots, carrier performance, premium-service risk, affected order value and modeled refund exposure.

## Modeled KPIs
- Orders: 24,000
- SLA breach rate: 12.60%
- Average delivery time: 2.84 days
- Late-order value: INR 38.52 lakh
- Modeled refund exposure: INR 1.34 lakh
- Late orders: 3,023

## Key findings
- BlueDartX has the lowest modeled carrier breach rate; RapidGo has the highest.
- Express and Same Day have materially higher modeled breach rates because their customer promises are tighter.
- City-level exception analysis is more useful than carrier averages alone because route and service mix differ.
- Late-order value provides a stronger prioritization lens than late-order count alone.

## Important interpretation
The dataset is synthetic and observational. Carrier performance is not a causal estimate and must not be presented as real company performance.

## Technical stack
Python, SQL/SQLite, Excel, Power BI-ready DAX/M, HTML/CSS/JS.

A native Power BI .pbix is not generated. DAX, Power Query M, model and report instructions are included.

## Dataset provenance
Synthetic data generated with deterministic seed 20261123 for portfolio demonstration. Period: 2026-07-01 to 2026-09-30.

## Credits
Created by: Abu Humza Khan
GitHub profile: https://github.com/AbuHumzaKhan
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/
Source: ChatGPT
Design Idea: ChatGPT

Change log: 2026-11-23 - Project 10 created, validated and portfolio showcase published.
