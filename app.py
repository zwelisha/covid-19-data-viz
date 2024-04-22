import json
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as graph_obj
import pandas as pd


file = open("covid.json", "r")
data = json.load(file)
file.close()

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    children=[
        html.Title("Zweli Visuals"),
        html.H1(
            "COVID-19 Data Analysis and Visualisation",
            style={"color": "white", "backgroundColor": "maroon", "padding": "15px"},
        ),
        html.Label("Select variable to plot and visualise:"),
        dcc.Dropdown(
            id="variable-label",
            options=[
                {"label": "Total Confirmed Cases", "value": "Total Confirmed Cases"},
                {"label": "Total Deaths", "value": "Total Deaths"},
                {"label": "Total Recovered", "value": "Total Recovered"},
                {"label": "Active Cases", "value": "Active Cases"},
                {"label": "Daily Confirmed Cases", "value": "Daily Confirmed Cases"},
                {"label": "Daily Deaths", "value": "Daily Deaths"},
            ],
            value="Total Confirmed Cases",
        ),
        dcc.Graph(id="covid-line-graph"),
        html.Footer(
            children=[
                html.Div(
                    style={
                        "color": "maroon",
                    },
                    children=[html.P("copyright @2024 Developed By Zweli Mthethwa")],
                )
            ]
        ),
    ]
)


@app.callback(Output("covid-line-graph", "figure"), [Input("variable-label", "value")])
def update_graph(selected_data):
    trace = graph_obj.Scatter(
        x=df["Date"],
        y=df[selected_data],
        mode="lines+markers",
        marker=dict(color="maroon"),
        name=selected_data,
    )
    layout = graph_obj.Layout(
        title="COVID-19 insights from March 2020 to June 2020 for the selected variable",
        xaxis=dict(title="Date"),
        yaxis=dict(title=selected_data),
    )
    return {"data": [trace], "layout": layout}


if __name__ == "__main__":
    app.run_server(debug=True)
