milnu=input('Mätarställning idag? ') #ställer fråga
milinnan=input('Mätarställning för et år sedan? ') #ställer fråga
literiår=input('Hur många liter har gått åt i år? ') #ställer fråga

milnu = int(milnu) #bestämmer att milnu är en int variabel
milinnan = int(milinnan) #bestämmer att milinnan är en int variabel
körtiår = milnu-milinnan #räknar ut antal körda mil i år genom att subtrahera antalet mil innan från antalet mil på mätaren nu
literiår = float(literiår) #bestämmer att literiår är en float variabel
literpermil = literiår/körtiår #bestämmer att literpermil är en variabel som literiår delat i körtiår
n = int(0)

if literiår == 0:
    print(f'Antal mil körda i år: {n:.1}')
    print(f'Bilen har dragit {literpermil:.3f} per mil i år.')

else:
    print(f'Antal mil körda i år: {körtiår:.0f}')
    print(f'Bilen har dragit {literpermil:.3f} per mil i år.')
 