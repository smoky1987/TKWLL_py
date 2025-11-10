"""
# =====================================================================

# Exersare lambda

# =====================================================================
"""
from http.cookiejar import split_header_words
from math import factorial

# Să dublăm un număr:
# x=lambda a: a*2
# print(x(5))

# =====================================================================

# Adunarea a două numere:
# y = lambda a,b : a+b
# print(y(3,2))
# =====================================================================

# Sortarea unei liste de tuple după al doilea element:
# freq={'a':2,'b':8,'c':4,'d':9}
# lista = list(freq.items())
# lista.sort(key=lambda x: x[1])
# print(lista)

# =====================================================================

# Sortare după Lungimea Elementului într-o Listă de Șiruri
# lista =["ada","fweffw","qwdpoq","wkefhw","a"]
# lista.sort(key=lambda x:len(x))
# print(lista)

# =====================================================================

# Sortare a unei Liste de Dictionare După un Anume Cheie
# studenti = [
#     {"nume":"Ana", "nota":6},
#     {"nume":"Ion", "nota":7},
#     {"nume":"Maxim", "nota":5},
# ]
# studenti_sortati=sorted(studenti, key=lambda x: x["nota"])
# print(studenti_sortati)
# =====================================================================

# Sortare după Multiple Chei: Mai Întâi după Primul Element, Apoi după Al Doilea Element


# =====================================================================

# Filtrarea elementelor impare dintr-o listă:
# lista = [1,2,3,4,5,6,7,8]
# lista_pare= list(filter(lambda x:x%2==0, lista))
# print(lista_pare)
# =====================================================================

# Transformarea elementelor dintr-o listă cu map:
# lista = [1,2,3,4,5,6,7,8]
# dubl= list(map(lambda x:x*2, lista))
# print(dubl)

# =====================================================================

# Filtrează o listă de numere astfel încât să rămână doar cele care sunt pătrate perfecte.
# import math
# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# pp= list(filter(lambda x: x % math.sqrt(x)==0, lista))
# print(pp)

# =====================================================================

# Dintr-un text, extrage toate cuvintele distincte și sortează-le după lungime.
text = """Speedrunning is the act of playing a video game, or section of a video game, 
with the goal of completing it as fast as possible. Speedrunning often involves following 
planned routes, which may incorporate sequence breaking and exploit glitches that allow 
sections to be skipped or completed more quickly than intended. Tool-assisted speedrunning 
(TAS) is a subcategory of speedrunning that uses emulation software or additional tools to 
create a precisely controlled sequence of inputs."""

# text_distinct= set(text.split())
# text_distinct_sorted = sorted(text_distinct, key=lambda x: len(x))
# print(text_distinct_sorted)

# =====================================================================

# Calculează factorialul unui număr folosind reduce și lambda:
# from functools import reduce
# lista = [1,2,3,4]
#
# factorialul = reduce(lambda b,x: b+x*2, lista)
# print(factorialul)


"""
# =====================================================================

# Exersare Funcții Încapsulate

# =====================================================================
"""
# Scrie o funcție calculator_preturi care returnează două funcții:
# calculeaza_tva(pret_baza): Calculează TVA-ul (19%) din prețul de bază.
# pret_final(pret_baza): Calculează prețul final (preț de bază + TVA).

# def calculator_preturi():
#     def calculeaza_tva(pret_baza):
#         return pret_baza * 0.19
#
#     def pret_final(pret_baza):
#         return pret_baza + calculeaza_tva(pret_baza)
#
#     return calculeaza_tva, pret_final
#
# calculeaza_tva, pret_final = calculator_preturi()
# print(calculeaza_tva(2000))
# print(pret_final(2000))

# =====================================================================

# Scrie o funcție password_manager care returnează o funcție generate_password(length).
# Aceasta generează o parolă aleatorie de lungimea specificată, folosind caractere dintr-un
# set de litere mari și mici și cifre.



# def password_manager():
#     import random
#     import string
#     def generate_password(length):
#         password = ''
#         characters = string.ascii_letters+string.digits+string.punctuation
#         for i in range(length):
#             password += random.choice(characters)
#         return password
#     return generate_password
# generate_password = password_manager()
# print(generate_password(20))

# =====================================================================

# Scrie o funcție create_counter care returnează o funcție increment().
def create_counter():
    global counter
    counter = 0

    def increment():
        global counter
        counter += 1
        return counter

    def show_counter():
        global counter
        return counter

    return increment, show_counter

increment, show_counter = create_counter()
print(show_counter())
increment()
increment()
increment()
print(show_counter())

# =====================================================================
# Scrie o funcție create_cache care returnează o funcție calculator(n, operatie).
# Aceasta efectuează o operație ("patrat" sau "cub") asupra unui număr,
# dar folosește un cache pentru a stoca rezultatele anterioare,
# evitând astfel recalcularea acestora.

def create_cache():
    cache={}
    def calculator(n, operatie):
        if (n,operatie) in cache:
            print("Get from cache")
            return cache[(n,operatie)]
        else:
            print("Calculating..")
            res = n**2 if operatie == 'patrat' else n**3
            cache[(n,operatie)] = res
        return res
    return calculator

calculator = create_cache()
print(calculator(12, 'patrat'))
print(calculator(9, 'cub'))
print(calculator(10, 'cub'))
"""
# =====================================================================

# BONUS

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        return [k for k in counter if counter[k]>1]
        return list(filter(lambda k: counter[k]>1, counter))



# =====================================================================
"""
# Scrie o funcție create_validator care returnează o funcție validate_data(data)
# ce validează un
# set de date. Aceasta include două funcții interne:

# validate_email(email): Verifică dacă adresa de email este validă (conține @, un domeniu cu
# extensie și partea locală).

# validate_password(password): Verifică dacă parola respectă cerințele de lungime și
# dacă conține cel puțin o literă mare.

# validator = create_validator()
# print(validator({'email': 'test@example.com', 'password': 'Password123'}))
# print(validator({'email': 'invalid-email', 'password': 'weak'}))

