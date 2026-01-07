from utils import richiedi_indice_valido
from datetime import datetime
from repository import salva_dati

def rimuovi_goleador(partecipanti, corsi):
    if len(partecipanti) == 0:
        print("⚠️ Non ci sono partecipanti.")
        return

    print("\n--- RIMUOVI GOLEADOR ➖🍬 ---")

    for i, p in enumerate(partecipanti):
        goleador_attuali = p.get('goleador', 0)
        print(f"{i + 1}. {p['nome_partecipante']} {p['cognome_partecipante']} (Attuali: {goleador_attuali})")

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

    adesso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    movimento = {
        "data" : adesso,
        "quantita" : -da_rimuovere
        }
    if "storico" not in partecipante:
        partecipante["storico"] = []

    partecipante["storico"].append(movimento)
    
    print(f"✅Fatto. Ora 👤 {partecipante['nome_partecipante']} ha 🍬 {nuovo_totale}")
    salva_dati(corsi, partecipanti)

def assegna_goleador(partecipanti, corsi):
# --- CONTROLLO INIZIALE ---
    if len(corsi) == 0 or len(partecipanti) == 0:
        print("⚠️ Attenzione: mancano corsi o partecipanti!")
        print("Aggiungili dal menu principale prima di fare assegnazioni.")
        return # Questo comando fa uscire subito dalla funzione
    
# --- SELEZIONE PARTECIPANTE ---
    print("Seleziona un partecipante:")
    for i, partecipante in enumerate(partecipanti):
        print(f"{i + 1}. {partecipante['nome_partecipante']} {partecipante['cognome_partecipante']}")
    
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

    adesso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    movimento = {
        "data" : adesso,
        "quantita" : quantita
    }

    if "storico" not in partecipante_selezionato:
        partecipante_selezionato["storico"] = []

    partecipante_selezionato["storico"].append(movimento)

    partecipante_selezionato['goleador'] = nuovo_totale

    salva_dati(corsi, partecipanti) 
    print(f"✅Fatto, Ora {partecipante_selezionato['nome_partecipante']} ne ha {nuovo_totale}")