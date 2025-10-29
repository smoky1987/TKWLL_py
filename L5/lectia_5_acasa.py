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

