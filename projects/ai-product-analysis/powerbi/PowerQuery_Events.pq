// Update the file path before applying in Power BI Desktop.
let
    Source = Csv.Document(File.Contents("data/interaction_events.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {
        {"event_id", type text}, {"request_id", type text}, {"event_ts", type datetimezone},
        {"event_sequence", Int64.Type}, {"event_type", type text}, {"model_tier", type text},
        {"event_cost_usd", type number}, {"event_latency_ms", Int64.Type}
    })
in
    Types
