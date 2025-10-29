"""
# =====================================================================

# Exersare dictionare

# =====================================================================
"""
from logging import getLevelNamesMapping

# Exercitiu nr. 1:
# Conditia: Creează un dicționar numit `student` cu cheile "nume", "varsta" și "nota".
# student = {
#     "name":"SIMION",
#     "virsta":"9",
#     "nota":"10",
#     1:4
# }






# Exercitiu nr. 2:
# Conditia: Accesează și afișează valoarea pentru cheia "varsta" din dicționarul `student`.
# Rezolvarea:
# print(student["virsta"])
# print(student.get("virsta"))



# Exercitiu nr. 3:
# Conditia: Modifică valoarea cheii "nota" în dicționarul `student` la 10.
# Rezolvarea:
# student["nota"] = 10
# print(student)

# Exercitiu nr. 4:
# Conditia: Verifică dacă cheia "clasa" există în dicționarul `student`.
# Rezolvarea:
# if "clasa" in student:
#     print(student["clasa"])
# else:
#     print(f" nu exista chie clasa in {student}")

# Exercitiu nr. 5:
# Conditia: Șterge cheia "varsta" din dicționarul `student`.
# Rezolvarea:

# element = student.pop("nota")
# print(element)
# print(student)
# print(student["name"])
# del student["name"]
# print(student)

"""
# =====================================================================

# Exersare cu adaugarea si eliminarea elementelor din dictionare

# =====================================================================
"""
# Exercitiu nr. 1:
# Conditia: Adaugă o nouă cheie "clasa" cu valoarea "10A" în dicționarul `student`.
# Rezolvarea:


# Exercitiu nr. 2:
# Conditia: Elimină cheia "nota" din dicționarul `student` și afișează dicționarul.
# Rezolvarea:


# Exercitiu nr. 3:
# Conditia: Folosind metoda `clear()`, golește tot conținutul dicționarului `student`.
# Rezolvarea:


# Exercitiu nr. 4:
# Conditia: Reinitializează dicționarul `student` și adaugă mai multe chei deodată: "nume", "varsta", "nota".
# Rezolvarea:
# student = {"nume": "Alexandru", "virsta": 23, "nota": 7}


# Exercitiu nr. 5:
# Conditia: Adaugă un element cu cheia "email" și valoarea "ana@example.com" în dicționarul `student`.
# Rezolvarea:


"""
# =====================================================================

# Exersare cu keys(), values(), items()

# =====================================================================
"""
# Exercitiu nr. 1:
# Conditia: Creează un dicționar `catalog` care conține numele și notele mai multor elevi:
# Găsește și afișează media notelor.

# note = {"Ana": 6, "Marcu": 7, "Stefan": 10, "F": 9, "H": 3}
# print(sum(note.values())/len(note))



# Exercitiu nr. 2:
# Creează un dicționar de produse și prețuri, afișează numele produsului cu cel mai mare preț.
# note = {"Ana": 6, "Marcu": 7, "Stefan": 10, "F": 9, "H": 3}
#
# nota_max = max(note.values())
# for k,v in note.items():
#     if v == nota_max:
#         print(k)
#         break
#
#
#
# nota_min = -float('inf')
# numele = ""
# for nume,nota in note.items():
#     if nota > nota_min:
#         numele = nume
#         nota_min = nota
# print(numele)
#
# print(max(note, key=note.get))



# Exercitiu nr. 3:
# Conditia: Ai un dicționar `stoc` cu produse și cantități.
# Sterge produsele care au un stoc mai mic de 10.
# Rezolvarea:
stoc = {"mere": 12, "pere": 8, "banane": 15}
# stoc_min = min(stoc.values())
# lista_de_sters=[]
#
# for k,v in stoc.items():
#     if v < 10:
#         lista_de_sters.append(k)
#
#
# for k in lista_de_sters:
#     stoc.pop(k)
# print(stoc)

# for k,v in stoc.copy().items():
#     if v < 10:
#         stoc.pop(k)
# print(stoc)

# for k,v in stoc.copy().items():
#     if v < 10:
#         stoc.pop(k)
# print(stoc)

list


# Exercitiu nr. 4:
# Conditia: Ai un dicționar de angajați și salariile lor: `{"Andrei": 3000, "Elena": 4000, "Maria": 3500}`.
# Creează un nou dicționar doar cu angajații care au salariul mai mare de 3500 și afișează-l.
# Rezolvarea:
# salarii = {"Andrei": 3000, "Elena": 4000, "Maria": 3500}
# sal_mai_maria = {}
# for nume, salariu in salarii.items():
#     if salariu >= 3500:
#         sal_mai_maria[nume]=salariu
# print(sal_mai_maria)

# sal_mai_maria = {nume:salariu for nume, salariu in salarii.items() if salariu >= 3500}
# print(sal_mai_maria)

# Exercitiu nr. 5:
# Conditia: Creează un dicționar `inventar` cu produse și cantități: `{"mere": 10, "pere": 5, "banane": 8}`.
# Scade cantitatea fiecărui produs cu 1 (simulând vânzarea unui produs) și afișează noul dicționar.
# Rezolvarea:

# stoc = {"mere": 10, "pere": 5, "banane": 8}
#
# for k in stoc:
#     stoc[k]=stoc.get(k)-1
# print(stoc)

