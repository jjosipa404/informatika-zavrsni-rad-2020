import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from . import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Line', external_stylesheets=external_stylesheets)
token = 'pk.eyJ1IjoieW9wYTQwNCIsImEiOiJja2VybzViNHgyNjRoMnJtcWhhYjZsd3k2In0.D4b2A8FMk7-kKqFzqgrHIw' 



df = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")
df = df.iloc[::-1]
#columns: dateRep,day,month,year,cases,deaths,countriesAndTerritories,geoId,countryterritoryCode,
#popData2019,continentExp,Cumulative_number_for_14_days_of_COVID-19_cases_per_100000
#------------------------------------------------
data = df.groupby(["countriesAndTerritories"])[["cases"]].sum()
data.reset_index(inplace=True)

#------------------------------------------------




#------------------------------------------------


options = df["countriesAndTerritories"]
col_options = [dict(label=x, value=x) for x in data["countriesAndTerritories"]]

app.layout = html.Div([
    html.H4('Choose a country to show the line chart of cases vs deaths:'),
    dcc.Dropdown(
        id="dropdown",
        options=col_options,
        value='Croatia'
        ),
    dcc.Graph(
            id="graph",
            figure=px.line(df.loc[df["countriesAndTerritories"] == "Croatia"],
             x="dateRep", y="cases",
             color="month", 
             hover_data=["countriesAndTerritories"],height=700)
        )
])

@app.callback(
    Output('graph','figure'),
    [Input(component_id='dropdown', component_property='value')]
    )


def update_graph(option_slctd):
    return px.line(df.loc[df["countriesAndTerritories"] == option_slctd],
     x="dateRep", y="cases",color="month", hover_data=["countriesAndTerritories"])

