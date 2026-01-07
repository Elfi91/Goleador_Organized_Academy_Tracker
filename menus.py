from corsi import visualizza_corsi, aggiungi_corso, modifica_corso
from partecipanti import visualizza_partecipanti, aggiungi_partecipante, rimuovi_partecipante, sposta_partecipante
from goleador import assegna_goleador, rimuovi_goleador
from statistiche import classifica_goleador, classifica_per_corso, top_scorer_per_corso
from ai_coach import chiedi_al_coach

def menu_corsi(corsi, partecipanti):
    print("\n--- GESTIONE CORSI ---")
    print("a. Visualizza Corsi")
    print("b. Aggiungi Corso")
    print("c. Modifica Corso")
    print("x. Torna al menu principale")
    
    sub_scelta = input("Cosa vuoi fare? ").lower() 
    
    if sub_scelta == 'a':
        visualizza_corsi(corsi, partecipanti)
    elif sub_scelta == 'b':
        aggiungi_corso(partecipanti, corsi)
    elif sub_scelta == 'c':
        modifica_corso(partecipanti, corsi)
    elif sub_scelta == 'x':
        return
    else:
        print("Scelta non valida!")

def menu_partecipanti(corsi, partecipanti):
    print("\n--- GESTIONE PARTECIPANTI ---")
    print("a. Visualizza Partecipanti")
    print("b. Iscrivi nuovo Partecipante")
    print("c. Rimuovi Partecipante")
    print("d. Sposta partecipante (Cambia corso)")
    print("x. Torna al menu principale")
        
    sub_scelta = input("Cosa vuoi fare? ").lower()
        
    if sub_scelta == 'a':
        visualizza_partecipanti(partecipanti)
    elif sub_scelta == 'b':
        aggiungi_partecipante(partecipanti, corsi)
    elif sub_scelta == 'c':
        rimuovi_partecipante(partecipanti, corsi)
    elif sub_scelta == 'd':
        sposta_partecipante(partecipanti, corsi)
    elif sub_scelta == 'x':
        return
    else:
        print("Scelta non valida!") 

def menu_goleador(corsi, partecipanti):
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
        return

def menu_statistiche(corsi, partecipanti):
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
        return
        