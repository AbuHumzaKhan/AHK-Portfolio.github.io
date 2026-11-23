# Power BI DAX

Orders = COUNTROWS(Orders)

Late Orders = CALCULATE([Orders], Orders[late_flag] = 1)

SLA Breach % = DIVIDE([Late Orders], [Orders])

On Time % = 1 - [SLA Breach %]

Order Value = SUM(Orders[order_value_inr])

Late Order Value = CALCULATE([Order Value], Orders[late_flag] = 1)

Refund Exposure = SUM(Orders[refund_inr])

Avg Delivery Days = AVERAGE(Orders[actual_days])

First Attempt Failure % = 1 - AVERAGE(Orders[first_attempt_success])
