import json
import os

def ripara_database():
    print("🧹 INIZIO PULIZIA DATABASE...")
    
    if not os.path.exists("dati.json"):
        print("❌ File dati.json non trovato!")
        return

    # 1. Carichiamo i dati sporchi
    with open("dati.json", "r", encoding="utf-8") as f:
        try:
            db = json.load(f)
        except json.JSONDecodeError:
            print("❌ Il file è danneggiato o vuoto.")
            return

    partecipanti = db.get("partecipanti", [])
    corsi = db.get("corsi", [])
    
    print(f"📊 Trovati {len(partecipanti)} partecipanti totali.")

    # 2. Filtriamo: teniamo SOLO quelli che hanno un nome valido
    partecipanti_sani = []
    fantasmi_rimossi = 0

    for p in partecipanti:
        # Controlliamo se esiste la chiave 'nome_partecipante' e se non è vuota
        if "nome_partecipante" in p and p["nome_partecipante"].strip() != "":
            partecipanti_sani.append(p)
        else:
            fantasmi_rimossi += 1
            print(f"   🗑️ Trovato e rimosso un utente corrotto (ID o Dati mancanti)")

    # 3. Salviamo i dati puliti
    db["partecipanti"] = partecipanti_sani
    
    with open("dati.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

    print("-" * 30)
    if fantasmi_rimossi > 0:
        print(f"✅ PULIZIA COMPLETATA! Rimossi {fantasmi_rimossi} utenti fantasma.")
    else:
        print("✅ Nessun utente corrotto trovato. Il database era già pulito.")
    print("Ora puoi riavviare main.py senza problemi!")

if __name__ == "__main__":
    ripara_database()