import pandas as pd
import folium

from pkg_estimator import get_data
def map_init(active=True):
    map_folium = folium.Map(
    prefer_canvas=True,
    min_zoom=10,
    max_zoom=15,
    location=(44.816789, -0.572046),
    zoom_control= False)
    return map_folium


def build_carto(
    path="data/girond.csv",
    nom_commune = "Bordeaux",
    type_local = "Maison",
    nature_mutation = "Vente"):

    map_folium = map_init()
    gold_data = get_data.get_gold_data(
    path=path,
    nom_commune = nom_commune,
    type_local = type_local,
    nature_mutation = nature_mutation)

    for index, row in gold_data.iterrows():
        lat = row["latitude"]
        long = row["longitude"]
        folium.CircleMarker([lat, long],
                    radius=5,
                    color="white",
                    weight=1,
                    popup=f"""
                      <div style=width:250px>
                      <p><b>{row['type_local']} - {row["adresse_nom_voie"]}</b></p>
                      <ul>

                         <li><b> Prix</b> : {row['valeur_fonciere']} | <b>Surface</b> : {int(row['surface_reelle_bati'])} m2</li>

                         <li><b> Prix</b> : {int(row['prix_m2'])} € / m2</li>

                      </ul>
                      </div>
                    """,
                    fill_color="blue", # divvy color
                    ).add_to(map_folium)
    return map_folium, gold_data
