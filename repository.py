import json
import os

def salva_dati(lista_corsi, lista_partecipanti):
    db_completo = {
        "corsi" : lista_corsi,
        "partecipanti" : lista_partecipanti
    }

    with open("dati.json", "w") as f:
        json.dump(db_completo, f, indent=4)

def carica_dati():
    filename = "dati.json"

    if not os.path.exists(filename):
        return [], []
    
    try:
        with open(filename, "r") as f:
            db_completo = json.load(f)

            lista_corsi = db_completo.get("corsi", [])
            lista_partecipanti = db_completo.get("partecipanti", [])

            return lista_corsi, lista_partecipanti
        
    except (json.JSONDecodeError, IOError):
        return [], []