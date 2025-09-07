'''
 Na stranici https://www.color-hex.com/color-palette/33532 imate boje Google logotipa. Pomoću odgovarajućih naredbi za konverziju pokušajte pretvoriti RBG zapise u HEX boja i obratno.
• Primjer:
• Naziv boje HEX zapis RGB (Red Green Blue)
• CRVENA #EA4335 (234, 67, 53)
• Za HEX zapis EA-43-35 trebate dobiti RGB zapis 234-67-53
• NAPOMENA Zanemarite početni # znak u HEX zapisu sa stranice.
• NAPOMENA HEX zapis čine tri grupe po dva znaka EA-43-35, svaka dva znaka čine jednu boju RGB
'''


# HEX u RGB
print()
hex_1 = input('Unesi dva slova: ')
hex_2 = input('Unesi 2 broja: ')
hex_3 = input('Unesi 2 broja: ')

r = int(hex_1, 16)
g = int(hex_2, 16)
b = int(hex_3, 16)

print(f'RGB = {r}, {g}, {b}')

# RGB u HEX
print()
rgb_1 = int(input('Upisi 3 broja: '))
rgb_2 = int(input('Upisi 2 broja: '))
rgb_3 = int(input('Upisi 3 broja: '))

hexa = hex(rgb_1), hex(rgb_2), hex(rgb_3)

print(f'Hexadecimalni broj RGBa je: {hexa}')