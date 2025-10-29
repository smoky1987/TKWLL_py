"""
# =====================================================================

# Exersare if, elif, else

# =====================================================================
"""
from ast import literal_eval

# Exercitiu 1:
# Condiția: Verifică dacă un număr introdus de utilizator este pozitiv, negativ sau zero.
# nr = int(input("un nr please: "))
# if nr > 0:
#     print("nr pozitiv")
# elif nr <0:
#     print("numar negativ")
# else:
#     print("egal zero")


# Exercitiu 2:
# Condiția: Verifică dacă o literă introdusă este vocală sau consoană.
# litera = input("un litera please: ")
# if litera in "aieou":
#     print("litera vocala")
# else:
#     print("litera consoana")

# Exercitiu 3:
# Condiția: Verifică dacă o vârstă introdusă este pentru copil, adolescent sau adult.
# virsta = int(input("Virsta va rog: "))
# if virsta <= 0:
#     print("virsta corecta ")
# elif virsta <18:
#     print("Copil")
# elif virsta <70:
#     print("Adolescent")
# else:
#     print("adult")


# Exercitiu 4:
# Condiția: Verifică dacă un an este bisect.
# Anul bisect trebuie sa fie divizibil cu 4
# dar nu trebuie sa fie divizibil cu 100, cu exceptia cazului in care este divizibil cu 400.

# anul = int(input("Introdu anul: "))
# if anul % 4 == 0:
#     if anul % 100 == 0:
#         # blah
#         if anul % 400 == 0:
#             print("Anul este bisect")
#         else:
#             print("Anul nu este bisect")
#     else:
#         print(" este un an bisect")
# else:
#     print("Nu este an bisect")

# bisect = ((anul % 4 == 0 and anul % 100 == 0 or anul % 400 == 0)
#           or (anul % 4 == 0 and anul % 100 != 0))
# if bisect:
#     print("an bisect")
# else:
#     print("nu e an bisect")


"""
# =====================================================================

# Exersare for cu if elif else

# =====================================================================
"""
# Exercitiu 5:
# Condiția: Afișează doar numerele pare dintr-o listă.
# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#
# for i in lista:
#     if i%2 == 0:
#         print(i)

# Exercitiu 6:
# Condiția: Afișează numerele negative dintr-o listă.
# lista = [1,2,3,4,-5,6,7,-8,9,10,-11,12,13,-14,15]
#
# for i in lista:
#     if i<0:
#         print(i, end="")

# Exercitiu 7:
# Condiția: Determină câte numere sunt pozitive, negative și zero într-o listă.
# lista = [1,2,0,4,-5,6,7,-8,9,10,-11,0,13,-14,15]
# pozitive, negative, zerouri = 0,0,0
# for n in lista:
#     if n > 0:
#         pozitive += 1
#     elif n <0:
#         negative += 1
#     else:
#         zerouri += 1
# print(pozitive, negative, zerouri)

# Exercitiu 8:
# Condiția: Afișează fiecare dintre primele 5 numere dintr-o listă, doar dacă sunt mai mari decât 10.

# lista = [1,22,0,4,-5,6,7,-8,9,10,-11,0,13,-14,15]
# for i in lista[:5]:
#     if i>10:
#         print(i)

# Exercitiu 9:
# Condiția: Determină suma tuturor numerelor impare dintr-o listă

# lista = [1,22,0,4,-5,6,7,-8,9,10,-11,0,13,-14,15]
# suma =0
# for i in lista:
#     if i%2!=0:
#         suma+=i
# print(suma)

"""
# =====================================================================

# Exersare for, if, elif, else, sortari

# =====================================================================
"""
# Exercitiu 10:
# Condiția: Sortează o listă de numere în ordine crescătoare și afișează rezultatul.
# lista = [1,5,2,8,3,9,4,7,6]
# lista.sort()
# lrng = len(lista)
# for n in range(lrng):
#     for j in range(lrng-1):
#         num = 0
#         if lista[n] < lista[j]:
#             num = lista[n]
#             lista[n] = lista[j]
#             lista[j] = num
# print(lista)


# Exercitiu 11:
# Condiția: Sortează o listă de numere și afișează doar numerele mai mari de 10.
# lista = [1,35,2,8,10,3,9,24,7,6]
# lista.sort()
# lrng = len(lista)
# lmmten=[]
# for n in range(lrng):
#     for j in range(lrng-1):
#         num = 0
#         if lista[n] < lista[j]:
#             num = lista[n]
#             lista[n] = lista[j]
#             lista[j] = num
#
# for m in range(lrng):
#     if lista[m] > 10:
#         lmmten.append(lista[m])
# print(lmmten)



# Exercitiu 12:
# Condiția: Găsește al doilea cel mai mare număr dintr-o listă,
# printeaza-l daca este divizorul lui 3
# lista = [1,35,2,8,10,3,9,24,7,6]
# lista.sort()
# if lista[len(lista)-2]%3==0:
#     print(f'numarul 3 este divizorul lui {lista[len(lista)-2]} sa invers')
# else:
#     print('nu e un divizor a lui 3')



# Exercitiu 13:
# Condiția: Afișează toate elementele unice dintr-o listă sortată.

# lista = [1, 2, 3, 3, 4, 5, 5]
# unelemente = []
# for i in lista:
#     if i not in unelemente:
#         unelemente.append(i)
# print(unelemente)

"""
# =====================================================================

# Exersare liste imbricate

# =====================================================================
"""

# Exercitiu 14:
# Condiția: Afișează fiecare element dintr-o listă de liste, daca elementul este negativ

# lista = [
#     [-1,2,3,4,5],
#     [1,-2,3,4,5],
#     [1,2,-3,4,5],
#     [1,2,3,-4,5],
#     [1,2,3,4,-5]
# ]
#
# for liste in lista:
#     for i in liste:
#        if i < 0:
#            print(i)
#     print("*"*50)

# Exercitiu 15:
# Condiția: Găsește suma tuturor elementelor dintr-o listă de liste.

# lista = [
#     [-1,2,3,4,5],
#     [1,-2,3,4,5],
#     [1,2,-3,4,5],
#     [1,2,3,-4,5],
#     [1,2,3,4,-5]
# ]
# suma = 0
# for liste in lista:
#     for i in liste:
#            suma += i
# print(suma)
#
#
# summa = 0
# for liste in lista:
#     suma+= sum(liste)
# print(summa)


# Exercitiu 16:
# Condiția: Calculează media valorilor din fiecare sublistă.
# suma = 0
# for i in lista:
#     medie = sum(lista)/len(lista)
#     print(medie)


# for liste in lista:
#     suma = 0
#     for i in liste:
#         suma += i
#     media = suma / len(lista)
#     print(media)

# Exercitiu 17:
# Condiția: Verifică dacă există un element specific într-o listă de liste.
# lista = [
#     [-1,2,3,4,5],
#     [1,-2,3,4,5],
#     [1,2,-3,4,5],
#     [1,2,3,-4,5],
#     [1,2,3,8,-5]
# ]
# # not shure about, but..
# for item in lista:
#     for j in item:
#         if j == 8:
#             print(j)
#             break
#         else:
#             print("None")
