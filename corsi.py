from repository import salva_dati

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

def visualizza_corsi(corsi):
    print("\n--- LISTA CORSI ---")
    if len(corsi) == 0:
        print("⚠️  Nessun corso presente. (Usa l'opzione 'b' per aggiungerne uno)")
    else:
        for i, corso in enumerate(corsi):
            print(f"{i}. 📚 Nome: {corso['nome_corso']} - Posti: {corso['numero_posti']}")