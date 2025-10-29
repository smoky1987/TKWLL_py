"""
# =====================================================================

# Exersare cu dictionare

# =====================================================================
"""
from urllib.request import proxy_bypass_registry

# Exercitiu 1: Primele două produse cu cel mai mic preț
# produse = {"TV": 6, "Frigider": 7, "Dulap": 10, "Canapea": 9, "Perna": 3}
#
# lowest_cost = sorted(produse.items(), key=lambda produs:produs[1],reverse=False)[:2]
# print(lowest_cost)

# produse2 = {"TV": 6, "Frigider": 7, "Dulap": 10, "Canapea": 9, "Perna": 3}
# prod_sort = sorted(produse2, key=lambda x:produse2[x],reverse=False)[:2]
# print(prod_sort)



# =====================================================================


# Exercitiu 2
# Creează un dicționar traduceri care să conțină câteva prescurtări frecvente folosite în mesaje
# (ex: "pls" devine "te rog", "u" devine "tu", "gr8" devine "grozav", etc.).
# Apoi, folosește-l pentru a înlocui aceste prescurtări într-un mesaj.
# Dicționar cu prescurtări și traducerile lor
# traduceri = {
#     "pls": "te rog",
#     "u": "tu",
#     "gr8": "grozav",
#     "b4": "înainte",
#     "idk": "nu știu",
#     "btw": "apropo",
#     "lol": "ha ha",
# }
# final_phrase = ""
# mesaj = "pls spune-mi u gr8 planul b4 idk ce sa fac, btw lol"
#
# mesaj_list = mesaj.split(" ")
# print(mesaj_list)
# #
# for mesaj in mesaj_list:
#     final_phrase += traduceri.get(mesaj, mesaj)+" "
#     print(final_phrase)



# for mesaje in mesaj_list:
#     if mesaje in traduceri:
#         final_phrase += " " + traduceri[mesaje]
#     else:
#         final_phrase += " "+mesaje
#
# print(final_phrase)

# =====================================================================



# Gestionează stocul unui magazin și adaugă informații suplimentare despre produse.
# Imagină-ți că ești managerul unui magazin care vinde produse de uz casnic.
# Fiecare produs are un preț și un stoc disponibil. Trebuie să gestionezi stocul pentru fiecare produs,
# iar dacă produsul are un stoc mai mic de 5 unități, trebuie să adaugi un mesaj de „Stoc redus”.
# De asemenea, trebuie să calculezi valoarea totală a stocului pentru fiecare produs,
# în funcție de preț și cantitate.
# Lista de produse din magazin
# produse = [
#     {"nume": "Mătură", "pret": 15, "stoc": 10},
#     {"nume": "Fier de călcat", "pret": 50, "stoc": 2},
#     {"nume": "Aspirator", "pret": 200, "stoc": 5},
#     {"nume": "Mop", "pret": 30, "stoc": 12},
#     {"nume": "Roboțel de bucătărie", "pret": 250, "stoc": 1},
# ]
#
# for prod in produse:
#     prod["prod_val"] = prod["pret"]*prod["stoc"]
#     if prod["stoc"]<5:
#         prod["mesaj"] = "Stoc redus"
#     print(prod)


"""
# =====================================================================

# Exersare cu seturi

# =====================================================================
"""
#
# # Exercitiu 1:
# # Adăugați un element într-un set și verificați dacă a fost adăugat
# set1 = {1, 2, 3, 4}
#
#
# set1.add(7)
# print(set1)
#
#
# # =====================================================================
#
#
# # Exercitiu 2:
# # Înlăturați un element dintr-un set folosind remove și verificați rezultatul
# set1.remove(7)
# print(set1)
#
# # =====================================================================
#
#
# # Exercitiu 3:
# # Folosiți pop pentru a elimina un element aleator dintr-un set și afișați-l
#
# print(set1.pop())
#
# # =====================================================================
#
#
# # Exercitiu 4:
# # Folosiți discard pentru a elimina un element care nu există în set
#
# set1.discard(7)
# print(set1)
#
# # =====================================================================
#
#
# # Exercitiu 5:
# # Verificați dacă un set conține un element specific
# print("{" in set1 )
#
#
#
# # =====================================================================
#
#
# # Exercitiu 6:
# # Iterați printr-un set și adăugați elementele într-o listă
# list = []
# for i in set1:
#     list.append(i)
# print(list)

"""
# =====================================================================

# Exersare cu metodele de seturi

# =====================================================================
"""

# Exercitiu 7:
# Uniunea a două seturi
# set7_1 = {1, 2, 3}
# set7_2 = {3, 4, 5}
#
# print(set7_1|set7_2)
# print(set7_1.union(set7_2))

# =====================================================================


# Exercitiu 8:
# Intersecția a două seturi

# print(set7_1&set7_2)
# print(set7_1.intersection(set7_2))


# =====================================================================


# Exercitiu 9:
# Verificați dacă două seturi sunt disjuncte (nu au elemente comune)

# set7_1 = {1, 2}
# set7_2 = {3, 4, 5}
# print(set()==set7_1.intersection(set7_2))
# print(set7_1.isdisjoint(set7_2))


# =====================================================================


# Exercitiu 10:
# Verificați dacă un set este submulțime al altui set
# set7_1 = {1, 2}
# set7_2 = {3, 4, 5}

# print(set7_1== set7_1.intersection(set7_2))
# print(set7_1.issubset(set7_2))
# print(set7_2.issubset(set7_1))

# =====================================================================


# Exercitiu 11:
# Diferența între două seturi
# print(set7_2-set7_1)

"""
# =====================================================================

# Exersare aditionala

# =====================================================================
"""

# Se dă o listă de cuvinte, în care unele cuvinte se pot repeta.
# Trebuie să construiești un dicționar care conține fiecare cuvânt din listă ca și cheie,
# iar valoarea asociată fiecărei chei să fie numărul de apariții al acelui cuvânt în listă.

# Lista de cuvinte care reprezintă culori, cu unele valori repetate
# cuvinte = ['Rosu', 'Verde', 'Rosu', 'Albastru', 'Rosu', 'Rosu', 'Verde', 'Rosu', 'Verde',
#            'Rosu', 'Albastru', 'Rosu', 'Rosu', 'Verde', 'Rosu', 'Verde', 'Rosu', 'Albastru',
#            'Rosu', 'Rosu', 'Verde']
#
# cuvinte_unice = []
# freq ={}
# for i in cuvinte:
#     if i not in cuvinte_unice:
#         cuvinte_unice.append(i)
# for cuvint in cuvinte_unice:
#     freq[cuvint] = cuvinte.count(cuvint)
# print(freq)

# for cuvint in  cuvinte:
#     if cuvint in freq:
#         freq[cuvint] = freq[cuvint] + 1
#     else:
#         freq[cuvint] = 0+1
# print(freq)

# for cuvint in  cuvinte:
#     freq[cuvint] = freq.get(cuvint,0) + 1
# print(freq)

# from collections import Counter
#
# freq2 = dict(Counter(cuvinte))
# print(freq2)



# =====================================================================

# Se dă o listă de numere și o valoare țintă. Trebuie să găsești toate perechile de numere din listă
# care au suma egală cu valoarea țintă și să le afișezi. Fiecare pereche trebuie să fie un set de
# două numere.

# Lista de numere și valoarea țintă
# nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# target_val = 35
# res = []
# visited = set()
# for num in nums:
#     val = target_val - num
#     if val in nums and val not in visited:
#         pereche = {num,val}
#         visited.update(pereche)
#         res.append(pereche)
# print(res)
