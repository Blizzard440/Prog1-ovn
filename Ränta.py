#räkna räta på sparade pengar

balance = float(input('Ditt startkapital: '))
save = float(input('Jag vill spara i månaden: '))
year = int(input('Under hur många år: '))
interest = int(input('Ränta i %: '))
balancewithinterest = 0

for i in range(1, year):
    balance += save * 12
    balancewithinterest += save * 12
    balancewithinterest *= (interest / 100 + 1)
    print(f'År {i} har du sparat {balance:.1f} kronor, vilket är {balancewithinterest:.2f} med ränta')
