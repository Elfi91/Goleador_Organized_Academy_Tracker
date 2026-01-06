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
        print("Non puoi iscrivere nessuno se non crei prima un corso!")
        return
    
    aggiungi_nome_partecipante = input("Scrivi di seguito il nome del partecipante: ")
    aggiungi_cognome_partecipante = input("Scrivi di seguito il cognome del partecipante: ")
    
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