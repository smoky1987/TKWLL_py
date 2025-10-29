"""
# =====================================================================

# Exercitii cu citirea datelor din input și stocarea lor într-o listă

# =====================================================================
"""
from sys import prefix

# Exercițiul 1: Scrie un program care cere utilizatorului să introducă trei nume de prieteni și
# să le stocheze
# într-o listă. Afișează al doilea prieten din listă.
# Sugestie: Folosește input() pentru a obține numele și print()
# pentru a afișa al doilea prieten din listă.

# lista = []
# prieten_1 = input("Prieten 1 nume ?: ")
# lista.append(prieten_1)
# prieten_2 = input("Prieten 2 nume ?: ")
# lista.append(prieten_2)
# print(f"Numele al 2-ilea prieten este {lista[1]} ")

# Exercițiul 2: Citește de la utilizator o propoziție și împarte fiecare cuvânt într-o listă.
# Afișează al treilea cuvânt din propoziție.
# Sugestie: Folosește metoda split() pentru a împărți textul și print()
# pentru a afișa al treilea element din listă.

# text  = input("Scrie un text: ")
# lista = text.split() # sau lista=list(text)
# print(lista)
# print(f"Cuvintul al 3lea este : {lista[2]}")



"""
# =====================================================================

# Exersare cu append, concatenare, extend, remove, del

# =====================================================================
"""


# Exercițiul 3: Creează o listă goală de cumpărături. Citește de la utilizator trei produse și
# adaugă-le în listă
# folosind append(). Afișează lista la final.
# lgcumparaturi = []
# pr1 = input("Introdu primul produs: ")
# pr2 = input("Introdu al doilea produs: ")
# pr3 = input("Introdu al treilea produs: ")
# lgcumparaturi.append(pr1)
# lgcumparaturi.append(pr2)
# lgcumparaturi.append(pr3)
# print(lgcumparaturi)


# Exercițiul 4: Adaugă în lista de cumpărături alte trei produse utilizând extend()
# cu o altă listă ce conține aceste produse. Afișează noua listă.
# lista = ["ou","lapte"]
# lista.extend(['piine','ceapa'])
# print(lista)



# Exercițiul 5: Creează o listă cu trei filme preferate.
# Cere utilizatorului să introducă un nou film și adaugă-l în
# lista originală folosind +. Afișează lista actualizată.
# listMovies = ["F1","LOTR", "FAF", "War Craft"]
# newList = input("a new movie please: ")
# print(listMovies + [newList])


# # Exercițiul 6: Folosește lista de filme creată anterior.
# Șterge primul film din listă folosind remove() și afișează lista actualizată.

# lista =["LOTR", "FAF", "Die Hard"]
# lista.remove("FAF")
# lista.pop(len(lista)-1)
# print(lista)

# 1. Remove - sterge prima aparitie a elementului
# element = "Inexistent"
# element = "Inexistent"
# produse = ["ou","lapte"]
# if element in produse:
#     produse.remove(element)
#     print(produse)
# if element in produse:
#     produse.pop(produse.index(element))
#     print(produse)

"""
# =====================================================================

# Exersare cu pop, extend, remove, del

# =====================================================================
"""

# Exercițiul 7: Creează o listă cu patru fructe.
# Folosește pop() pentru a scoate al doilea fruct și afișează fructul eliminat și lista rămasă.
# fruitList = ['apple', 'banana', 'orange', 'grapefruit']
# print(fruitList)
# print(f" fructul eliminata este: {fruitList.pop(2)}")
# print(f"Lista ramasa: {fruitList}")




# Exercițiul 8: Creează o listă cu trei jucării. Adaugă două jucării noi cu extend(),
# apoi elimină prima jucărie cu del. Afișează lista actualizată.
# lj1 = ["tigru plus", "masina", "excavator"]
# lj1.extend(["constructor", "tiranosaur"])
# lj1.remove("tigru")
# print(lj1)

# Exercițiul 9: Creează o listă de animale și elimină unul dintre ele folosind remove().
# Afișează lista după ștergere.
# animal_list = ["tigru", "hiena", "hipopotam","girafa"]
# animal_list.remove("tigru")
# print(animal_list)
"""
# =====================================================================

# Exerciții mai complexe cu liste

# =====================================================================
"""
# Exercițiul 10: Creează o listă de nume ale colegilor din clasă.
# Ordinează lista în ordine alfabetică și afișează-o.
# După aceea, adaugă numele unui coleg nou și afișează lista actualizată, sortată din nou.

# lista = ["Max", "Ion", "Nicu", "Hatch"]
# lista.sort(reverse=True, key=len)   #lista.sort(reverse=True)  #lista.sort()
# # lista.append("Alina")
# # lista.sort()
# print(lista)


# Exercițiul 11: Gândește-te la o listă de prețuri ale unor produse și creează-o.
# Afișează prețul cel mai mic și cel mai mare
# din listă, apoi adaugă un nou preț. Afișează lista actualizată, sortată crescător.
# produse = ["ou","lapte","faina", "piine"]
# preturi = [15,20,35,70,1000,56, 45]

# for i in preturi:
#     if i %2 == 0:
#         if i %4 == 0:
#             print(i)

# preturi.sort()
# print(f"Cel mai mare element {preturi[-1]}")
# print(f"Cel mai mic element {preturi[0]}")

#functii built in
# print(max(preturi))
# print(min(preturi))

#for
# preturi = [15,20,35,70,1000]
# minimum =float("inf")  # valoare definita la infinit
# maximum = float("-inf") # valoare infinita minima
# for i in preturi:
#     if i< minimum:
#         minimum = i
# print(minimum)
#
# for i in preturi:
#     if i> maximum:
#         maximum = i
# print(maximum)




"""
# =====================================================================

# BONUS!!!

# =====================================================================
"""

# Creați o matrice de coordonate care reprezintă pozițiile unei table de șah.
# litere = ["a", "b", "c", "d", "e", "f", "g", "h"]
# numere = [1, 2, 3, 4, 5, 6, 7, 8]
# tabla_de_sah = []
# for l in litere:
#     for n in numere:
#         tabla_de_sah.append(l+str(n))
# print(tabla_de_sah)
