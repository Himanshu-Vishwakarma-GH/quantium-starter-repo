import pandas as pd
from dash import Dash, Input, Output, dcc, html
import plotly.express as px

df = pd.read_csv('Pink Morsel Sales.csv')
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)


def build_figure(region):
    filtered_df = df if region == "all" else df[df["region"] == region]
    sales_by_date = (
        filtered_df.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    return px.line(
        sales_by_date,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Total Sales"},
        markers=True,
    )


app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Impact of Pink Morsel Price Increase on Sales"),
                html.P(
                    "Use the region filter to compare how sales changed before and after the price increase.",
                ),
            ],
            style={"textAlign": "center", "marginBottom": "24px"},
        ),
        html.Div(
            [
                html.Label(
                    "Select a region:",
                    style={"fontWeight": "600", "marginBottom": "8px", "display": "block"},
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "north", "value": "north"},
                        {"label": "east", "value": "east"},
                        {"label": "south", "value": "south"},
                        {"label": "west", "value": "west"},
                        {"label": "all", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    labelStyle={
                        "marginRight": "16px",
                        "padding": "8px 14px",
                        "borderRadius": "999px",
                        "backgroundColor": "#f3f4f6",
                        "boxShadow": "0 1px 2px rgba(0, 0, 0, 0.06)",
                    },
                ),
            ],
            style={
                "backgroundColor": "white",
                "padding": "18px 20px",
                "borderRadius": "16px",
                "marginBottom": "22px",
                "boxShadow": "0 10px 30px rgba(15, 23, 42, 0.12)",
            },
        ),
        dcc.Graph(
            id="sales-chart",
            figure=build_figure("all"),
            style={"height": "72vh"},
            config={"displayModeBar": False},
        ),
    ],
    style={
        "minHeight": "100vh",
        "padding": "32px",
        "fontFamily": "Arial, sans-serif",
        "background": "linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)",
    },
)


@app.callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_chart(region):
    return build_figure(region)

if __name__ == "__main__":
    app.run(debug=True)