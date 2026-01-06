"GEMINI GEM = https://gemini.google.com/gem/1HOZjA5ibxeSk-AKGGa0ToZyXxjtzD-zh?usp=sharing"

from repository import carica_dati
from corsi import visualizza_corsi, aggiungi_corso
from partecipanti import visualizza_partecipanti, aggiungi_partecipante, rimuovi_partecipante
from goleador import assegna_goleador, rimuovi_goleador
from statistiche import classifica_goleador, classifica_per_corso, top_scorer_per_corso
from ai_coach import chiedi_al_coach

# ===================================
# MAIN
# ===================================

corsi, partecipanti = carica_dati()

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
        print("x. Torna al menu principale")
        
        sub_scelta = input("Cosa vuoi fare? ").lower() 
        
        if sub_scelta == 'a':
            visualizza_corsi(corsi)
        elif sub_scelta == 'b':
            aggiungi_corso(partecipanti, corsi)
        elif sub_scelta == 'x':
            pass
        else:
            print("Scelta non valida!")

    elif scelta == "2":
        print("\n--- GESTIONE PARTECIPANTI ---")
        print("a. Visualizza Partecipanti")
        print("b. Iscrivi nuovo Partecipante")
        print("c. Rimuovi Partecipante")
        print("x. Torna al menu principale")
        
        sub_scelta = input("Cosa vuoi fare? ").lower()
        
        if sub_scelta == 'a':
            visualizza_partecipanti(partecipanti)
        elif sub_scelta == 'b':
            aggiungi_partecipante(partecipanti, corsi)
        elif sub_scelta == 'c':
            rimuovi_partecipante(partecipanti, corsi)
        elif sub_scelta == 'x':
            pass
        else:
            print("Scelta non valida!")

    elif scelta == "3":
        print("\n--- GESTIONE PUNTEGGI ---")
        print("a. Assegna Goleador (+)")
        print("b. Rimuovi Goleador (-)")
        print("x. Torna nel menu principale")
        sub_scelta = input("Scegli: ").lower()

        if sub_scelta == 'a':
            assegna_goleador(partecipanti, corsi)
        elif sub_scelta == 'b':
            rimuovi_goleador(partecipanti, corsi)
        elif sub_scelta == 'x':
            pass

    elif scelta == "4":
        print("\n--- ANALYTICS & STATISTICHE ---")
        print("a. Classifica goleador")
        print("b. Classifica corso")
        print("c. Top scorer per ogni corso")
        print("d. 🤖 Chiedi al Coach AI (Gemini)")
        print("x. Torna al menu principale")
        sub_scelta = input("Scegli: ").lower()

        if sub_scelta == 'a':
            classifica_goleador(partecipanti)
        elif sub_scelta == 'b':
            classifica_per_corso(partecipanti, corsi)
        elif sub_scelta == 'c':
            top_scorer_per_corso(partecipanti, corsi)
        elif sub_scelta == 'd':
            chiedi_al_coach(partecipanti)
        elif sub_scelta == 'x':
            pass
        
    else:
        print("Inserisci un numero dall'elenco")
