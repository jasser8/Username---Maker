#LO USERNAME: nome dell'utente di un servizio Web

#Variabile cognome, tipo di dato: stringa quindi uso la class str,
#acquisico dati dalla tastiera
cognome = str(input("Cognome: "))

#Variabile nome...
nome = str(input("Nome: "))

#Variabile data di nascita...
datadinascita = str(input("Data di nascita (gg/mm/aaaa): "))

#costruzione dello username
username = cognome[0:3] + nome[0:3] + datadinascita[-2:]
username = username.lower()

#output dei dati
print("Il tuo username è:",username)

#istruzione fittizia di input
tasto = input()

