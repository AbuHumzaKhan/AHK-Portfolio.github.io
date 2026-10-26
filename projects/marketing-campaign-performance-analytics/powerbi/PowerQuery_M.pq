// Create a text parameter named ProjectRoot pointing to the project's data folder.
let
    Source = Csv.Document(File.Contents(ProjectRoot & "\campaign_daily_performance.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"date", type date}, {"campaign_id", type text}, {"campaign_name", type text},
        {"channel", type text}, {"objective", type text}, {"audience_segment", type text},
        {"impressions", Int64.Type}, {"clicks", Int64.Type}, {"spend_usd", Currency.Type},
        {"conversions", Int64.Type}, {"revenue_usd", Currency.Type}, {"daily_budget_usd", Currency.Type}
    }),
    ValidRows = Table.SelectRows(ChangedTypes, each [impressions] >= 0 and [clicks] >= 0 and [clicks] <= [impressions] and [spend_usd] >= 0 and [conversions] >= 0 and [revenue_usd] >= 0)
in
    ValidRows