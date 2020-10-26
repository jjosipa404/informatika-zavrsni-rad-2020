import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from . import get_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Travel', external_stylesheets=external_stylesheets)
token = 'pk.eyJ1IjoieW9wYTQwNCIsImEiOiJja2VybzViNHgyNjRoMnJtcWhhYjZsd3k2In0.D4b2A8FMk7-kKqFzqgrHIw' 
get_data.get_and_save_countries()

df = pd.read_csv("corona\\dash_apps\\finished_apps\\apicountries.csv") #location,latitude,longitude,confirmed,dead,recovered,updated
df_travel = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTxATUFm0tR6Vqq-UAOuqQ-BoQDvYYEe-BmJ20s50yBKDHEifGofP2P1LJ4jWFIu0Pb_4kRhQeyhHmn/pub?gid=0&single=true&output=csv')
df_travel=pd.DataFrame({
            'adm0_name' : list(df_travel["adm0_name"]),
            'iso3':list(df_travel["iso3"]),
            'X':list(df_travel["X"]),
            'Y':list(df_travel["Y"]),
            'published':list(df_travel["published"]),
            'sources':list(df_travel["sources"]),
            'info':list(df_travel["info"]),
            'optional1':list(df_travel["optional1"]),
            'optional2':list(df_travel["optional2"]),
            'optional3':list(df_travel["optional3"]),
            'ObjectId':list(df_travel["ObjectId"]),
        })

fig2 = px.scatter_mapbox(df_travel, lat="Y", lon="X", 
                        hover_name="adm0_name",
                        hover_data={"adm0_name":False,"iso3":False,"X":False,"Y":False,"published":False,"sources":False,"optional1":False,"optional2":False,"optional3":True,"info":False,"ObjectId":False},
                        zoom=3, height=800,
                        opacity=0.4
                        )
fig2.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig2.update_layout(margin={"r":0,"l":0})
#------------------------------------------------

fig = go.Figure(data=[go.Table(
    header=dict(values=["adm0_name","optional2","optional3"],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_travel["adm0_name"], df_travel["optional2"],df_travel["optional3"]],
               fill_color='lavender',
               align='left'))
])

#-----------------------------------------

app.layout = html.Div([
    dcc.Graph(
        id='example-world',
        figure=fig2
    )
])


