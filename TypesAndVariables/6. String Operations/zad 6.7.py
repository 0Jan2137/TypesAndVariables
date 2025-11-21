# A program that prints a numerical representation of each letter of your name.

name = 'Kacper'   # replace with your name if needed

for letter in name:
    print(f'The letter {letter} has a code {ord(letter)}')


#pętla przechodzi po każdej literze w imieniu
#ord(letter) pobiera kod znakowy
#wypisywanie litera → kod