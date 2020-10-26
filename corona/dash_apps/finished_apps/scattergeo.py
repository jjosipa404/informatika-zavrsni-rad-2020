import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from . import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('ScatterGeo', external_stylesheets=external_stylesheets)
token = 'pk.eyJ1IjoieW9wYTQwNCIsImEiOiJja2VybzViNHgyNjRoMnJtcWhhYjZsd3k2In0.D4b2A8FMk7-kKqFzqgrHIw' 



#------------------------------------------------
datas = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")
datas = datas.groupby(["countriesAndTerritories","month","countryterritoryCode"])[["cases","deaths"]].sum()
datas.reset_index(inplace=True)

fig3 = px.scatter_geo(datas, locations="countryterritoryCode",
            animation_frame = 'month', animation_group = 'countriesAndTerritories', 
            color="cases", size=[ abs(x) for x in datas["cases"]],
            color_continuous_scale=px.colors.sequential.Reds,
            size_max=70, hover_name='countriesAndTerritories', 
            hover_data = ['cases', 'deaths'], 
            projection="natural earth", height=700, width=1500,
            title = 'Visualizing spread of COVID monthly ' )
#-----------------------------------------

app.layout = html.Div([
    dcc.Graph(
        id='slider-world',
        figure=fig3
    )
])

