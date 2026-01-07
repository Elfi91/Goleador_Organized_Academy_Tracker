from repository import salva_dati
from utils import richiedi_indice_valido


def rimuovi_partecipante(partecipanti, corsi):
    if len(partecipanti) == 0:
        print("Non ci sono partecipanti da eliminare")
        return
    
    print("\n--- ELIMINAZIONE ---")
    for i, partecipante in enumerate(partecipanti):
        print(f"{i}. {partecipante['nome_partecipante']} {partecipante['cognome_partecipante']}")

    print("Scegli il numero del partecipante da eliminare: ")
    indice = richiedi_indice_valido(partecipanti)

    rimosso = partecipanti.pop(indice)

    print(f"🗑️  {rimosso['nome_partecipante']} {rimosso['cognome_partecipante']} Eliminato correttamente ")

    salva_dati(corsi, partecipanti)

def visualizza_partecipanti(partecipanti):
    print("\n--- LISTA PARTECIPANTI ---")
    if len(partecipanti) == 0:
        print("⚠️  Nessun partecipante iscritto.")
    else:
        for p in partecipanti:
            n_goleador = p.get('goleador', 0)
            corso = p.get('corso', 'N/A')
            print(f"👤 {p['nome_partecipante']} {p['cognome_partecipante']} | 📚 {corso} | 🍬 {n_goleador}")


# 2. La funzione "Operaia": aggiungi partecipanti
def aggiungi_partecipante(partecipanti, corsi):
    if len(corsi) == 0:
        print("⚠️ Non puoi iscrivere nessuno se non crei prima un corso!")
        return
    
    print("\n--- SELEZIONE CORSO ---")
    
    for i, corso in enumerate(corsi):
        # Mostriamo anche i posti disponibili per comodità visiva
        print(f"{i}. {corso['nome_corso']} (Max posti: {corso['numero_posti']})")        
    
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