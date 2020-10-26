import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from . import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Pie', external_stylesheets=external_stylesheets)
token = 'pk.eyJ1IjoieW9wYTQwNCIsImEiOiJja2VybzViNHgyNjRoMnJtcWhhYjZsd3k2In0.D4b2A8FMk7-kKqFzqgrHIw' 
get_data.get_and_save_countries()
df = pd.read_csv("corona\\dash_apps\\finished_apps\\apicountries.csv") #location,latitude,longitude,confirmed,dead,recovered,updated


#------------------------------------------------
data = df.groupby(["location"])[["confirmed"]].sum()
data.reset_index(inplace=True)
options = df["location"]
col_options = [dict(label=x, value=x) for x in data["location"]]
#------------------------------------------------
app.layout = html.Div([
    html.H4("Choose a country to show it's statistics:"),
    dcc.Dropdown(
        id="dropdown",
        options=col_options,
        value='Croatia'
        ),
    dcc.Graph(
            id="graph",
            figure=px.pie(df.loc[df["location"] == "Croatia"],
            names=["confirmed","dead","recovered"], 
            values=[df.loc[df["location"] == "Croatia"]["confirmed"],df.loc[df["location"] == "Croatia"]["dead"],df.loc[df["location"] == "Croatia"]["recovered"]], 
            hole=0.4
        ))

])

#-----------------------------------------
@app.callback(
    Output('graph','figure'),
    [Input(component_id='dropdown', component_property='value')]
    )


def update_graph(option_slctd):
    return px.pie(df.loc[df["location"] == option_slctd],
            names=["confirmed","dead","recovered"], 
            values=[df.loc[df["location"] == option_slctd]["confirmed"],df.loc[df["location"] == option_slctd]["dead"],df.loc[df["location"] == option_slctd]["recovered"]], 
            hole=0.4
        )




