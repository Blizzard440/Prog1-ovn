starthöjd = float(input('Hur högt släpps bollen från? '))

cm = starthöjd * 100
ggr = 0

while cm >= 1:
    cm = cm * 0.7
    ggr = ggr + 1
    print (f'{cm:.2f} cm')
print(f'bollen studsar {ggr} gånger')