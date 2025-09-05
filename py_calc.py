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
# 1. korak - pohranjujemo vrijednosti od korisnika
a = input('Unesi vrijednost prvog broja: ')
b = input('Unesi vrijednost drugog broja: ')

# 2. korak - Unesene brojeve pretvori u int

a = int(a) 
b = int(b) 


# print('Vrijednost a:', a) 
# print('Vrijednost b:', b)

print('Zbroj brojeva a', a, 'i b', b, 'je ', a + b)
print('Razlika brojeva a', a, 'i b', b, 'je ', a- b)
print('Umnozak brojeva a', a, 'i b', b, 'je ', a * b)
print('Kolicnik brojeva a', a, 'i b', b, 'je ', a / b)
print('Potencija brojeva a', a, 'i b', b, 'je ', a ** b)
print('Modula brojeva a', a, 'i b', b, 'je ', a % b)

'''
Modulo - simbol %

173 / 5 = 3
15
 23
 20
 (3) -> ovo je ostatak dijeljenja, odnosno modulo
'''