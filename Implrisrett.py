nome = 'Emanuele'
codicePersonale = 2003
autenticazione = input("inserire codice personale: ")
if autenticazione == 2003:
	print ("Accesso efettuato con successo!")
else: 
	print("Per quale motivo vuoi enttare nel mio account!? ")
	print("Accesso negato!")

b = input("inserisci la base: ")
h = input("inserisci l'altezza: ")

if b == 0:
	print("base = 0")
	
if h == 0:
	print("altezza = 0")
	
area = b*h
perimetro = b*2+h*2

print ("area: ") 
print area

 
print ("perimetro: ") 
print perimetro
	
