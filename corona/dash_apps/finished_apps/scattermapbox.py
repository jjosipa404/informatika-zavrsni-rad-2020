import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from . import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('ScatterMapbox', external_stylesheets=external_stylesheets)
token = 'pk.eyJ1IjoieW9wYTQwNCIsImEiOiJja2VybzViNHgyNjRoMnJtcWhhYjZsd3k2In0.D4b2A8FMk7-kKqFzqgrHIw' 
get_data.get_and_save_countries()

df = pd.read_csv("corona\\dash_apps\\finished_apps\\apicountries.csv") #location,latitude,longitude,confirmed,dead,recovered,updated

fig2 = px.scatter_mapbox(df, lat="latitude", lon="longitude", 
                        hover_name="location",
                        hover_data={"location":False,"latitude":False,"longitude":False,"confirmed":True,"recovered":True,"dead":True,"updated":False},
                        color_continuous_scale=px.colors.sequential.Reds,
                        color="confirmed",size="confirmed",size_max=100,
                        zoom=0.75, height=800,
                        opacity=0.4,
                        title = 'COVID-19 Confirmed Cases (Updated: ' + df["updated"][0] +')'
                        )
fig2.update_layout(mapbox_style="carto-darkmatter", mapbox_accesstoken=token)
fig2.update_layout(margin={"r":0,"l":0})
#------------------------------------------------


app.layout = html.Div([
    dcc.Graph(
        id='example-world',
        figure=fig2
    )
])

