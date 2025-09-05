'''
Zatražite od korisnika unos dva broja. 
Nakon unosa brojeva, ispišite:
    zbroj, razliku, umnožak, količnik (rezultat djeljnja), 
    potenciranje te modulo unesenih brojeva

Svaka operacija treba biti ispisana u novom redu, a ispis treba imati uključene brojeve, 
znak računske operacije te rezultat.
PRIMJER ISPISA: 
5 + 8 = 13
5 - 8 = -3

NAPOMENA Za sada kod unosa neka kod prvog unosa drugi broj NE bude 0 (nula), 
jer nije dopušteno dijeliti s nulom. To svakako pokušajte napraviti, ali NE u prvom pokušaju.
'''


# 1. Kraci oblik unosa teksta i konverzije u zeljeni tip podataka
a = int(input('Unesi vrijednost prvog broja: '))
b = int(input('Unesi vrijednost drugog broja: '))


# print('Zbroj brojeva a', a, 'i b', b, 'je ', a + b)
# print('Razlika brojeva a', a, 'i b', b, 'je ', a- b)
# print('Umnozak brojeva a', a, 'i b', b, 'je ', a * b)
# print('Kolicnik brojeva a', a, 'i b', b, 'je ', a / b)
# print('Potencija brojeva a', a, 'i b', b, 'je ', a ** b)
# print('Modula brojeva a', a, 'i b', b, 'je ', a % b)


# a + b = rezultat
# a - b = rezultat

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {round(a / b, 2)}')
print(f'{a} ** {b} = {a ** b}')
print(f'{a} % {b} = {a % b}')


