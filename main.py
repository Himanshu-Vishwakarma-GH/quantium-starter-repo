import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv('Pink Morsel Sales.csv')
df["date"] = pd.to_datetime(df["date"])

sales_by_date = df.groupby("date", as_index=False)["sales"].sum().sort_values("date")
sales_by_date.head()

fig = px.line(
sales_by_date,
x="date",
y="sales",
title="Pink Morsel Total Sales Over Time",
labels={"date": "Date", "sales": "Total Sales"},
)

app = Dash(__name__)

app.layout = html.Div( [ html.H1("Impact of Pink Morsel Price Increase on Sales"), dcc.Graph(figure=fig) ] )

if __name__ == "__main__":
    app.run(debug=True)