svar=input('skriv ett tal: ')
x=float(svar)
y=x*x
print(f'talet i kvadrat är{y:.5f}')

i=19
j=107
k=40
print(f'resultat:{i}') #Betyder att bara 1 skrivs
print(f'resultat:{j:5}') # Betyder 5 digits med 2 blanka i början
print(f'resultat:{k:05}') #Betyder totalt 5 digits med nollor
