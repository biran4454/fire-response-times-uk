import pandas as pd
import os
import json

df = pd.read_csv('firestats-edit1.csv')

import folium
from branca.utilities import split_six
state_geo = "Counties_(December_2021)_EN_BFC.geojson" #'http://geoportal1-ons.opendata.arcgis.com/datasets/01fd6b2d7600446d8af768005992f76a_4.geojson'

m = folium.Map(location=[55, 4], zoom_start=5)
m.choropleth(
    geo_data=state_geo,
    data=df,
    columns=["LOCATION_CATEGORY", "TOTAL_RESPONSE_TIME"],
    key_on='feature.properties.CTY21NM',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Response Time',
    highlight=True
)
m
m.save("./test.html")
