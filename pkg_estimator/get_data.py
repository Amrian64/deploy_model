import pandas as pd
import os
from pathlib import Path


def get_pickle():
    dirname_file = os.path.dirname(__file__)
    dirname_parent = Path(dirname_file)
    print("dirname_parent", dirname_parent)
    print("dirname_file", dirname_file)
    folder = dirname_file
    #type_local = "bdx_maison"
    type_local = "full"
    print("*"*30,f"{folder}/data/{type_local}.pkl")
    data = pd.read_pickle(f"{folder}/data/{type_local}.pkl")
    return data

def get_data(path="data/girond.csv"):


    data = get_pickle()
    #data = pd.read_csv(path)
    #print(data.columns)
    data = data[["date_mutation","nature_mutation","nom_commune","valeur_fonciere","adresse_nom_voie","surface_reelle_bati", "type_local",'longitude', 'latitude']]
    return data


def get_data_selected(data, nom_commune = "Bordeaux",
                      type_local = "Maison",
                      nature_mutation = "Vente"):

    data = data[data["nom_commune"] == nom_commune]
    data = data[data["type_local"] == type_local]
    data = data[data["nature_mutation"] == nature_mutation]

    data = data.dropna(subset=["longitude","latitude", "surface_reelle_bati", "valeur_fonciere"])
    data["prix_m2"] = data["valeur_fonciere"] / data["surface_reelle_bati"]
    # data["prix_m2"] = data.astype({"prix_m2": int})
    return data

def get_gold_data(
    path="data/girond.csv",
    nom_commune = "Bordeaux",
    type_local = "Maison",
    nature_mutation = "Vente"):

    data = get_pickle()
    #data = get_data(path=path)
    data = get_data_selected(data,
        nom_commune = nom_commune,
        type_local = type_local,
        nature_mutation = nature_mutation)

    data = filtre_seuil(data)

    return data

def filtre_seuil(gold_data):
    seuil_filtre_med = int(gold_data[["prix_m2"]].median().values[0])
    seuil_filtre_max = int(gold_data[["prix_m2"]].quantile(q = .80).values[0])
    seuil_filtre_min = int(gold_data[["prix_m2"]].quantile(q = .01).values[0])
    gold_data = gold_data[gold_data["prix_m2"] >= seuil_filtre_min]
    gold_data = gold_data[gold_data["prix_m2"] <= seuil_filtre_max]
    return gold_data


