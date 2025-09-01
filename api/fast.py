from fastapi import FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware
from pkg_estimator import carto
import os


app = FastAPI(
    title= "Estimator",
)

@app.get("/")
def welcome(input_user):
    response = e.predict(input_user)
    return {"response": response}

@app.get('/map', response_class=HTMLResponse)

def map(nom_commune: str = "Bordeaux", type_local: str = "Maison"):
    map_folium, gold_data = carto.build_carto(
        nom_commune = nom_commune,
        type_local = type_local,
        nature_mutation = "Vente")


    return map_folium.get_root().render()
