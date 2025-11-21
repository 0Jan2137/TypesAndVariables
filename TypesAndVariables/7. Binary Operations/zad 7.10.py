import random

# COMPUTER TURN
computer = random.randint(1, 6)

# YOUR TURN
you = int(input('Guess the number (1-6): '))

won = (you == computer)

print(f'Computer rolled: {computer}')
print(f'You won: {won}')



#komputer losuje liczbę 1–6
#użytkownik wpisuje swoją liczbę
#porównanie obu wartości
#wypisanie wyniku True/False