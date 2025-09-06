'''Kreirajte varijable user input te ispišite na ekran odgovarajuće vrijednosti, za:
    Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn po litri (nije važno kojeg goriva), 
    izračunajte koliko košta 1 km vožnje automobilom. 
    Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji je udaljen 20 km u jednom smjeru.
'''


# Varijable
print()
fuel_consumption = float(input('Kolika je potrosnja goriva na 100km ?: '))
fuel_price = float(input('Kolika je cijena goriva ?: ')) #EURO
one_way_distance = int(input('Kolika je dnevna kilometraza u jednom smjeru?: '))
days_in_month = int(input('Koliko je dana u mjesecu ?: '))

# Izracuni
daily_distance = one_way_distance * 2
one_km_cost = fuel_consumption * fuel_price / 100
daily_fuel_price = daily_distance * one_km_cost 
monthly_price = one_km_cost * daily_distance * days_in_month

# Ispis
print()
print(f'Cijena jednog kilometra je: {one_km_cost: .2f}€')
print(f'Dnevni trosak na gorivo je: {daily_fuel_price: .2f}€')
print(f'Mjesecni trosak na gorivo je: {monthly_price: .2f}€')
print()