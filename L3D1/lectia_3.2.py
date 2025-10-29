"""
# =====================================================================

# Exersare cu for

# =====================================================================
"""
from ast import literal_eval
from itertools import count
from math import factorial
from operator import truediv
from wsgiref.util import application_uri

# Exercitiu 1:
# Condiția: Generează o listă cu pătratele numerelor de la 1 la 10
# lista=[]
# for i in range(1,11):
#     lista.append(i**2)
# print(lista)

# =====================================================================

# Exercitiu 2:
# Condiția: Calculează factorialul numărului 5

# nr = 1
# for i in range(2,6):
#     nr *= i
# print(nr)

# =====================================================================

# Exercitiu 3:
# Condiția: Afișează prima literă din fiecare cuvânt al propoziției 'Hello World Python'
# propzitia = 'Hello World Python'
# cuvinte = propzitia.split(" ")
# print(cuvinte)
# for i in range(len(cuvinte)):
#     print(cuvinte[i][0])


# =====================================================================

# Exercitiu 4:
# Condiția: Afișează o piramidă de numere până la 5
# exemplu:
#     1
#    22
#   333
#  4444
# 55555

# for i in range(1,6):
#     var = i*str(i)
#     print(var)

"""
# =====================================================================

# Exersare cu list comprehensions
# =====================================================================
"""


# Exercitiu 5:
# Condiția: Generează o listă cu pătratele numerelor de la 1 la 10
# lista = [numar**2 for numar in range(1,6)]
# print(lista)

# =====================================================================

# Exercitiu 6:

# import random
# lista = [random.randint(1,100) for i in range(100)]
# lista_pare = []
# for i in lista:
#     if i%2 == 0:
#         lista_pare.append(i)
# print(lista_pare)
#
# lista_pare = [i for i in lista_pare if i%2 == 0]
# print(lista_pare)

# =====================================================================

# Exercitiu 7:
# Condiția: Generează o listă cu lungimile fiecărui cuvânt din lista ['Ana', 'are', 'mere']
# lisa = ['Ana','are','mere']
# lista_lungimi= [len(cuvint) for cuvint in lisa]
# print(lista_lungimi)

# =====================================================================

# Exercitiu 8:
# Condiția: Generează o listă cu vocalele dintr-un șir de caractere dat
# str_de_car = 'kwiuayncbiyoiby4obbi4cwuabi4uwcoifuawbo'
# vocale = [litera for litera in str_de_car if litera in "aoieu"]
# print(vocale)
#
# cond = True
# if cond:
#     var = 'a'
# else:
#     var = 'b'
#
# var = "a" if cond else "b"
#
# lista = [0,1,2,3,4,5,6,7,8,9,10]
# #      [ceea ce                   de unde iau nr    cond de includere]
# vocale=["a" if i%2==0 else "b" for i in lista if i>6]
# print(vocale)

# litere = ["a", "b", "c", "d", "e", "f", "g", "h"]
# numere = [1, 2, 3, 4, 5, 6, 7, 8]
# tabla_de_sah = []
# litera = 'a'
# rind = [litera + str(numar) for numar in numere]
# tabla_de_sah=[rind for litera in litere]
# print(tabla_de_sah)


"""
# =====================================================================

# Exersare liste imbricate

# =====================================================================
"""
# Exercitiu 9:
# Condiția: Afișează fiecare element dintr-o listă de liste, daca elementul este negativ
# liste = [
#     [1,2,3,4,-7,8,-90],
#     [10,11,12,13,14,15],
#     [-16,-17,18,19,20],
# ]
#
#
# for lista in liste:
#     negative = []
#     for i in lista:
#         if i < 0:
#             negative.append(i)
#     print(i)


# =====================================================================

# Exercitiu 10:
# Condiția: Găsește suma tuturor elementelor dintr-o listă de liste.

# liste = [
#     [1,2,3,4,-7,8,-90],
#     [10,11,12,13,14,15],
#     [-16,-17,18,19,20],
# ]
# suma = 0
# for lista in liste:
#     suma += sum(lista)
# print(suma)
# print(sum([sum(lista) for lista in liste]))

# =====================================================================

# Exercitiu 11:
# Condiția: Calculează media valorilor din fiecare sublistă.
# liste = [
#     [1,2,3,4,-7,8,-90],
#     [10,11,12,13,14,15],
#     [-16,-17,18,19,20],
# ]
#
# for lista in liste:
#     suma = 0
#     count = 0
#     for i in lista:
#         suma += i
#         count += 1
#     media = suma / count
#     print(media)
#
# print([sum(lista)/len(lista)for lista in liste])


# =====================================================================

# Exercitiu 12:
# Condiția: Verifică dacă există un element specific într-o listă de liste.

liste = [
    [1,2,3,4,-7,8,-90],
    [10,11,12,13,14,15],
    [-16,-17,18,19,20],
]

element_Spec = 15
for lista in liste:
    for i in lista:
        if i == element_Spec:
            print(i)

"""
# =====================================================================

# Exersare while

# =====================================================================
"""
# cuvinte_permise = ["yes", "no", "y", "n"]
# cuvint = input('Introdu cuvintul, cuvinte permise sunt ["yes", "no", "y", "n"] ')
# while cuvint not in cuvinte_permise:
#     print("cuvint nepermis!")
#     cuvint = input('Introdu cuvintul, cuvinte permise sunt ["yes", "no", "y", "n"] ')
#
# print(cuvint)

# Exercitiu 13:
# Condiția: Afișează rezultatul toate puterile lui 2 mai mici decât 1000, folosind while

# nr = 2
# putere = 0
# while nr**putere < 1000:
#      print(nr**putere)
#      putere += 1


# =====================================================================
# Exercitiu 14:
# Condiția: Afișează numerele de la 10 la 1 în ordine descrescătoare
# nr = 10
# while nr != 1:
#     print(nr)
#     nr-=1




# =====================================================================

# Exercitiu 15:
# Condiția: Generează o listă cu primele 10 numere impare
# lista = []
# i = 1
# while len(lista) < 10:
#     lista.append(i)
#     i += 2
# print(lista)


# =====================================================================

# Exercitiu 16:
# Condiția: Suma numerelor de la 1 la 50
# Condiția: Calculează suma numerelor de la 1 la 50 folosind sum() și list comprehension
# suma = 0
# nr = 50
# while nr > 0:
#     suma += nr
#     nr -= 1
# print(suma)
#
# lista = [i for i in range(1,15)]
# suma = sum(lista)
# print(suma)

# n = 5
# print(n*(n-1)/2)




# =====================================================================

# Exercitiu 17:
# Condiția: Afișează cifra fiecărui caracter dintr-un număr dat
# nr = 123456789
# while nr > 0:
#     num= nr % 10
#     print(num)
#     nr //= 10

"""
# =====================================================================

# Exersare aditionala

# =====================================================================
"""


# Exercitiu 18:
# Condiția:  Afișează toate subșirurile (sublistele) listei [1, 2, 3]


# =====================================================================

# Exercitiu 19:
# Condiția: Găsește și afișează toate perechile de numere din intervalul 1-10 ale căror sumă este 10


# =====================================================================

# Exercitiu 20:
# Condiția: Determină toate numerele prime din intervalul [2, 100] cu ajutorul while
# numar_prime = []
# nr=2
# while nr < 101:
#     prim = True
#     for i in range(2,nr):
#         if nr%i==0:
#             prim = False
#     if prim:
#         numar_prime.append(nr)
#     nr+=1
# print(f"Prime numbers: {numar_prime}")
# print(17*17)

# =====================================================================

# Exercitiu 21:
# Condiția: Calculeaza și afișează toate numerele perfecte mai mici decât 10000

