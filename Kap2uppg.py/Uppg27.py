import math 

svar = input('Vad är cirkelns radie: ')
radie = float(svar)
area = radie*radie*math.pi
omkrets = (radie+radie)*math.pi
print(f'Arean på cirkeln är: {area:.3f}')
print(f'Omkretsen på cirkeln är: {omkrets:.3f}')