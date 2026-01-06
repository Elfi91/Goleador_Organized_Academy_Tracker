from utils import richiedi_indice_valido

def classifica_goleador(partecipanti):
    print("\n--- CLASSIFICA ---")

    classifica = partecipanti[:]
    classifica.sort(key=lambda p: p.get('goleador', 0), reverse=True)

    for i, p in enumerate(classifica):
        print(f"{i}. 🍬 {p.get('goleador', 0)} 👤 {p['nome_partecipante']} {p['cognome_partecipante']}  📚 {p['corso']} ")

def classifica_per_corso(partecipanti, corsi):
    print("\n--- CLASSIFICA PER CORSO ---")

    if len(corsi) == 0:
        print("Non ci sono corsi.")
        return
    
    for i, c in enumerate(corsi):
        print(f"{i}. {c['nome_corso']}")

    indice = richiedi_indice_valido(corsi)
    corso_scelto = corsi[indice]
    nome_del_corso = corso_scelto['nome_corso']

    studenti_del_corso = []
    totale_goleador_corso = 0

    for p in partecipanti:
        # 1. IL CONTROLLO:
        # Se il corso dello studente (p['...']) è uguale (==) al nome_del_corso:
        if p.get('corso') == nome_del_corso:
            studenti_del_corso.append(p)

            # 3. LA SOMMA AL TOTALE:
            # Aggiungi al totale le goleador di questo studente (usa .get per sicurezza!)
            goleador_studente = p.get('goleador', 0)
            totale_goleador_corso += goleador_studente

    studenti_del_corso.sort(key=lambda p: p.get('goleador', 0), reverse=True)

    print(f"\nClassifica per: {nome_del_corso}")

    for i, p in enumerate(studenti_del_corso):
        print(f"{i+1}. {p['nome_partecipante']} (🍬 {p.get('goleador', 0)})")

    print(f"\n💰 TOTALE GOLEADOR DISTRIBUITE NEL CORSO: {totale_goleador_corso}")


def top_scorer_per_corso(partecipanti, corsi):
    print("\n--- 🏆 TOP SCORER PER OGNI CORSO ---")

    if len(corsi) == 0:
        print("Non ci sono corsi registrati.")
        return

    # 1. Analizziamo un corso alla volta
    for c in corsi:
        nome_corso_corrente = c['nome_corso']
        
        # Prepariamo una lista vuota SOLO per gli studenti di questo corso specifico
        studenti_del_corso = []

        for p in partecipanti:
            if p.get('corso') == nome_corso_corrente:
                studenti_del_corso.append(p)
        
        if len(studenti_del_corso) == 0:
            print(f"📚 {nome_corso_corrente}: Nessun iscritto.")
        else:
            # Ordiniamo dal più grande al più piccolo
            studenti_del_corso.sort(key=lambda p: p.get('goleador', 0), reverse=True)
            
            # Il primo della lista è il campione
            campione = studenti_del_corso[0] 
            
            # 3. STAMPA FINALE (Come hai chiesto: Corso, Nome, Cognome, Goleador)
            print(f"📚 {nome_corso_corrente} | 🥇 {campione['nome_partecipante']} {campione['cognome_partecipante']} | 🍬 {campione.get('goleador', 0)}")
