from django.shortcuts import render
import requests
import pandas as pd


def get_summary():
    url = 'https://api.covid19api.com/summary'
    r = requests.get(url)
    data = r.json()
    return data

def get_travel_data():
    url = 'https://www.trackcorona.live/api/travel' 
    r = requests.get(url)
    data = r.json()
    return data

def by_countries_data():
    url = 'https://www.trackcorona.live/api/countries' 
    r = requests.get(url)
    data = r.json()
    return data    

def country_data(alpha2):
    url = "https://www.trackcorona.live/api/countries/" + alpha2
    r = requests.get(url)
    data = r.json()
    return data  

def get_country_codes():
    url = "https://api.printful.com/countries"
    r = requests.get(url)
    data = r.json()
    return data["result"]