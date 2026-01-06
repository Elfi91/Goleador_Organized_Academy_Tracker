def richiedi_indice_valido(lista_riferimento):
    while True:
        try:
            valore = int(input("Inserisci il numero corrispondente: "))
            
            # Controlliamo se il numero è dentro i limiti della lista
            if 0 <= valore < len(lista_riferimento):
                return valore # È valido! Usciamo e restituiamo il numero
            else:
                max_indice = len(lista_riferimento) - 1
                if max_indice == 0:
                    print(f"⚠️ Errore: C'è solo un'opzione (0). Inserisci 0.")
                else:
                    print(f"⚠️ Errore: Inserisci un numero tra 0 e {max_indice}.")
                
        except ValueError:
            # Succede se l'utente scrive lettere invece di numeri
            print("⚠️ Errore: Devi inserire un numero intero, non parole!")
