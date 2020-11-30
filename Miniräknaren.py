main = 0

while main != 4:
    print('(1) för +')
    print('(2) för -')
    print('(3) för *')
    print('(4) för att avsluta')
    
    main = int(input('Välj räknesätt: '))

    if main == 1:
        print('Räkna med addtition')
        tal1 = float(input('Tal 1: '))
        tal2 = float(input('Tal 2: '))
        summa = tal1 + tal2
        print(f'summan av {tal1} och {tal2} är {summa} ')

    elif main == 2:
        print('Räkna med subtraktion')
        tal1 = float(input('Tal1: '))
        tal2 = float(input('Tal2: '))
        differens = tal1 - tal2
        print(f'differensen mellan {tal1} och{tal2} är {differens}')

    elif main == 3:
        print('Räkna med multiplikation')
        tal1 = float(input('Tal1: '))
        tal2 = float(input('Tal2: '))
        summa = tal1 * tal2
        print(f'Summan av {tal2} * {tal2} är {summa}')
    
    else:
        print ('Trevligt att stå till tjänst')
