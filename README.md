# 🏆 Goleador Academy Tracker

Benvenuti nel sistema gestionale della **Goleador Academy**!
Questa è un'applicazione CLI (Command Line Interface) scritta in Python per gestire corsi, studenti e un sistema di ricompense "gamificato" basato sulle caramelle Goleador.

## ✨ Funzionalità Principali

* **Gestione Corsi:** Crea nuovi corsi, imposta il numero massimo di posti e visualizza l'occupazione in tempo reale (es. 2/5 posti).
* **Gestione Studenti:** Iscrizione studenti con controllo "Buttafuori" (non puoi iscrivere se il corso è pieno), rimozione e trasferimento tra corsi.
* **Gamification:** Assegna o rimuovi Goleador agli studenti per premiare l'impegno.
* **Storico:** Ogni assegnazione viene salvata con data e ora.
* **Statistiche & Analytics:** Classifiche globali, classifiche per corso e individuazione automatica dei Top Scorer.
* **🤖 AI Coach Integrato:** Integrazione con **Google Gemini** per analizzare i dati della classe e generare commenti motivazionali personalizzati.
* **Persistenza Dati:** Tutti i dati sono salvati automaticamente su un file `dati.json`.

## 🛠️ Installazione e Requisiti

Assicurati di avere Python installato.

1.  **Clona o scarica** questa cartella.
2.  **Crea un ambiente virtuale** (opzionale ma consigliato):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Mac/Linux
    venv\Scripts\activate     # Su Windows
    ```
3.  **Installa le librerie necessarie:**
    ```bash
    pip install google-generativeai python-dotenv
    ```
4.  **Configura la Chiave API:**
    * Crea un file chiamato `.env` nella cartella principale.
    * Inserisci la tua chiave di Google Gemini:
        ```env
        GEMINI_KEY="Incolla_Qui_La_Tua_Chiave"
        ```


## 📂 Struttura del Progetto

* **main.py** Il punto di ingresso. Gestisce il ciclo principale del programma.
* **menus.py** Contiene l'interfaccia utente dei sotto-menu.
* **repository.py** Gestisce lettura e scrittura sul database dati.json.
* **corsi.py / partecipanti.py** Logica di gestione (CRUD).
* **goleador.py** Logica di assegnazione punti e storico.
* **ai_coach.py** Modulo di connessione all'Intelligenza Artificiale.
* **utils.py** Funzioni di utilità (es. input validati).
* **ripara_dati.py** Script di emergenza per pulire il database da dati corrotti.

## 🛡️ Note Tecniche

* Il sistema utilizza un controllo "Buttafuori" per impedire l'overbooking dei corsi.
* L'interfaccia utilizza indici Human-Friendly (parte da 1) convertiti internamente per liste 0-based.
* Gestione errori robusta tramite blocchi try-except.