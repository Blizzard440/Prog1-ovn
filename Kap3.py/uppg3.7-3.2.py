import math 

svar = input('Vad är cirkelns radie: ')

radie = float(svar)
area = radie*radie*math.pi
omkrets = (radie+radie)*math.pi

if svar == '0':
    print('Cirkeln är för liten att beräkna i detta program')

else:
    print(f'Arean på cirkeln är: {area:.3f}')
    print(f'Omkretsen på cirkeln är: {omkrets:.3f}')

radie = float(svar)
area = radie*radie*math.pi
omkrets = (radie+radie)*math.pi
