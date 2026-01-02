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

# ================================================
# CREAZIONE & SALVATAGGIO DATABASE
# ================================================

def salva_dati():
    dati = {
        "corsi" : corsi,
        "partecipanti" : partecipanti
        }

    with open("dati.json", "w") as f:
        json.dump(dati, f, indent=4)


    
'''
def check_if_json_db_has_correct_shape(db_name: str) -> bool:
    """Verifica che il db esiste ed è nella forma corretta."""
    if not os.path.isfile(db_name):
        return False
    
    with open(db_name, "r") as f:
        data = json.load(f)
        return isinstance(data, list)
    
def create_json_db(db_name: str) -> bool:
    """Crea un nuovo file db con lista vuota."""
    os.mkdir(os.path.dirname(db_name), exist_ok=True)

    with open(db_name, "w") as f:
        f.write("[]")

    return True

def save_json_db(db_name: str, new_value: dict) -> None:
    """Salva il nuovo oggetto nel db."""    
    if not check_if_json_db_has_correct_shape(db_name):
        create_json_db(db_name)

    db: list[dict] = []

    with open(db_name, "r") as f:
        db.extend(json.load(f))

    db.append(new_value)

    with open(db_name, "w", encoding='utf-8') as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
'''


# 1. Il Database (la lista vuota all'inizio)
corsi = []
partecipanti = []


# ================================================
# ASSEGNAZIONE GOLEADOR
# ================================================
'''
1. Controllare se abbiamo gli ingredienti (ci sono corsi? ci sono persone?).
2. Far scegliere l'utente (chi iscrivo? dove?).
3. Salvare il collegamento.'''

def assegna_goleador():
    # CONTROLLO INIZIALE
    # Se la lista corsi è vuota OPPURE (or) la lista partecipanti è vuota
    if len(corsi) == 0 or len(partecipanti) == 0:
        print("⚠️ Attenzione: mancano corsi o partecipanti!")
        print("Aggiungili dal menu principale prima di fare assegnazioni.")
        return # Questo comando fa uscire subito dalla funzione
    
    print("Seleziona un partecipante:")
    # 1. Correggi: metti 'partecipante' (singolo) e 'partecipanti' (lista) al posto giusto
    for i, partecipante in enumerate(partecipanti):
        # 2. Correggi: stampa solo il nome e cognome usando le chiavi ['...']
        print(f"{i}. {partecipante['nome_partecipante']} {partecipante['cognome_partecipante']}")
    
    indice_partecipante = int(input("Inserisci il numero del partecipante: "))

    print("Seleziona un corso:")
    for i, corso in enumerate(corsi):
        # 2. Correggi: stampa solo il nome e cognome usando le chiavi ['...']
        print(f"{i}. {corso['nome_corso']} {corso['numero_posti']}")        
    indice_corso = int(input("Inserisci il numero del corso: "))


# 1. Recuperiamo i dizionari veri
    partecipante_selezionato = partecipanti[indice_partecipante]
    corso_selezionato = corsi[indice_corso]
    
# 2. Stampa di conferma
    print(f"Stai dando Goleador a {partecipante_selezionato['nome_partecipante']} che è nel {corso_selezionato['nome_corso']}")

# 3. INPUT: Chiediamo il numero 
    quantita = int(input("Quante Goleador vuoi assegnare? "))
    
# 4. CALCOLO: Recupera il vecchio, somma il nuovo  
    goleador_precedenti = partecipante_selezionato.get('goleador', 0)
    nuovo_totale = goleador_precedenti + quantita 

# 5. AGGIORNAMENTO
    partecipante_selezionato['goleador'] = nuovo_totale
    print(f"Fatto, Ora ne ha {nuovo_totale}")

    salva_dati()


# ================================================
# 02. PARTECIPANTI
# ================================================

# 2. La funzione "Operaia": aggiungi partecipanti
def aggiungi_partecipante():
    aggiungi_nome_partecipante = input("Scrivi di seguito il nome del partecipante: ")
    aggiungi_cognome_partecipante = input("Scrivi di seguito il cognome del partecipante: ")
    
    # Creiamo il dizionario
    nuovo_partecipante = {
        "nome_partecipante": aggiungi_nome_partecipante,
        "cognome_partecipante": aggiungi_cognome_partecipante,
    }

    # Viene salvato nella lista globale
    partecipanti.append(nuovo_partecipante)
    print(f"Nome: {nuovo_partecipante['nome_partecipante']} - Cognome: {nuovo_partecipante['cognome_partecipante']}")  

# 3. La funzione "Vigile": smista il traffico
def gestisci_partecipanti():
    scelta2 = input("Hai scelto i partecipanti - Premi 'v' per visualizzare o 'a' per aggiungere: ")
    
    if scelta2 == 'v':
        if len(partecipanti) == 0:
            print("⚠️  La lista dei partecipanti è vuota!")
            conferma = input("Vuoi aggiungere un nuovo partecipante ora? (s/n): ")
            if conferma == 's':
                aggiungi_partecipante()
        print("Ecco la lista dei partecipanti: ")
        # Ciclo for
        for partecipante in partecipanti:
            print(f"Nome: {partecipante['nome_partecipante']} - Cognome: {partecipante['cognome_partecipante']}")  
    elif scelta2 == 'a':
        aggiungi_partecipante()

    salva_dati()



# ================================================
# 01. CORSI
# ================================================

# 2. La funzione "Operaia": crea il corso
def aggiungi_corso():
    aggiungi_nome_corso = input("Scrivi di seguito il nome del corso: ")
    numero_posti_massimo = input("Scrivi il numero di posti massimo del corso: ")
    
    # Creiamo il dizionario
    nuovo_corso = {
        "nome_corso": aggiungi_nome_corso,
        "numero_posti": numero_posti_massimo,
    }

    # Viene salvato nella lista globale
    corsi.append(nuovo_corso)
    print(f"Corso '{nuovo_corso['nome_corso']}' (Max {nuovo_corso['numero_posti']} posti) aggiunto correttamente.")

# 3. La funzione "Vigile": smista il traffico
def gestisci_corsi():
    scelta1 = input("Hai scelto i corsi - Premi 'v' per visualizzare o 'a' per aggiungere: ")
    
    if scelta1 == 'v':
        if len(corsi) == 0:
            print("⚠️  La lista dei corsi è vuota!")
            conferma = input("Vuoi aggiungere un nuovo corso ora? (s/n): ")
            if conferma == 's':
                aggiungi_corso()
        else:
            print("Ecco la lista dei corsi: ")
        # Ciclo for
        for corso in corsi:
                print(f"Nome: {corso['nome_corso']} - Posti: {corso['numero_posti']}")  
            
    elif scelta1 == 'a':
        aggiungi_corso()

    salva_dati()

# ================================================
# MAIN
# ================================================

# 4. Il Menu Principale (Il ciclo di vita del programma)
programma_attivo = True

while programma_attivo == True:
    print("\n---MENU PRINCIPALE---")
    print("1. Gestisci corsi")
    print("2. Partecipanti")
    print("3. Assegnazione Goleador")
    print("4. Analytics & Statistiche")
    print("0. Exit")

    scelta = input("Inserisci un'opzione: ")

    if scelta == "0":
        programma_attivo = False
        print("Arrivederci")
        break

    elif scelta == "1":
        gestisci_corsi()

    elif scelta == "2":
        gestisci_partecipanti()

    elif scelta == "3":
        assegna_goleador()

    elif scelta == "4":
        print("Hai scelto le Analytics & Statistiche")
        
    else:
        print("Inserisci un numero dall'elenco")