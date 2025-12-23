# import pandas as pd
# from dash import Dash, html, dcc
# import plotly.express as px
#
# df=pd.read_csv("output.csv")
# df["Dates"]=pd.to_datetime(df["Dates"])
# df=df.sort_values("Dates")
# app= Dash(__name__)
# fig=px.line(df,
#             x="Dates",
#             y="Sales",
#             title="Pink Morsels Sales Over Time",
#             labels={
#                 "Dates":"Dates",
#                 "Sales":"Sales",
#             }
# )
#
# app.layout=html.Div(children=[
#     html.H1(
#         "Pink Morsels Sales Visualization",
#         style={"text-align": "center"}
#     ),
#     dcc.Graph(
#         figure=fig
#     )
# ])
#
# if __name__=="__main__":
#     app.run(debug=True)

import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["Dates"] = pd.to_datetime(df["Dates"])
df = df.sort_values("Dates")

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "padding": "40px",
        "fontFamily": "Arial"
    },
    children=[

        # Header
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#d63384",
                "marginBottom": "30px"
            }
        ),

        # Radio buttons
        html.Div(
            style={"textAlign": "center", "marginBottom": "20px"},
            children=[
                html.Label(
                    "Filter by Region:",
                    style={"fontWeight": "bold", "marginRight": "10px"}
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "North"},
                        {"label": "East", "value": "East"},
                        {"label": "South", "value": "South"},
                        {"label": "West", "value": "West"},
                    ],
                    value="all",
                    inline=True,
                    style={"fontSize": "16px"}
                ),
            ],
        ),

        # Line chart
        dcc.Graph(id="sales-line-chart")
    ]
)

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Dates",
        y="Sales",
        title="Pink Morsels Sales Over Time",
        labels={
            "Dates": "Dates",
            "Sales": "Total Sales"
        }
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)
