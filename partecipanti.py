from repository import salva_dati
from utils import richiedi_indice_valido


def rimuovi_partecipante(partecipanti, corsi):
    if len(partecipanti) == 0:
        print("Non ci sono partecipanti da eliminare")
        return
    
    print("\n--- ELIMINAZIONE ---")
    for i, p in enumerate(partecipanti):
        nome = p.get('nome_partecipante', 'SCONOSCIUTO')
        cognome = p.get('cognome_partecipante', '')
        print(f"{i + 1}. {nome} {cognome}")

    print("Scegli il numero del partecipante da eliminare: ")
    indice = richiedi_indice_valido(partecipanti)

    rimosso = partecipanti.pop(indice)

    nome_rimosso = rimosso.get('nome_partecipante', 'SCONOSCIUTO')
    print(f"🗑️ {nome_rimosso} Eliminato correttamente ")

    salva_dati(corsi, partecipanti)

def visualizza_partecipanti(partecipanti):
    print("\n--- LISTA PARTECIPANTI ---")
    if len(partecipanti) == 0:
        print("⚠️  Nessun partecipante iscritto.")
    else:
        for p in partecipanti:
            n_goleador = p.get('goleador', 0)
            corso = p.get('corso', 'N/A')
            nome = p.get('nome_partecipante', 'SCONOSCIUTO')
            cognome = p.get('cognome_partecipante', '')

            print(f"👤 {nome} {cognome} | 📚 {corso} | 🍬 {n_goleador}")


# 2. La funzione "Operaia": aggiungi partecipanti
def aggiungi_partecipante(partecipanti, corsi):
    if len(corsi) == 0:
        print("⚠️ Non puoi iscrivere nessuno se non crei prima un corso!")
        return
    
    print("\n--- SELEZIONE CORSO ---")
    
    for i, corso in enumerate(corsi):
        # Mostriamo anche i posti disponibili per comodità visiva
        print(f"{i + 1}. {corso['nome_corso']} (Max posti: {corso['numero_posti']})")        
    
    indice_corso = richiedi_indice_valido(corsi)

    # --- LOGICA DI ASSEGNAZIONE ---
    corso_selezionato = corsi[indice_corso]
    nome_corso_scelto = corso_selezionato['nome_corso']

    # 1. Convertiamo il numero di posti da stringa a intero
    posti_max = int(corso_selezionato['numero_posti'])

    # 2. Contiamo quanti sono GIÀ iscritti a questo corso
    iscritti_attuali = 0
    for p in partecipanti:
        if p.get('corso') == nome_corso_scelto:
            iscritti_attuali += 1

    # 3. Il Controllo del Buttafuori
    if iscritti_attuali >= posti_max:
        print(f"\n⛔ STOP! Il corso '{nome_corso_scelto}' è PIENO ({iscritti_attuali}/{posti_max}).")
        print("Scegli un altro corso.")
        return
    
    # Se siamo qui, c'è posto! Procediamo...
    print(f"\n✅ C'è posto ({iscritti_attuali}/{posti_max}). Procediamo con l'iscrizione.")

    aggiungi_nome_partecipante = input("Scrivi di seguito il nome del partecipante: ")
    aggiungi_cognome_partecipante = input("Scrivi di seguito il cognome del partecipante: ")

    # Creiamo il dizionario
    nuovo_partecipante = {
        "nome_partecipante": aggiungi_nome_partecipante,
        "cognome_partecipante": aggiungi_cognome_partecipante,
        "corso" : nome_corso_scelto,
        "goleador" : 0,
        "storico" : []
    }

    # Viene salvato nella lista globale
    partecipanti.append(nuovo_partecipante)
    print(f"🎉 Iscritto! 👤 {nuovo_partecipante['nome_partecipante']} {nuovo_partecipante['cognome_partecipante']} è ora nel corso: {nome_corso_scelto}.")  

    salva_dati(corsi, partecipanti)


def sposta_partecipante(partecipanti, corsi):
    print("\n--- SPOSTA PARTECIPANTE ---")
    if len(partecipanti) == 0:
        print("Nessun partecipante iscritto")
        return
    if len(corsi) < 2:
        print("Serve almeno un altro corso per fare un trasferimento!")
        return

    print("Chi vuoi spostare?")
    for i, p in enumerate(partecipanti):
        nome = p.get('nome_partecipante', 'SCONOSCIUTO')
        cognome = p.get('cognome_partecipante', '')
        corso_attuale = p.get('corso', 'Nessun Corso')

        print(f"{i + 1}. {nome} {cognome} (Attuale: {corso_attuale})")

    idx_studente = richiedi_indice_valido(partecipanti)
    studente = partecipanti[idx_studente]

    if 'nome_partecipante' not in studente:
        print("⚠️ Attenzione: stai spostando un partecipante con dati corrotti!")


    print(f"\nDove vuoi trasferire {studente.get('nome_partecipante', 'questo studente')}?")
    for i, c in enumerate(corsi):
        print(f"{i + 1}. {c['nome_corso']} (Max: {c['numero_posti']})")

    idx_corso = richiedi_indice_valido(corsi)
    corso_destinazione = corsi[idx_corso]
    nome_nuovo_corso = corso_destinazione['nome_corso']

    posti_max = int(corso_destinazione['numero_posti'])

    iscritti_destinazione = 0
    for p in partecipanti:
        if p.get('corso') == nome_nuovo_corso:
            iscritti_destinazione += 1

        if iscritti_destinazione >= posti_max:
            print(f"\n⛔ IMPOSSIBILE: Il corso '{nome_nuovo_corso}' è PIENO ({iscritti_destinazione}/{posti_max}).")
            print("Trasferimento annullato.")
            return
        
        # 3. Eseguiamo il trasferimento
        vecchio_corso = studente['corso']
        studente['corso'] = nome_nuovo_corso

        # Se lo studente era corrotto, potremmo cogliere l'occasione per "ripararlo" o lasciarlo così
        nome_stampa = studente.get('nome_partecipante', 'Utente Anonimo')

        print(f"\n✅ Fatto! {nome_stampa} è passato da '{vecchio_corso}' a '{nome_nuovo_corso}'.")
        salva_dati(partecipanti, corsi)