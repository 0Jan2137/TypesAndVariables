# A program for printing detailed information.

employee = "Mr. John May, born on 1998-02-16"

name = employee[4:8]          # "John"
surname = employee[9:12]      # "May"
born = employee[22:32]        # "1998-02-16"
initials = name[0] + surname[0]

print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {born}')
print(f'Initials: {initials}')


#użycie slice do pobrania imienia
#slice do pobrania nazwiska
#wycięcie daty urodzenia
#inicjały: pierwsza litera imienia + nazwiska