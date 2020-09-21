svar = input('Antal sekunder: ') #läser in antalet sekunder
sek = int(svar) #konverterar svaret till ett heltal
print('Inmatning:', sek) 
vecka = sek // 604800 #Delar analet sekunder med sekunder på en vecka, kapar till heltal med //
sek = sek % 604800 #Räknar ut antalet sekunder som inte blir en hel vecka men hjälp av %
print('Rest från veckor: ', sek)
dag = sek // 86400 #Delar analet sekunder med sekunder på en dag, kapar till heltal med //
sek = sek % 86400 #Räknar ut antalet sekunder som inte blir en hel dag men hjälp av %
print('Rest från dagar: ', sek)
tim = sek // 3600 #Delar analet sekunder med sekunder på en timme, kapar till heltal med //
sek = sek % 3600 #Räknar ut antalet sekunder som inte blir en hel timme men hjälp av %
print('Rest från timmar:', sek) 
min = sek // 60 #Delar antalet sekunder med sekunder på en minut, kaper till heltal med //
sek = sek % 60 #Räknar ut antalet sekunder som inte blir en hel minut med hjälp av %
print('Rest från minuter:', sek)

print('Veckor: ', vecka)
print('Dagar: ', dag)
print('Timmar: ', tim)
print('Minuter: ', min)
print('Sekunder: ', sek)
