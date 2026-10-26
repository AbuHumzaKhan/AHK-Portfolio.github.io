// Query name: Campaigns. Uses the ProjectRoot text parameter.
let
    Source = Csv.Document(File.Contents(ProjectRoot & "\campaigns.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {{"campaign_id", type text}, {"campaign_name", type text}, {"channel", type text}, {"objective", type text}, {"audience_segment", type text}, {"daily_budget_usd", Currency.Type}}),
    UniqueCampaigns = Table.Distinct(ChangedTypes, {"campaign_id"})
in
    UniqueCampaigns