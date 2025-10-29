"""
# =====================================================================

# Recapitulare

# =====================================================================
"""
from itertools import count
from socket import fromfd

# Exercitiu 1
# Având un dicționar, creează un nou dicționar în care cheile și valorile sunt inversate.
# Afișează dicționarul original și dicționarul inversat.
# Dicționarul original
original_dict = {
    "mar": 1,
    "banana": 2,
    "cireasa": 3,
    "curmal": 4,
    "piersica": 5,
    "portocala": 6,
    "kiwi": 7,
    "pepene": 8,
    "strugure": 9,
    "mango": 10
}
# dict_invrsat = {}
# dict_invrsat = {value : key for key, value in original_dict.items()}
#
#
# print(dict_invrsat)


# =====================================================================

# Exercitiu 2
# Având un array de numere întregi nums și un număr întreg k,
# întoarce cele mai frecvente k elemente din array. Ordinea elementelor returnate nu contează.

# nums = [1,1,1,2,2,3]
# k = 2
# freq = {}
# for num in nums:
#     freq[num] = freq.get(num, 0) + 1
# top_k = sorted(freq, key=freq.get ,reverse=True)[:k]
# print(top_k)

# from collections import Counter
# top_k = Counter(nums).most_common(k)
# print(top_k)

# res = []
# for num in top_k:
#     res.append(num[0])

# res = [num[0] for num in top_k]
# print(res)

# freq= {}
# liste = [[1,2],[2,2],[1,2],[2,2],[3,1]]
# for lista in liste:
#     lista.sort()
#     lista = tuple(lista)
#     freq[lista] = freq.get(lista, 0)+1
# print(freq)






"""
# =====================================================================

# Exersare tuple

# =====================================================================
"""
# Exercițiul 3: Imutabilitatea tuplurilor
# Condiția
# Creează un tuplu cu trei elemente. Încearcă să schimbi unul dintre elementele din tuplu și
# observă eroarea care apare.

# a = (1,2,3)
# a[0]= 9
# print(a)



# =====================================================================

# Exercițiul 4: Adăugarea elementelor într-un tuplu
# Condiția
# Creează un tuplu cu două elemente și încearcă să adaugi un al treilea element prin concatenare.
# Observă diferența față de modificarea elementului direct.
# a = (1,2,3)
# b = a+(4,)
# print(b)


# =====================================================================

# Exercițiul 5: Accesarea elementelor dintr-un tuplu
# Condiția
# Creează un tuplu cu mai multe elemente și accesează primul, ultimul și un element din mijloc
# folosind indexarea.

# tupla = (45,8,4,9,32,4,22,31)
# print(tupla[0],tupla[-1],tupla[int(len(tupla)/2)])


# =====================================================================

# Exercițiul 6: Obținerea unui sub-tuplu
# Condiția
# Extrage un sub-tuplu cu primele trei elemente dintr-un tuplu dat.

# tupla = (45,8,4,9,32,4,22,31)
# tupla2 = tupla[:3]
# print(tupla2)



# =====================================================================

# Exercițiul 7: Indexarea
# Condiția
# Accesează al doilea și al patrulea element dintr-un tuplu folosind indexare .

# tupla = (45,8,4,9,32,4,22,31)
# print(tupla[1], tupla[3])

# =====================================================================

# Exercițiul 8: Găsirea poziției unui element
# Condiția
# Găsește poziția unui element specificat într-un tuplu.

# import string
#
# tupla = (45,8,4,9,32,4,22,31,"?")
# for i in string.punctuation:
#     if i in tupla:
#         print(tupla.index(i))


# =====================================================================

# Exercițiul 9: Verificarea existenței și obținerea indexului
# Condiția
# Verifică dacă un element se află într-un tuplu; dacă da, afișează poziția sa.
# tupla = (45,8,4,9,32,4,22,31,"?")
# tupla = (45,8,4,9,32,4,22,31,"?")
# for i in string.punctuation:
#     if i in tupla:
#         print(tupla.index(i))
# =====================================================================

# Exercițiul 10: Numărul de apariții ale unui element
# Condiția
# Creează un tuplu cu valori repetitive și numără câte ori apare un anumit element.


# tupla = ("?",45,22,8,4,9,8,32,4,22,31,"?")
# freq= {}
# for i in tupla:
#     freq[i] = freq.get(i,0)+1
# print(tuple(freq.items()))



# =====================================================================

# Exercițiul 11:
# Condiția
# Creează un tuplu cu elemente de diferite tipuri și numără câte sunt de tip str.
# tupla = (9,2,'r',5,'g',7,'e')
# count=0
# for i in tupla:
#     if type(i) == str:
#         count +=1
# print(count)
# x =  [count+1 for i in tupla if type(i)== str]
# print(sum(x))
# =====================================================================

# Exercițiul 12:
# Condiția
# Creează o listă de numere cu duplicate. Transform-o într-un tuplu fără duplicate folosind un
# set, și afișează rezultatul.

# lista = [1, 2, 3, 4, 3, 2, 1, 5]
# mySet = {}
# for num in lista:
#     mySet[num] = mySet.get(num, 0)
# print(tuple(mySet))


# =====================================================================

# Exercițiul 12: Transformă datele de inventar într-un tuplu de articole disponibile
# Condiția
# Creează un dicționar de inventar în care cheia este numele produsului, iar valoarea este
# cantitatea. Folosește un ciclu while pentru a transforma inventarul într-un tuplu de
# produse cu cantități mai mari de 0.

inventar = {
    "mere": 10,
    "pere": 0,
    "struguri": 15,
    "caise": 0,
    "prune": 8
}
# data = inventar.keys()
# i=0
# x={}
# while i < len(inventar):
#     if inventar.values()>0:
#         print(inventar.values())
#     i=i+1






# =====================================================================


# Dat fiind un șir de numere întregi nums, returnează numărul de perechi bune.
# O pereche (i,j) este considerată bună dacă nums[i] == nums[j] și i < j.

# Exemplul 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explicație: Există 4 perechi bune: (0,3), (0,4), (3,4), (2,5), indexate de la 0.

# Exemplul 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explicație: Fiecare pereche din șir este bună.

# Exemplul 3:
# Input: nums = [1,2,3]
# Output: 0


# =====================================================================
