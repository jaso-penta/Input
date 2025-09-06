'''
Imate 10000 kn i možete zaboraviti na njih na 15 godina. Ako Vam
banka nudi 2.5% godišnju kamatu za taj iznos, koliko ćete zaraditi
nakon 15 godina. Jednostavni kamatni račun k = C * p * t
• k = iznos kamata odnosno prinos
• C = iznos glavnice
• p = godišnja kamatna stopa –NAPOMENA: 5% = 5 / 100 = 0.05
• t = vrijeme u godinama
'''


# Varijable
print()
amount = float(input('Koliko novaca polazete ?: '))
interest_percent = float(input('Postotak kamata: '))
years = float(input('Na koliko godina polazete novac ?: '))
interest_rate = interest_percent / 100
print()


# Izracuni
k = amount * interest_rate * years


# Ispis
print(f"Nakon {years} godina zaradit cete {k:.2f} € na kamatama.")
print(f"Ukupno stanje bit ce {amount + k:.2f} €.")
print()