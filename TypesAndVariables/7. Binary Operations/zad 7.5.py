car_number = input('Enter car registration number: ')
is_krakow = (car_number[:2] == 'KR') or (car_number[:2] == 'KK')
print(f'Car is from Krakow: {is_krakow}')



#pobranie numeru rejestracji
#sprawdzenie pierwszych 2 znaków
#porównanie z "KR" lub "KK"
#wypisanie True/False