import random

dice = random.randint(1, 6)
special = (dice == 1) or (dice == 6)

print(f'Dice rolled: {dice}')
print(f'Special number (1 or 6): {special}')



#losowanie liczby 1–6
#sprawdzenie czy wynik to 1 lub 6
#wypisanie rzutu i True/False