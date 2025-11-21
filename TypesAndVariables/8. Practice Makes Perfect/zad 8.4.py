# A program that prints your height both in cm and in feet and inches.

cm = 170

# calculate the number of feet
feet = cm // 30.48

# calculate the number of inches (remainder → cm left after removing feet)
inches = (cm % 30.48) / 2.54

print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {round(inches)} inches')



#// → całkowita liczba stóp
#% → pozostałe cm
#zamiana reszty cm na cale
#wypisanie stóp i cali