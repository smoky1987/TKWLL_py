"""
# =====================================================================

# Exersare break, continue, pass

# =====================================================================
"""
from enum import StrEnum
from itertools import count

# Exercitiul 1: Avem o listă de numere și vrem să căutăm primul număr care este mai mare decât 10.
# Oprim căutarea după ce găsim acest număr și îl afișăm.
# numere = [2, 5, 8, 12, 4, 6]
#
# for numa in numere:
#     if numa > 10:
#         print(numa)
#         break

# =====================================================================

# Exercitiul 2: Avem un șir și vrem să aflăm dacă conține un caracter special (!, @, #, etc.).
# Oprim bucla când găsim primul astfel de caracter și afișăm poziția lui.
sir, caractere_speciale = "Bine@venit", "!@#$%^&*"

# for idx in range(len(sir)):
#     if sir[idx] in caractere_speciale:
#         print(f"Indexul caracterului {idx}")
#         break


# for caracter in sir:
#     if caracter in caractere_speciale:
#         print(f"Indexul caracterului {sir.index(caracter)}")
#         break


# for idx,caracter in enumerate(sir):
#     print(idx, caracter )
#     print(f"Indexul caracterului {idx}")
#     break


# =====================================================================

# Exercitiul 3: Avem o listă de numere și vrem să le adunăm.
# Dacă suma totală depășește 50, ne oprim și afișăm suma curentă.
numere = [10, 15, 8, 20, 5]
suma = 0
# for i in numere:
#     if suma > 50:
#         break
#     suma += i
# print(suma)

# idx = 0
# while suma < 50:
#     suma += numere[idx]
#     idx+=1
# print(suma)


# =====================================================================

# Exercitiul 4: Avem o listă de numere și vrem să afișăm doar numerele pare.
# Dacă găsim un număr impar, sărim peste el.
# numere = [1, 2, 3, 4, 5, 6]
# for i in numere:
#     if i % 2 != 0:
#         print(f" Numar impar: {i}")
#         continue
#     print(i, "Numar par")


# =====================================================================

# Exercitiul 5: Avem o propoziție și vrem să afișăm doar cuvintele mai lungi de 3 litere.
# Dacă întâlnim un cuvânt scurt, îl sărim.
# propozitie = "Acesta este un exemplu simplu"
# lista_split = propozitie.split(" ")
# for cuv in lista_split:
#     if len(cuv) <= 3:
#         continue
#     print(cuv)
# print([cuv for cuv in propozitie.split() if len(cuv) > 3])


# =====================================================================

# Exercitiul 6: Avem o listă de numere (pozitive și negative) și vrem să calculăm suma doar a numerelor pozitive.
numere = [-5, 10, -2, 8, -1, 7]
suma = 0
# for num in  numere:
#     if num < 0:
#         continue
#     suma += num
# print(suma)

# print(sum([numar for numar in numere if numar >0 ]))

# =====================================================================

"""USE_CASE A OPERATORULUI PASS"""
# Exemplu 1: Placeholder într-o funcție goală:
def afiseaza_scor():
    pass


# Exemplu 2: Creăm o clasă ContBancar care momentan nu are metode și folosim pass pentru a lăsa structura pregătită pentru mai târziu.
class ContBancar:
    pass

# =====================================================================

# Exercitiul 7: Parcurgem o listă de numere și, dacă indexul este impar, folosim pass.
# În alte cazuri, afișăm numărul de la acel index.
numere = [5, 10, 15, 20, 25]



"""
# =====================================================================

# Exersare while, for

# =====================================================================
"""
# Exercitiul 8: FizzBuzz Alternativ
# Scrie un program care numără de la 1 la 100. Pentru multiplii lui 3, afișează „Fizz”,
# pentru multiplii lui 5, afișează „Buzz”, iar pentru multiplii lui 15, afișează „FizzBuzz”.
# În rest, afișează numărul.


# Exercitiul 9: Scrie un program care combină două liste într-una singură, fără elemente duplicat.
# Combinarea Două Liste Fără Duplicat


# Exercitiul 10: Creează un program care generează toate numerele Fibonacci până la un număr n.


"""
# =====================================================================

# Exersare aditionala

# =====================================================================
"""
# Exercitiul aditionala: Genereaza o lista cu primele n numere prime



# Exercitiu aditionala:
# Condiția: Găsiți cel mai mic an care este strict mai mare decât un an dat,
# având în vedere că toate cifrele din acest an trebuie să fie diferite între ele.
# Asigurați-vă că fiecare cifră este unică și că nu există repetări.

"""
TEST-CASES:
2023 --> 2031
1987 --> 2013
999 --> 1023
2019 --> 2031
10000 --> 10234
"""
# an = int(input("introdu un an: "))
# while True:
    # gasit=True
    # str_an= str(an)
    # # print(str_an)
    # # print(str_an.count("0"))
    # for cifra in str(an):
    #     if str(an).count(cifra) !=1:
    #         gasit=False
    #         break
    # if gasit:
    #     break
    # an +=1
# print(an)

#=========================================# USE DICTIONARY #=========================================#

# an = int(input("introdu un an: "))
# while True:
#     an +=1
#     gasit=True
#     freq = {}
#     an_str = str(an)
#     for cifra in an_str:
#         if cifra in freq:
#             gasit=False
#             break
#         freq[cifra] = 1
#     if gasit:
#         print(an)
#         break