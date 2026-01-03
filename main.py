"GEMINI GEM = https://gemini.google.com/gem/1HOZjA5ibxeSk-AKGGa0ToZyXxjtzD-zh?usp=sharing"

# ===============
# LOGICA
# ===============

'''
Menu

1. Corsi:
    a. ✅ Lista corsi esistenti 
    b. ✅ Aggiungi corso
    c. Elimina corso

2. Partecipanti:
    a. ✅ Lista partecipanti
        i. Nome
        ii. Cognome
        iii. Corso che segue
        iiii. Goleador vinte
    b. ✅ Iscrivere un nuovo partecipante
    c. ✅ Rimuovere un partecipante

3. Assegnazione goleador:
    a. ✅ Assegna goleador
    b. ✅ rimuovi goleador
    e. ✅rimuovere goleador

4. Analytics / Statistiche:
    a. Totale goleador vinte per ogni corso
    b. Top scorer di ogni corso
    c. Identificare la Top Scorer
    d. Quando sono state vinte? Date and time - timestamp

'''

import os
import json

# ================================================
# CREAZIONE & SALVATAGGIO DATABASE
# ================================================

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

# 1. Il Database (la lista vuota all'inizio)
corsi, partecipanti = carica_dati()

# ================================================
# ASSEGNAZIONE GOLEADOR
# ================================================

'''
1. Controllare se abbiamo gli ingredienti (ci sono corsi? ci sono persone?).
2. Far scegliere l'utente (chi iscrivo? dove?).
3. Salvare il collegamento.
'''

def rimuovere_goleador():
    if len(partecipanti) == 0:
        print("⚠️ Non ci sono partecipanti.")
        return

    print("\n--- RIMUOVI GOLEADOR ➖🍬 ---")

    for i, p in enumerate(partecipanti):
        goleador_attuali = p.get('goleador', 0)
        print(f"{i}. {p['nome_partecipante']} {p['cognome_partecipante']} (Attuali: {goleador_attuali})")

    indice = richiedi_indice_valido(partecipanti)
    partecipante = partecipanti[indice]

    goleador_attuali = partecipante.get('goleador', 0)

    while True:
        try:
            da_rimuovere = int(input(f"Quante goleador vuoi rimuovere a {partecipante['nome_partecipante']}? "))

            if da_rimuovere < 0:
                print("⚠️ Non puoi togliere un numero negativo (sarebbe un'aggiunta!).")
            elif da_rimuovere > goleador_attuali:
                print(f"⚠️ Errore: Ne ha solo {goleador_attuali}, non puoi toglierne {da_rimuovere}!")
            else:
                break
        except ValueError:
            print("inserisci un numero intero")

    nuovo_totale = goleador_attuali - da_rimuovere
    partecipante['goleador'] = nuovo_totale

    print(f"✅Fatto. Ora 👤 {partecipante['nome_partecipante']} ha 🍬 {nuovo_totale}")

    salva_dati(corsi, partecipanti)


def richiedi_indice_valido(lista_riferimento):
    while True:
        try:
            valore = int(input("Inserisci il numero corrispondente: "))
            
            # Controlliamo se il numero è dentro i limiti della lista
            if 0 <= valore < len(lista_riferimento):
                return valore # È valido! Usciamo e restituiamo il numero
            else:
                max_indice = len(lista_riferimento) - 1
                if max_indice == 0:
                    print(f"⚠️ Errore: C'è solo un'opzione (0). Inserisci 0.")
                else:
                    print(f"⚠️ Errore: Inserisci un numero tra 0 e {max_indice}.")
                
        except ValueError:
            # Succede se l'utente scrive lettere invece di numeri
            print("⚠️ Errore: Devi inserire un numero intero, non parole!")

def assegna_goleador():
# --- CONTROLLO INIZIALE ---
    if len(corsi) == 0 or len(partecipanti) == 0:
        print("⚠️ Attenzione: mancano corsi o partecipanti!")
        print("Aggiungili dal menu principale prima di fare assegnazioni.")
        return # Questo comando fa uscire subito dalla funzione
    
# --- SELEZIONE PARTECIPANTE ---
    print("Seleziona un partecipante:")
    for i, partecipante in enumerate(partecipanti):
        print(f"{i}. {partecipante['nome_partecipante']} {partecipante['cognome_partecipante']}")
    
    indice_partecipante = richiedi_indice_valido(partecipanti)

# --- LOGICA DI ASSEGNAZIONE ---
    partecipante_selezionato = partecipanti[indice_partecipante]
    nome_corso = partecipante_selezionato.get("corso", "Nessun corso")

# 2. Stampa di conferma
    print(f"\nStai dando Goleador a {partecipante_selezionato['nome_partecipante']} del corso {nome_corso}")

# 3. INPUT: Chiediamo il numero 
    
    while True:
        try:
            quantita = int(input("Quante Goleador vuoi assegnare? "))
            if quantita > 0:
                break
            print("Devi assegnare almeno una goleador")
        except ValueError:
            print("Inserisci un numero valido")
    
# 4. CALCOLO: Recupera il vecchio, somma il nuovo  
    goleador_precedenti = partecipante_selezionato.get('goleador', 0)
    nuovo_totale = goleador_precedenti + quantita 

# 5. AGGIORNAMENTO
    partecipante_selezionato['goleador'] = nuovo_totale
    salva_dati(corsi, partecipanti)
    print(f"✅Fatto, Ora {partecipante_selezionato['nome_partecipante']} ne ha {nuovo_totale}")

# ================================================
# 02. PARTECIPANTI
# ================================================

def rimuovi_partecipante():
    if len(partecipanti) == 0:
        print("Non ci sono partecipanti da eliminare")
        return
    
    print("\n--- ELIMINAZIONE ---")
    for i, partecipante in enumerate(partecipanti):
        print(f"{i}. {partecipante['nome_partecipante']} {partecipante['cognome_partecipante']}")

    print("Scegli il numero del aprtecipante da eliminare:: ")
    indice = richiedi_indice_valido(partecipanti)

    rimosso = partecipanti.pop(indice)

    print(f"🗑️  {rimosso['nome_partecipante']} {rimosso['cognome_partecipante']} Eliminato correttamente ")

    salva_dati(corsi, partecipanti)

def visualizza_partecipanti():
    print("\n--- LISTA PARTECIPANTI ---")
    if len(partecipanti) == 0:
        print("⚠️  Nessun partecipante iscritto.")
    else:
        for p in partecipanti:
            n_goleador = p.get('goleador', 0)
            corso = p.get('corso', 'N/A')
            print(f"👤 {p['nome_partecipante']} {p['cognome_partecipante']} | 📚 {corso} | 🍬 {n_goleador}")


# 2. La funzione "Operaia": aggiungi partecipanti
def aggiungi_partecipante():
    aggiungi_nome_partecipante = input("Scrivi di seguito il nome del partecipante: ")
    aggiungi_cognome_partecipante = input("Scrivi di seguito il cognome del partecipante: ")
    
    if len(corsi) == 0:
        print("Non puoi iscrivere nessuno se non crei prima un corso!")
        return

    for i, corso in enumerate(corsi):
        print(f"{i}. {corso['nome_corso']} {corso['numero_posti']}")        
    
    indice_corso = richiedi_indice_valido(corsi)

    # --- LOGICA DI ASSEGNAZIONE ---
    corso_selezionato = corsi[indice_corso]
    nome_corso_scelto = corso_selezionato['nome_corso']
    
# 2. Stampa di conferma
    print(f"\nHai selezionato il corso: {nome_corso_scelto}")

    # Creiamo il dizionario
    nuovo_partecipante = {
        "nome_partecipante": aggiungi_nome_partecipante,
        "cognome_partecipante": aggiungi_cognome_partecipante,
        "corso" : nome_corso_scelto
    }

    # Viene salvato nella lista globale
    partecipanti.append(nuovo_partecipante)
    print(f"👤 {nuovo_partecipante['nome_partecipante']} {nuovo_partecipante['cognome_partecipante']}")  

    salva_dati(corsi, partecipanti)


# 3. La funzione "Vigile": smista il traffico
def gestisci_partecipanti():
    scelta2 = input("Hai scelto i partecipanti - Premi 'v' per visualizzare, 'a' per aggiungere, 'e' per eliminare: ")
    
    if scelta2 == 'v':
        if len(partecipanti) == 0:
            print("⚠️  La lista dei partecipanti è vuota!")
            conferma = input("Vuoi aggiungere un nuovo partecipante ora? (s/n): ")
            if conferma == 's':
                aggiungi_partecipante()

        print("\n--- LISTA PARTECIPANTI & PUNTEGGI ---")
        # Ciclo for
        for partecipante in partecipanti:
            numero_goleador = partecipante.get('goleador', 0)
            nome_corso_scelto = partecipante.get('corso')
            print(f"👤 {partecipante['nome_partecipante']} {partecipante['cognome_partecipante']} | 📚 Corso: {nome_corso_scelto} | 🍬 Goleador: {numero_goleador}")  
    elif scelta2 == 'a':
        aggiungi_partecipante()

    elif scelta2 == 'e':
        rimuovi_partecipante()

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
    print(f"📚 Corso '{nuovo_corso['nome_corso']}' (Max {nuovo_corso['numero_posti']} posti) aggiunto correttamente.")
    
    salva_dati(corsi, partecipanti)

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
            print("--- Ecco la lista dei corsi ---")
        # Ciclo for
        for corso in corsi:
            print(f"📚 Nome: {corso['nome_corso']} - Posti: {corso['numero_posti']}")  
            
    elif scelta1 == 'a':
        aggiungi_corso()

def visualizza_corsi():
    print("\n--- LISTA CORSI ---")
    if len(corsi) == 0:
        print("⚠️  Nessun corso presente. (Usa l'opzione 'b' per aggiungerne uno)")
    else:
        for i, corso in enumerate(corsi):
            print(f"{i}. 📚 Nome: {corso['nome_corso']} - Posti: {corso['numero_posti']}")

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
        print("\n--- GESTIONE CORSI ---")
        print("a. Visualizza Corsi")
        print("b. Aggiungi Corso")
        print("c. Torna al menu principale")
        
        sub_scelta = input("Cosa vuoi fare? ").lower() # .lower() gestisce anche se scrivono 'A'
        
        if sub_scelta == 'a':
            visualizza_corsi()
        elif sub_scelta == 'b':
            aggiungi_corso()
        elif sub_scelta == 'c':
            pass # Torna al menu principale
        else:
            print("Scelta non valida!")

    elif scelta == "2":
        print("\n--- GESTIONE PARTECIPANTI ---")
        print("a. Visualizza Partecipanti")
        print("b. Iscrivi nuovo Partecipante")
        print("c. Rimuovi Partecipante")
        print("d. Torna al menu principale")
        
        sub_scelta = input("Cosa vuoi fare? ").lower()
        
        if sub_scelta == 'a':
            visualizza_partecipanti()
        elif sub_scelta == 'b':
            aggiungi_partecipante()
        elif sub_scelta == 'c':
            rimuovi_partecipante()
        elif sub_scelta == 'd':
            pass
        else:
            print("Scelta non valida!")

    elif scelta == "3":
        print("\n--- GESTIONE PUNTEGGI ---")
        print("a. Assegna Goleador (+)")
        print("b. Rimuovi Goleador (-)")
        print("c. Torna nel menu principale")
        sub_scelta = input("Scegli: ")

        if sub_scelta == 'a':
            assegna_goleador()
        elif sub_scelta == 'b':
            rimuovere_goleador()
        elif sub_scelta == 'c':
            pass

    elif scelta == "4":
        print("Hai scelto le Analytics & Statistiche")
        
    else:
        print("Inserisci un numero dall'elenco")