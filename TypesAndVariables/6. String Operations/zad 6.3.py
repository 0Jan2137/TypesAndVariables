# A program that prints a university abbreviation (universal version)

university = "Krakow University of Economics"

skip_words = {"of", "in", "on", "at", "and", "the"}   # words to ignore

words = university.split()

abbreviation = ""

for word in words:                 # clearer name instead of 'w'
    if word.lower() not in skip_words:
        abbreviation += word[0]

print(abbreviation)


#lista słów do pominięcia: "of", "in", "and", itp.
#podział nazwy na słowa .split()
#pętla po każdym słowie
#jeśli nie jest na liście → bierzemy pierwszą literę
#łączymy wszystkie litery → wypisujemy skrót