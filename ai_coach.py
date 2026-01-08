import google.genai as genai
from dotenv import load_dotenv
import os

cartella_corrente = os.path.dirname(os.path.abspath(__file__))
percorso_env = os.path.join(cartella_corrente, '.env')
load_dotenv(percorso_env)

load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")

def chiedi_al_coach(partecipanti):
    print("\n🤖 Sto chiamando il Coach AI... (Attendi qualche secondo)")

    # 1. Controllo di sicurezza
    if not API_KEY or API_KEY.startswith("INSERISCI") or len(API_KEY) < 10:
        print("❌ ERRORE: Chiave API mancante, non valida o file .env non trovato.")
        return
    
    try:
        genai.configure(api_key=API_KEY)
        
        # Usiamo questo alias che è apparso nella tua lista dei disponibili
        model = genai.GenerativeModel('gemini-flash-latest') 
        
        # 2. Controllo Dati (Se la classe è vuota, inutile chiamare l'AI)
        if not partecipanti:
            print("⚠️ Non ci sono ancora partecipanti su cui fare statistiche!")
            return

        # 3. Calcolo dell'andamento
        totale_goleador = sum(p.get('goleador', 0) for p in partecipanti)
        
        # Troviamo il Top Scorer
        top_player = max(partecipanti, key=lambda x: x.get('goleador', 0))
        nome_top = f"{top_player['nome_partecipante']} {top_player['cognome_partecipante']}"
        punti_top = top_player.get('goleador', 0)

        # 4. Prompt (Istruzioni per l'AI)
        # Qui spieghiamo il contesto "Goleador Academy"
        prompt = (
            f"Sei il Coach Motivazionale della 'Goleador Academy'. "
            f"Analizza questi dati della classe:\n"
            f"- Totale Goleador (punti) distribuiti: {totale_goleador}\n"
            f"- Numero studenti: {len(partecipanti)}\n"
            f"- Attuale Primo della Classe: {nome_top} con {punti_top} punti.\n\n"
            f"SCRIVI UN COMMENTO BREVE (max 2 frasi):\n"
            f"1. Fai un complimento esagerato ed epico al primo in classifica.\n"
            f"2. Sprona il resto della classe a impegnarsi per raggiungerlo.\n"
            f"Usa un tono energico da allenatore sportivo."
        )

        # 5. Generazione
        response = model.generate_content(prompt)
        
        print("\n" + "="*20)
        print("📣 IL COACH DICE:")
        print(response.text.strip())
        print("="*20 + "\n")

    except Exception as e:
        print(f"\n⚠️ Errore di connessione col Coach.")
        print(f"Dettaglio tecnico: {e}")