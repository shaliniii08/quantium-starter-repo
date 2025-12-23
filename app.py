import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df=pd.read_csv("output.csv")
df["Dates"]=pd.to_datetime(df["Dates"])
df=df.sort_values("Dates")
app= Dash(__name__)
fig=px.line(df,
            x="Dates",
            y="Sales",
            title="Pink Morsels Sales Over Time",
            labels={
                "Dates":"Dates",
                "Sales":"Sales",
            }
)

app.layout=html.Div(children=[
    html.H1(
        "Pink Morsels Sales Visualization",
        style={"text-align": "center"}
    ),
    dcc.Graph(
        figure=fig
    )
])

if __name__=="__main__":
    app.run(debug=True)