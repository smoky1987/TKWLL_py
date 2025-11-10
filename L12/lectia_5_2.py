"""
# =====================================================================

# Recapitulare

# =====================================================================
"""
from typing import Optional


#
# def get_first_even(numbers: list) -> Optional[int]:
#     for number in numbers:
#         if number % 2 == 0:
#             return number
#
#     return None
# result = get_first_even([1, 3, 5, 9, 1])
# print(result)
#
# """==================================================================================================="""

# def j(w, s=", "):
#     r = ""
#     for i in range(len(w)):
#         r += w[i] + s
#     return r
#
# a = ["apple", "banana", "cherry"]
# x = " - "
# z = j(a, x)
# print(z)
# """==================================================================================================="""

# def join_strings(words, separator=", "):
#     result = ""
#     for word in words:
#         result += word + separator
#     return result
#
# result = join_strings(["apple", "banana", "cherry"], " - ")
# print(result)

# """==================================================================================================="""
# class Finder:
#     MAX_CLIKCS = 70
#
# def find_first_above(numbers, threshold):
#     for number in numbers:
#         if number > threshold:
#             return number
#     return None
#
# result = find_first_above([3, 7, 1, 9, 2], 5)
#
# """==================================================================================================="""

# def add_item(item, items=[]):
#     items.append(item)
#     return items
#
# list_a = add_item(1)
# list_b = add_item(2, [2, 3, 4])
# list_c = add_item(3)

# Ce output vor avea list_a, list_b și list_c?
# print(list_a)
# print(list_b)
# print(list_c)


"""
# =====================================================================

# Exercitii valori optionale

# =====================================================================
"""

# Funcție cu parametri opționali și valori implicite
# Creează o funcție care primește numele și tipul unui animal de companie. Dacă tipul
# nu este specificat, implicit va fi "câine".
# def ex_1(numele, tipul="ciine"):
#     return f"Eu am un {tipul} si-l cheama {numele}"
#
# print(ex_1("Kesa","papagal"))
# print(ex_1("Asea"))
# print(ex_1("Asea","cine"))

"""==================================================================================================="""

# Salut Personalizat
# Scrie o funcție greet care primește doi parametri:
# name (numele persoanei), obligatoriu.
# greeting (felul în care vrei să saluți persoana), opțional, cu valoarea implicită "Salut".

# def greet(name, greeting="Salut"):
#     print(f" {greeting}, {name} !")
#
# greet("Simion")
# greet("Simi", "Buna")

"""==================================================================================================="""
# Scrie o funcție care primește trei parametri:

# a și b, două numere obligatorii.
# operation, o valoare opțională, implicit fiind "adunare".

# Funcția ar trebui să returneze rezultatul operației (adunare, scădere, înmulțire sau împărțire)
# între a și b în funcție de valoarea lui operation.

# def calculator(a,b,operation="adunare"):
#     if operation == "adunare":
#         return a+b
#     elif operation == "scadere":
#         return a-b
#     elif operation == "inmultire":
#         return a*b
#     else:
#         return a/b
# print(calculator(2,3))
# print(calculator(2,3,"scadere"))
# print(calculator(2,3, "inmultire"))
# print(calculator(2,3, "impartire"))
#
#
#
# def calculator2(a,b, operation="adunare"):
#     calc = {
#         "scadere":a-b,
#         "inmultire":a*b,
#         "impartire":a/b
#     }
#     return calc.get(operation, a+b)
#
# print(calculator2(2,3))
# print(calculator2(2,3,"scadere"))
# print(calculator2(2,3, "inmultire"))
# print(calculator2(2,3, "impartire"))
"""
# =====================================================================

# Exercitii args

# =====================================================================
"""

"""ARGS - TUPLE"""


# Suma tuturor numerelor
# Scrie o funcție care primește un număr variabil de argumente numerice și returnează
# suma acestora.

# def add(*args):
#     return f" {sum(args)}"
#
# print(add(1,2,3,4))
# print(add(1,2))
# print(add())


"""==================================================================================================="""

# Media numerelor
# Scrie o funcție care primește mai multe numere și returnează media lor.

# def media(*args):
#     return sum(args) / len(args)
#
# print(media(1,2,3,4))
# print(media(1,2))
# print(media(4,5,7,900,890))
"""==================================================================================================="""

# Concatenează toate cuvintele
# Scrie o funcție care primește un număr variabil de cuvinte (ca stringuri) și
# returnează un singur string format din toate cuvintele concatenate.
# def concatinatie(*args) -> Optional[str]:
#     conc =""
#     for arg in args:
#         conc = conc + arg
#     return conc
# print(concatinatie("ion"," cupi"," baton"))

"""==================================================================================================="""

# Numără elementele ne-numerice
# Scrie o funcție care primește un număr variabil de argumente
# și returnează câte dintre ele nu sunt numere (adică nu sunt de tip int sau float).

# def elem_nenum(*args):
#     count = 0
#     for arg in args:
#         if type(arg) != int and type(arg) != float:
#             count += 1
#     return count
#
# print(elem_nenum(1, 2.0, 3.2,"miami", "sport"))
"""==================================================================================================="""

# Filtrează și păstrează doar numerele pozitive
# Scrie o funcție care primește un număr variabil de argumente numerice și
# returnează o listă cu doar numerele pozitive.
# def pztv_num(*data):
#     fin=[]
#     for i in data:
#         if 0 < i:
#             fin.append(i)
#     return fin
# print(pztv_num(-1,2,-5,7,-3,9))

"""
# =====================================================================

# Exercitii kwargs

# =====================================================================
"""

"""KWARGS - DICT"""

# Afișează profilul utilizatorului
# Scrie o funcție care acceptă detalii despre o persoană (de exemplu, nume, vârstă, oraș etc.)
# și afișează aceste informații într-un format plăcut.

# def afiseaza_profilul(**kwargs):
#     # return  f" {type(kwargs)} ****** {kwargs} "
#     res=""
#     for key, value in kwargs.items():
#         res+=f"{key}={value}\n"
#     return res
# print(afiseaza_profilul(nume="Simion", varsta="90", oras="Chisinau"))
# print(afiseaza_profilul(nume="Alex",oras="Chisinau",  varsta="10" ))
# print(afiseaza_profilul(nume="Alex",oras="Chisinau"))


"""==================================================================================================="""

# Calculează prețul total al produselor
# Scrie o funcție care primește produse și prețurile lor și returnează suma totală a prețurilor.

"""==================================================================================================="""

# Filtrează și afișează doar atributele care sunt stringuri
# Scrie o funcție care primește diverse atribute și le afișează doar pe cele care sunt de tip str.

# def afiseaza_str(**params):
#     for k,v in params.items():
#         if isinstance(v, str):
#             print(f"{k}: {v}")
# print(afiseaza_str(k="k", nume="Simion"))
# print(afiseaza_str(k="k", nume="Simion", nr=10))
# print(afiseaza_str(k="k", nume="Simion", nr="10"))


"""==================================================================================================="""

# Calculează media valorilor numerice
# Scrie o funcție care primește diverse atribute și returnează media valorilor care sunt de tip int
# sau float.


"""==================================================================================================="""

# Afișează adresa completă
# Scrie o funcție care acceptă diverse părți ale unei adrese (de exemplu, stradă, oraș, țară etc.)
# și le afișează într-un format de adresă completă.


"""
# =====================================================================

# Exercitii combinate

# =====================================================================
"""

# Calculator de Discounturi
# Scrie o funcție calculate_discount(*prices, **discount_options) care primește:
#
# o listă de prețuri (*args) [100,200,300,500]

# opțiuni de discount (**kwargs) precum percentage (un procentaj de discount),
# apply_to_all (dacă se aplică tuturor articolelor) și specific_item (pentru a aplica discount
# doar la un anumit preț).{"percentage": 30, "apply_to_all": False, "specific_items":[0]}
# Returnează suma totală după aplicarea discountului.

# def calculate_discout(*prices, percentage=10, **discount_options):
#     suma = 0
#     if discount_options.get("apply_to_all"):
#         suma = sum(prices)
#         return round(suma * percentage / 100, 2)
#     specific_items = discount_options.get("specific_items", [])
#     for idx in range(len(prices)):
#         if idx in specific_items:
#             suma+=prices[idx]*(1-percentage/100)
#     return suma
#
# print(calculate_discout(100,200,3000, reducere = True, percentage=50,apply_to_all=True))
# print(calculate_discout(100,200,3000,400, percentage=20,specific_items = [0]))
# print(calculate_discout(100,200,3000,400,600,specific_items = [0],apply_to_all=False))



"""==================================================================================================="""
# def add_item(item, items=None):
#     items = items or []
#     items.append(item)
#     return items
#
# list_a = add_item(1)
# list_b = add_item(2, [])
# list_c = add_item(3)
# print(list_a)
# print(list_b)
# print(list_c)
