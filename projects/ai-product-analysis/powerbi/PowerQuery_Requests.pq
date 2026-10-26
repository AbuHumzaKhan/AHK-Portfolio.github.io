// Update the file path before applying in Power BI Desktop.
let
    Source = Csv.Document(File.Contents("data/ai_requests.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {
        {"request_id", type text}, {"request_ts", type datetimezone}, {"product_area", type text},
        {"model_tier", type text}, {"user_segment", type text}, {"prompt_version", type text},
        {"input_tokens_total", Int64.Type}, {"output_tokens_total", Int64.Type}, {"total_tokens", Int64.Type},
        {"regeneration_count", Int64.Type}, {"edit_size_pct", type number}, {"final_outcome", type text},
        {"request_status", type text}, {"total_latency_ms", Int64.Type}, {"input_cost_usd", type number},
        {"output_cost_usd", type number}, {"total_cost_usd", type number}, {"successful_output", Int64.Type},
        {"was_regenerated", Int64.Type}
    }),
    AddMonth = Table.AddColumn(Types, "Request Month", each Date.StartOfMonth(Date.From(DateTimeZone.RemoveZone([request_ts]))), type date)
in
    AddMonth
