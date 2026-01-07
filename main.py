from repository import carica_dati
from menus import menu_corsi, menu_partecipanti, menu_goleador, menu_statistiche

# ===================================
# MAIN
# ===================================

corsi, partecipanti = carica_dati()
programma_attivo = True

while programma_attivo == True:
    print("\n" + "="*30)
    print("   🍬 GOLEADOR ACADEMY 🍬")
    print("="*30)

    print("1. Gestisci corsi")
    print("2. Gestisci Partecipanti")
    print("3. Assegnazione Goleador")
    print("4. Analytics & Statistiche")
    print("0. Exit")

    scelta = input("Inserisci un'opzione: ")

    if scelta == "1":
        menu_corsi(corsi, partecipanti)

    elif scelta == "2":
        menu_partecipanti(corsi, partecipanti)        

    elif scelta == "3":
        menu_goleador(corsi, partecipanti)

    elif scelta == "4":
        menu_statistiche(corsi, partecipanti)

    elif scelta == "0":
        print("\n👋 Arrivederci! Dati salvati.")
        programma_attivo = False

    else:
        print("Inserisci un numero dall'elenco")
