"GEMINI GEM = https://gemini.google.com/gem/1HOZjA5ibxeSk-AKGGa0ToZyXxjtzD-zh?usp=sharing"

# ===============
# LOGICA
# ===============

'''
Menu

1. Corsi:
    a. Lista corsi esistenti
    b. Aggiungi corso
    c. Elimina corso

2. Partecipanti:
    a. Lista partecipanti
        i. Nome
        ii. Cognome
        iii. Corso che segue
        iiii. Goleador vinte
    b. Iscrivere un nuovo partecipante
    c. Rimuovere un partecipante

3. Assegnazione goleador:
    a. Quante goleador sono state vinte?
    b. Chi le ha vinte?
    c. Quando sono state vinte? Date and time - timestamp

4. Analytics / Statistiche:
    a. Totale goleador vinte per ogni corso
    b. Top scorer di ogni corso
    c. Identificare la Top Scorer
'''

# ===============
# JSON FILE
# ===============

''' {
        "corso_nome": "Python junior",
        "partecipanti": [
            {
            "nome" : "Anna",
            "cognome" : "Rossi",
            "goleadore" : "x"
            },
            {
            "nome" : "Mario",
            "cognome" : "Bianchi",
            "goleadore" : "y"
            } 
            ]
    }
'''

# ===============
# Pseudocodice
# ===============

'''
SE il file data.json esiste:
    dati = leggi il contenuto del file
ALTRIMENTI:
    dati = crea contenitore vuoto
'''

# Logica di Caricamento.
import os
import json

if os.path.exists ("data.json"):
    # Qui vanno caricare i dati veri
    with open("data.json", "r") as f:
        data = json.load(f)
else:
    data = []

corsi = []

def aggiungi_corso():
    aggiungi_nome_corso = input("Scrivi di seguito il nome del corso: ")
    numero_posti_massimo = input("Scrivi il numero di posti massimo del corso: ")
    nuovo_corso = {
        "nome_corso": aggiungi_nome_corso,
        "numero_posti": numero_posti_massimo,
    }
    corsi.append(nuovo_corso)

    print(f"Il nome del corso è {aggiungi_nome_corso} e il numero massimo dei posti è {numero_posti_massimo}")

def gestisci_corsi():
    scelta1 = input("Hai scelto i corsi - Premi 'v' per visualizzare o 'a' per aggiungere: ")
    if scelta1 == 'v':
        print("Hai scelto di visualizzare la lista dei corsi")
    elif scelta1 == 'a':
        aggiungi_corso()

# ==========

programma_attivo = True
while programma_attivo == True:
    print("1. Corsi\n2. Partecipanti\n3. Assegnazione Goleador\n4. Analytics & Statistiche\n0. Exit")
    scelta = input("Inserisci un numero: ")

    if scelta == "0":
        programma_attivo = False
        print("Hai scelto di uscire del programma")

    elif scelta == "1":
        gestisci_corsi()

    elif scelta == "2":
        print("Hai scelto i partecipanti")

    elif scelta == "3":
        print("Hai scelto le assegnazione goleador")

    elif scelta == "4":
        print("Hai scelto le Analytics & Statistiche")