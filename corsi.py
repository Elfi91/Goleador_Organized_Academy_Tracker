from repository import salva_dati
from utils import richiedi_indice_valido

def aggiungi_corso(partecipanti, corsi):
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

def visualizza_corsi(corsi, partecipanti):
    print("\n--- LISTA CORSI ---")
    if len(corsi) == 0:
        print("⚠️  Nessun corso presente. (Usa l'opzione 'b' per aggiungerne uno)")
    else:
        for i, corso in enumerate(corsi):
            nome_corso = corso['nome_corso']
            posti_max = corso['numero_posti']

            iscritti_attuali = 0 
            for p in partecipanti:
                if p.get('corso') == nome_corso:
                    iscritti_attuali += 1

            print(f"{i + 1}. 📚 Nome: {nome_corso} - Posti: {iscritti_attuali}/{posti_max}")


def modifica_corso(partecipanti, corsi):
    print("\n--- MODIFICA CORSO ---")
    if len(corsi) == 0:
        print("Non ci sono corsi da modifciare")
        return
    
    # 1. Scegli il corso
    for i, corso in enumerate(corsi):
        print(f"{i + 1}. {corso['nome_corso']} (Max: {corso['numero_posti']})")

    indice = richiedi_indice_valido(corsi)
    corso_da_modificare = corsi[indice]

    vecchio_nome = corso_da_modificare['nome_corso']
    vecchi_posti = corso_da_modificare['numero_posti']

    print(f"\nStai modificando: {vecchio_nome}")
    print("Lascia vuoto o premi Invio se non vuoi cambiare il campo")

    # 2. Richiedi nuovi dati (Gestione input vuoto)
    nuovo_nome = input(f"Nuovo nome (attuale: {vecchio_nome}): ").strip()
    nuovi_posti = input(f"Nuovi posti Max (attuale: {vecchi_posti}): ").strip()

    # 3. Aggiorniamo solo se l'utente ha scritto qualcosa
    if nuovo_nome != "":
        corso_da_modificare['nome_corso'] = nuovo_nome

        # Se cambio nome al corso, devo cambiare il nome nel cartellino degli studenti!
        contatore_partecipanti_aggiornati = 0
        for p in partecipanti:
            if p.get('corso') == vecchio_nome:
                p['corso'] = nuovo_nome
                contatore_partecipanti_aggiornati += 1

        print(f"🔄 Ho aggiornato anche il corso a {contatore_partecipanti_aggiornati} studenti.")

    if nuovi_posti != "":
        if nuovi_posti.isdigit():
            corso_da_modificare['numero_posti'] = nuovi_posti
        else:
            print("⚠️ Attenzione: I posti devono essere un numero. Modifica posti annullata.")

    print("✅ Modifiche salvate")
    salva_dati(corsi, partecipanti)