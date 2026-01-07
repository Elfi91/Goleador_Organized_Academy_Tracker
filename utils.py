def richiedi_indice_valido(lista_riferimento):
    while True:
        try:
            valore_utente = int(input("Inserisci il numero corrispondente: "))

            indice_reale = valore_utente - 1
            
            # Controlliamo se il numero è dentro i limiti della lista
            if 0 <= indice_reale < len(lista_riferimento):
                return indice_reale # È valido! Usciamo e restituiamo il numero
            else:
                max_numero = len(lista_riferimento) - 1
                print(f"⚠️ Errore: Inserisci un numero tra 1 e {max_numero}.")
                
        except ValueError:
            # Succede se l'utente scrive lettere invece di numeri
            print("⚠️ Errore: Devi inserire un numero intero!")
