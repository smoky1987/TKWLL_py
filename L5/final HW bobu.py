"""
# =====================================================================

# Exercitii cu citirea datelor din input și stocarea lor într-o listă

# =====================================================================
"""
from wsgiref.util import application_uri

# Exercițiul 1: Realizează o listă cu trei orașe preferate. Afișează ultimul oraș din listă
# folosind slicing negativ.
# Sugestie: Folosește -1 ca index pentru a accesa ultimul element din listă.
# orase =["Chisinau", "Kiev", "Bangladesh"]
# print(orase[-1::])

# Exercițiul 2: Scrie un program care citește de la utilizator 5 activități preferate și
# le stochează într-o listă.
# Apoi, folosește index() pentru a afla poziția unei activități specificate de utilizator și
# afișeaz-o.
# Sugestie: Folosește input() pentru a obține activitățile și index() pentru a găsi poziția.
# activity = []
# ac1 = input("Activitatea 1: ")
# ac2 = input("Activitatea 2: ")
# ac3 = input("Activitatea 3: ")
# ac4 = input("Activitatea 4: ")
# ac5 = input("Activitatea 5: ")
# activity.append(ac1)
# activity.append(ac2)
# activity.append(ac3)
# activity.append(ac4)
# activity.append(ac5)
# print("Activitatea ta se afla pe pozitia ",activity.index(input("Care e activitatea? ")))


"""
# =====================================================================

# Exersare cu append, concatenare, extend, remove, del

# =====================================================================
"""

# Exercițiul 3: Creează o listă goală de cumpărături.
# Citește de la utilizator trei produse și adaugă-le în listă
# folosind append(). Afișează lista la final.
# lgCumparaturi =[]
# c1 = input("Cumparatura 1: ")
# c2 = input("Cumparatura 2: ")
# c3 = input("Cumparatura 3: ")
# lgCumparaturi.append(c1)
# lgCumparaturi.append(c2)
# lgCumparaturi.append(c3)
# print("Cumparaturile sunt", lgCumparaturi)

# Exercițiul 4: Folosește del pentru a elimina ultimul element din lista de
# cumpărături creată mai sus.
# Afișează lista după ștergere.

# bought_list = ["ciorapi", "stergare", "pantaloni"]
# bought_list.__delitem__(len(bought_list)-1)
# print(bought_list)

# Exercițiul 5: Creează o listă cu trei culori preferate.
# Cere utilizatorului să introducă o culoare și elimină-o din listă folosind remove().
# Afișează lista.
# color = ["Red","Green","Blue","Black","White"]
# delColor = input("color to delete: ")
# color.remove(delColor)
# print(color)

"""
# =====================================================================

# Exersare cu pop, extend, remove, del

# =====================================================================
"""

# Exercițiul 6: Creează o listă de trei activități preferate.
# Elimină ultima activitate cu pop(),
# afișând atât activitatea eliminată, cât și lista rămasă.
# lista_actvt = ["volei", "basket", "footbal"]
# lista_actvt.pop(len(lista_actvt) - 1)
# print(lista_actvt)

# Exercițiul 7: Creează o listă cu patru cărți.
# Adaugă o carte nouă la finalul listei cu append().
# Elimină prima carte din listă folosind del.

# carti_lista = ["c1","c2","c3","c4"]
# carti_lista.append("c5")
# del carti_lista[0]
# print(carti_lista)

# Exercițiul 8: Folosește lista de cărți creată mai sus. Scoate ultima carte cu pop()
# și afișează cartea scoasă împreună cu lista rămasă.
# carti_lista = ["c1","c2","c3","c4"]
# print(carti_lista.pop(len(carti_lista)-1))
# print(carti_lista)


"""
# =====================================================================

# Exerciții mai complexe cu liste

# =====================================================================
"""


# Exercițiul 9: Creează o listă de trei destinații de vacanță preferate.
# După ce utilizatorul adaugă o nouă destinație,
# îmbină lista originală cu cea nouă și afișeaz-o în ordine alfabetică.
# destinatii = ["turcia", "croatia", "grecia"]
# add_destination = input("Ce destinatie? ")
# destinatii.append(add_destination)
# destinatii.sort()
# print(destinatii)

# Exercițiul 10: Creează o listă cu numere de la 1 la 10. Afișează doar numerele pare
# folosind slicing și apoi elimină numerele impare din listă.
# Afișează lista finală cu numere pare.

# listaN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newList = []
# newList.extend(listaN[1::2])
# print(newList)

# Exercitii cu functia .join()
from os.path import split
# Exercitiu 1: Folosește funcția join pentru a combina cuvintele într-o propoziție.
# cuvinte = ["Ana", "are", "mere"]
# Răspunsul tau mai jos:
# print("".join(cuvinte))
from time import process_time_ns

# Exercitiu 2: Folosește join pentru a separa cuvintele cu o virgulă.
# lista_cumparaturi = ["pâine", "lapte", "ouă"]
# Răspunsul tau mai jos:
# print(", ".join(cuvinte))


# Exercitiu 3: Folosește join pentru a crea o listă de nume separate prin punct și virgulă.
# nume = ["Ioana", "Mihai", "Elena"]
# Răspunsul tau mai jos:
# print("; ".join(nume))

# Exercitiu 4: Folosește join pentru a adăuga puncte între literele unui cuvânt.
# cuvant = "cuvânt"
# Răspunsul tau mai jos:
# l = '.'.join(cuvant)
# print(l)
# print('.'.join(list(cuvant)))

# Exercitiu 5: Folosește join pentru a conecta elementele unei liste cu un spațiu nou-linie.
# versuri = ["Mereu spre stele", "Privim adânc", "Și visăm"]
# Răspunsul tau mai jos:
# x= ' -'.join(versuri)
# print(x)
# print(versuri.join("-"))
# =====================================================================


# =====================================================================
# Exercitii cu functia .split()
# Exercitiu 1: Folosește funcția split pentru a împărți o propoziție în cuvinte.
# propozitie = "Ana are mere"
# Răspunsul tau mai jos:
# print(propozitie.split(" "))

# Exercitiu 2: Împarte o listă de cumpărături în elemente separate,
# folosind virgula ca separator.
# lista_cumparaturi = "pâine, lapte, ouă"
# # Răspunsul tau mai jos:
# lc = lista_cumparaturi.split(", ")
# print(lc)


# Exercitiu 3: Împarte un șir de caractere la fiecare punct și virgulă.
# nume = "Ioana; Mihai; Elena"
# Răspunsul tau mai jos:
# print(f"numele sunt{nume.split("; ")}")

# Exercitiu 4: Folosește split pentru a descompune o dată în zi, lună și an.
# data = "25/04/2022"
# Răspunsul tau mai jos:
# print(data.split("/"))

# Exercitiu 5: Împarte o frază folosind spațiul ca separator și obține primele două cuvinte.
# fraza = "Astăzi este o zi frumoasă"
# # Răspunsul tau mai jos:
# x =fraza.split(" ")
# print(x[0],x[1])

# =====================================================================


# =====================================================================

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
