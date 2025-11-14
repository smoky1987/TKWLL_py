"""
# =====================================================================

# Exersare functii

# =====================================================================
"""

# Exercitiu 1
# Creaţi o funcţie care adună 2 numere şi returnează rezultatul

def add(x,y):
    print(f"arguments are {x} and {y}")
    return x + y
print(add(1,2))

# =====================================================================


# Exercitiu 2
# Creaţi o funcţie care înmulțește 3 numere şi returnează rezultatul


def multiplai(x,y,z):
    print(f"arguments are {x} , {y} and {z}")
    return x * y * z
print(multiplai(1,2, 4))

# =====================================================================


# Exercitiu 3
# Creaţi o funcţie care primeşte un parametru - un număr, şi afişează la ecran,
# dacă acest număr este mai mare, mai mic sau egal cu 5.

def checker(x):
    if x > 5 :
        return (f"valoarea mai mare ca 5 ")
    elif x < 5 :
        return (f"valoarea mai mic ca 5 ")
    else:
        return (f"valoarea este 5")
print(checker(5))

# =====================================================================


# Exercitiu 4
# Creaţi funcţia mediaNumere, care primeşte un parametru de tip listă,
# şi returnează media numerelor din lista respectivă.

def med_Listei(x:list):
    return sum(x) / len(x)

print(med_Listei([1,2,3,4,5]))
# =====================================================================


# Exercitiu 4
# Scrieți o funcție Python care găseşte maximul a trei numere

def max_3(a,b,c):
    max = a
    for i in [a,b,c]:
        if i > max:
            max = i
    return max

print(max_3(1,2,3))

# =====================================================================


# Exercitiu 5
# Scrieți o funcție Python care să înmulțească toate numerele dintr-o listă şi să returneze rezultatul

def mul_all(lista):
    res = 1
    for i in lista:
        res *= i
    return res

print(mul_all([1,2,6,9]))

# =====================================================================


# Exercitiu 6
# Creaţi funcţia myName, care primeşte parametrul nume(de tip String), şi afişează la ecran "Salut, <nume>",
# dar înainte de aceasta transformă numele să fie scris cu prima literă mare.

#
def call(nume):
    print(f"salut {nume.capitalize()}")

call("Alexandr")
print(call("L"))


# =====================================================================


# Exercitiu 7
# Scrieți o funcție Python care primeşte ca date de intrare un șir de caractere și calculează numărul de
# litere majuscule și minuscule. Funcţia trebuie să returneze ambele rezultate
# "sir de caractere CARE este Fain"



# =====================================================================


# Exercitiu 8
# Creați o funcție care primește un string și returnează un dicționar cu numărul de apariții pentru
# fiecare caracter.



# =====================================================================

# Exercitiu 9
# Creați o funcție care primește ca argument un număr și returnează o listă cu
# divizorii numărului respectiv.
# Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]

def find_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

print(find_divisors(8))
print(find_divisors(90))
print(find_divisors(789))
# =====================================================================


"""
# =====================================================================

# Exersare transformarea exercitiilor complexe in functii

# =====================================================================
"""
# Exercitiu 10
# Creează un dicționar de produse și prețuri, afișează numele produsului cu cel mai mare preț.

def func_10(note):
    cheie_note = list(note.keys())
    maximum = note[cheie_note[0]]
    numele = cheie_note[0]


    for cheie in cheie_note:
        if note[cheie] > maximum:
            maximum = note[cheie]
            numele = cheie
    return maximum, numele
note = {"Ana": 6, "Marcu": 7, "Stefan": 10, "F": 9, "H": 3}
print(func_10(note))
note = {"Ana": 10, "Marcu": 10, "Stefan": 10, "F": 10, "H": 8}
print(func_10(note))

# =====================================================================

# Exercitiu 11
# Având un dicționar, creează un nou dicționar în care cheile și valorile sunt inversate.
# Afișează dicționarul original și dicționarul inversat.
# Dicționarul original
# original = {
#     "banana": 1,
#     "rosie": 2,
#     "castravete": 3,
#     "olive": 4,
#     "apple": 5,
# }
#
# inversat = {}
# for k, v in original.items():
#     inversat[v] = k
#
# print(f"Dictionaru original: {original}")
# print(f"Dictionaru inversat: {inversat}")


# =====================================================================

# Exercitiu 12
# Având un array de numere întregi nums și un număr întreg k,
# întoarce cele mai frecvente k elemente din array. Ordinea elementelor returnate nu contează.

# nums = [1,1,1,1,1,12,2,2,2,2,2,3,3,33,5,44,4,4,444,555,5,5,5,5]
# k = 2
#
# # Cream frecventa a elementelor
# nums_set = set(nums)
# frecventa = {}
# for i in nums_set:
#     frecventa[i] = nums.count(i)
#
# # Sortam frecventa dupa ordine descrescatoare
# frecventa_lista = list(frecventa.items())
# frecventa_lista.sort(reverse=True, key=lambda x: x[1])
#
# # slicing [:k]
# list_compr = []
# for i in frecventa_lista[:k]:
#     list_compr.append(i[0])

# print(list_compr)
# print([x[0] for x in frecventa_lista[:k]])

# =====================================================================

# Exercitiu 13
# Se dă o listă de numere și o valoare țintă. Trebuie să găsești toate perechile de numere din listă
# care au suma egală cu valoarea țintă și să le afișezi. Fiecare pereche trebuie să fie un set de
# două numere.

# Lista de numere și valoarea țintă
# nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 10]
# target_val = 35
#
# nums_set = set(nums)
# result = set()
# # Iteram prin valorile setului
# for i in nums_set:
# # Aflam al - 2 - lea numar lipsa
#     valoarea_complementara = target_val - i
#     # Daca al doilea numar se gaseste, {i, valoarea_complementara}
#     if valoarea_complementara in nums_set:
#         result.add((i, valoarea_complementara))
#
# print(result)
#
# lista = [nums_set, result]
# print(lista)

# =====================================================================


# Exercitiu 14
# Condiția: Găsiți cel mai mic an care este strict mai mare decât un an dat,
# având în vedere că toate cifrele din acest an trebuie să fie diferite între ele.
# Asigurați-vă că fiecare cifră este unică și că nu există repetări.
# an = int(input("Introdu un an:"))
# an_urmatorul = an + 1
#
# while True:
#     gasit = True
#
#     an_str = str(an_urmatorul)
#     for i in range(len(an_str)):
#         for j in range(i+1, len(an_str)):
#             if an_str[i] == an_str[j]:
#                 gasit = False
#                 break
#         if not gasit:
#             break
#
#     if gasit:
#         print(an_urmatorul)
#         break
#
#     an_urmatorul += 1


# """
# # =====================================================================
#
# # Exersare lambda
#
# # =====================================================================
# """

# Să dublăm un număr:


# =====================================================================

# Adunarea a două numere:


# =====================================================================

# Sortarea unei liste de tuple după al doilea element:
# perechi = [(1, 'b'), (3, 'a'), (2, 'c')]


# =====================================================================

# Sortare după Lungimea Elementului într-o Listă de Șiruri

# cuvinte = ["banana", "mar", "portocala", "kiwi", "capsuna"]


# =====================================================================

# Sortare a unei Liste de Dictionare După un Anume Cheie

# produse = [
#     {"nume": "Telefon", "pret": 2000},
#     {"nume": "Laptop", "pret": 4000},
#     {"nume": "Tableta", "pret": 1500}
# ]


# =====================================================================

# Sortare după Multiple Chei: Mai Întâi după Primul Element, Apoi după Al Doilea Element
#     scoruri = {"Alice": 5, "Bob": 8, "Clara": 3}


# =====================================================================



# =====================================================================

# Filtrarea elementelor impare dintr-o listă:
# numere = [1, 2, 3, 4, 5, 6]


# =====================================================================

# Transformarea elementelor dintr-o listă cu map:
# numere = [1, 2, 3]


# """
# # =====================================================================
#
# # Exercitiu aditional
#
# # =====================================================================
# """
# """
#     Scrieţi o funcţie care primeşte 3 parametri: nume, prenume, varsta, în această ordine, şi calculează
#     care va fi preţul biletului de intrare la un muzeu pentru persoana respectivă, în modul următor:
# 	•	biletul standard costă 100 lei
# 	•	biletul pentru copii (până la 18 ani) costă 40 lei
# 	•	biletul pentru persoanele a căror prenume începe cu litera "A" costă 90 lei, dacă au mai mult de 17 ani
# 	Funcţia va returna preţul biletului calculat pentru fiecare persoană de o anumită vârstă.
# 	Citiţi de la tastatură datele persoanei şi apelaţi funcţia definită.
# """

