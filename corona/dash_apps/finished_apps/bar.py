import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from . import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Bar', external_stylesheets=external_stylesheets)
token = 'pk.eyJ1IjoieW9wYTQwNCIsImEiOiJja2VybzViNHgyNjRoMnJtcWhhYjZsd3k2In0.D4b2A8FMk7-kKqFzqgrHIw' 

df2 = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")
df2 = df2.iloc[::-1]
#columns: dateRep,day,month,year,cases,deaths,countriesAndTerritories,geoId,countryterritoryCode,
#popData2019,continentExp,Cumulative_number_for_14_days_of_COVID-19_cases_per_100000
#------------------------------------------------
data = df2.groupby(["countriesAndTerritories","continentExp"])[["cases","deaths"]].sum()
data.reset_index(inplace=True)

#------------------------------------------------

fig = px.bar(data, x="continentExp", y="cases",color="countriesAndTerritories")

fig2 = px.bar(data.loc[data["continentExp"] == "Europe"], x="countriesAndTerritories", y="cases",color="countriesAndTerritories")

fig2.update_layout(xaxis_tickangle=-45)
#------------------------------------------------

options = data["continentExp"]
col_options = [dict(label=x, value=x) for x in data["continentExp"]]



app.layout = html.Div([
    dcc.Graph(
        figure=fig
    ),
    html.H4('Choose a continent:'),
    dcc.Dropdown(
        id="dropdown",
        options=col_options,
        value='Europe'
        ),
     dcc.Graph(
        id='graph',
        figure=fig2
    )
])


@app.callback(
    Output('graph','figure'),
    [Input(component_id='dropdown', component_property='value')]
    )

def update_graph(option_slctd):
    return px.bar(data.loc[data["continentExp"] == option_slctd],
    x="countriesAndTerritories", 
    y="cases",
    color="countriesAndTerritories")

