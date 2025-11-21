# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.

phone = input('Enter phone number: ')   # e.g. 543097329

part1 = phone[0:3]
part2 = phone[3:6]
part3 = phone[6:9]

print(f'Phone number: {part1}-{part2}-{part3}')

#pobranie numeru z input
#podzielenie na 3 grupy po 3 cyfry
#wypisanie w formacie XXX-XXX-XXX