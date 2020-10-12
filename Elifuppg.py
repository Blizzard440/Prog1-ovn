print('Välj mellan:\n\t05,50\n\t06,00\n\t06,10')
alarm = input('väckaren ringer, vad säger den? ').lower()

if alarm == '05,50':
    valett = input('Vad vill du göra? [snooza/stiga upp]')
    if valett == 'snooza':
        print('snoozar')
        valtvå = input('Väckaren ringer igen 06,00, vad gör du? [snooza/stiga upp?]')
        if valtvå == 'snooza':
            print ('snoozar')
        elif valtvå == 'stiga upp':
            print('Dags att stiga upp')
        
        
    elif valett == 'stiga upp':
        print('Dags att stiga upp')
    
    
elif alarm == '06,00':
    print('snooza')

elif alarm == '06,10':
    print('dags att stiga upp')

else:
    print('Nu blir det brottom!')

print('Välj mellan:\n\t06,10\n\t06,15\n\t06,20')
frukost = input('vad är klockan? ')

if frukost == '06,10':
    print('DU har gott om tid att äta frukost')

elif frukost == '06,15':
    print('Du har tid att äta frukost')

elif frukost == '06,20':
    print('Du får skynda dig i med maten')

else:
    print('Idag får du svälta)')

print('Välj mellan:\n\t06,15\n\t06,20\n\t06,25')
tandborstning = input('Vad är klockan nu? ')

if tandborstning == '06,15':
    print('Du har god tid på dig att borsta tänderna så borsta noga.')

elif tandborstning == '06,20':
    print('Du hinner borsta tänderna')

elif tandborstning == '06,25':
    print('Du får fuskborsta idag')

else:
    print('Du får skita i tanborstning idag!')
