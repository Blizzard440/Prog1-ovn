lön = 0.01
ggr = 0
dag = 1
tot = 0

print ('dag 0 har man 0 kr')

while tot < 10000000:
    print(f'dag {dag:.0f} har man totalt fått {lön:.2f} kr')
    tot = tot + lön
    lön = lön + lön
    ggr = ggr + 1
    dag = dag + 1
    print (f'Totalt tjänat {tot:.2f} kr')

print(f'{ggr} dagar till {tot} kr sparade pengar')
