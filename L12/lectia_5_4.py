"""
# =====================================================================

# Exerciții Simple de Încălzire

# =====================================================================
"""

# Exercițiul 0.1
# Creează o funcție care primește o listă de numere și returnează
# suma numerelor pare din listă
# def suma_pare(lista):
#     suma = 0
#     for num in lista:
#         if num % 2==0:
#             suma += num
#     return suma

# def sec_try(lista):
#  return sum(num for num in lista if num % 2==0)

# print(suma_pare([1, 2, 3, 4, 5, 6]))
# print(suma_pare([1, 3, 5, 7]))
# print(sec_try([1, 2, 3, 4, 5, 6]))
# print(sec_try([1, 3, 5, 7]))
"""=================================================================================================="""

# Exercițiul 0.2
# Creează o funcție care primește un șir de caractere și returnează
# numărul de vocale din șir (considerăm vocale: a, e, i, o, u)

# def numar_vocale(text):
#     vocale = "aeiou"
#     nr_vocale = 0
#     counter = 0
#     for litera in text:
#         if litera in vocale:
#             nr_vocale += 1
#     return  nr_vocale
#
# print(numar_vocale("Python"))
# print(numar_vocale("Exercitiu"))

"""=================================================================================================="""

# Exercițiul 0.3
# Creează o funcție care primește un număr și returnează True dacă
# numărul este prim, False în caz contrar

# def este_prim(numar):
#     for i in range(2, numar):
#         if numar % i == 0:
#             return False
#     return True
#
# print(este_prim(7))
# print(este_prim(12))
# print(este_prim(2))

"""
# =====================================================================

# Partea 1: Funcții Simple cu Logică Complexă

# =====================================================================
"""


# Exercițiul 1
# Creează o funcție care primește un șir de caractere și returnează True dacă este palindrom,
# ignorând spațiile și caracterele speciale.

# def is_palindrom(sir):
#     return sir == sir[::-1]
# print(is_palindrom('cojoc'))
# print(is_palindrom('capac'))
# # Ex: "A man a plan a canal Panama" -> True
# def palindrom_complex(text):
#     # preprocesare ignoram spatii si tot lower
#     string_nou = text.lower().replace(' ', '')
#     return string_nou == string_nou[::-1]
#
# print(palindrom_complex("Python"))                          # Output: False
# print(palindrom_complex("A man a plan a canal Panama"))     # Output: True
# print(palindrom_complex("raCe car"))                        # Output: True

"""=================================================================================================="""

# Exercițiul 2
# Scrie o funcție care primește un număr și returnează suma cifrelor sale
# până când rezultatul are o singură cifră

# Ex: 789 -> 7+8+9=24 -> 2+4=6
# def suma_cifre(numar):
#     numar_string = str(numar)
#     while len(numar_string) >1:
#         suma= sum(int(i) for i in numar_string)
#         numar_string = str(suma)
#     return numar_string


# print(suma_cifre(789))   # Output: 6
# print(suma_cifre(999))   # Output: 9
# print(suma_cifre(189))   # Output: 9
# print(suma_cifre(1234))
"""=================================================================================================="""

# Exercițiul 3
# Implementează o funcție care găsește cel mai lung prefix comun
# pentru o listă de șiruri. Ex: ["flower", "flow", "flight"] -> "fl"
def prefix_comun(lista_cuvinte):
    res = ""

    # Lungimea a cuvintului minim, pentru a nu obtine IndexOutOfRange
    if not lista_cuvinte:
        return res

    min_length = len(min(lista_cuvinte, key=len))

    # Este responsbail pentru iterarea prin index a cuvintelor
    for i in range(min_length):
        # primul cuvint din lista lista_cuvinte[0] --> litera curenat din primul cuvint lista_cuvinte[0][i]
        litera_curenta = lista_cuvinte[0][i]
        count = 0
        for cuvint in lista_cuvinte:
            if cuvint[i] == litera_curenta:
                count += 1
            else:
                break

        if count == len(lista_cuvinte):
            res += litera_curenta
        else:
            break

    return res
print(prefix_comun(["flower", "flow", "flight"]))               # Output: "fl"
print(prefix_comun(["dog", "racecar", "car"]))                  # Output: ""
print(prefix_comun(["interstellar", "interview", "interest"]))  # Output: "inter"
print(prefix_comun([]))                                         # Output: ""
print(prefix_comun(["", "test", "testing"]))                    # Output: ""
print(prefix_comun(["cat", "catalog", "category"]))             # Output: "cat"


"""
# =====================================================================

# Partea 2: *args, **kwargs și Parametri Opționali

# =====================================================================
"""


# Exercițiul 4
# Creează o funcție calculator care poate primi oricâți parametri numerici
# și un parametru optional 'operatie' care poate fi 'suma', 'produs', 'medie'
def calculator(*args, operatie='suma'):
    # TODO: Implementează funcția
    pass


# print(calculator(1, 2, 3, 4, operatie='suma'))         # Output: 10
# print(calculator(1, 2, 3, 4, operatie='produs'))       # Output: 24
# print(calculator(1, 2, 3, 4, operatie='medie'))        # Output: 2.5
# print(calculator())                                    # Output: 0
# print(calculator(1, 2, 3, operatie='invalid'))         # Output: "Operație nevalidă"

"""=================================================================================================="""

# Exercițiul 5
# Creează o funcție care poate primi orice tip de parametri și returnează
# un dicționar cu statistici despre tipurile parametrilor primiți

# statistici = {
#     "total_parametri":
#     "tipuri": {
#               "<class 'int'>": 2,
#               "<class 'str'>": 3
#               }
#     "args_count":
#     "kwargs_count":
#     "kwargs_keys":
# }
def analiza_parametri(*args, **kwargs):
    # TODO: Implementează funcția
    pass

# print(analiza_parametri(1, "text", 3.14, True))
# print(analiza_parametri(1, 2, nume="Ana", varsta=25))
# print(analiza_parametri(x=1, y="2", z=3.14))
# print(analiza_parametri())
# print(analiza_parametri([1,2,3], {"a":1}, lista=[4,5,6]))


"""
# =====================================================================

# Partea 3: Lambda și Funcții Încapsulate

# =====================================================================
"""


# Exercițiul 6
# Folosește map și lambda pentru a transforma o listă de dicționare
# Ex: [{nume: "Ana", varsta: 25}, {nume: "Ion", varsta: 30}] -> ["Ana are 25 ani", "Ion are 30 ani"]
def procesare_persoane(lista_dict):
    # TODO: Implementează funcția
    pass

# persoane = [
#    {"nume": "Ana", "varsta": 25},
#    {"nume": "Ion", "varsta": 30},
#    {"nume": "Maria", "varsta": 28},
#    {"nume": "Andrei", "varsta": 35},
#    {"nume": "Elena", "varsta": 22}
# ]
# print(procesare_persoane(persoane))

"""=================================================================================================="""

# Exercițiul 7
# Implementează o funcție care returnează un dicționar cu operații matematice:
# - inmultire(x)(y): returnează produsul x * y
# - putere(x)(y): returnează x la puterea y
# - divizare(x)(y): returnează x/y (sau None dacă y=0)
# - compunere(f,g)(x): aplică funcțiile f și g în ordine: f(g(x))
def generator_operatii():
    # TODO: Implementează funcția
    pass


# ops = generator_operatii()
# print(ops)
# # Test inmultire
# dublu = ops["inmultire"](2)
# triplu = ops["inmultire"](3)
# print(dublu(5))     # Output: 10
# print(triplu(4))    # Output: 12
#
# # Test putere
# patrat = ops["putere"](2)
# cub = ops["putere"](3)
# print(patrat(3))    # Output: 9
# print(cub(2))       # Output: 8
#
# # Test divizare
# jumatate = ops["divizare"](1)
# print(jumatate(2))  # Output: 0.5
# print(jumatate(0))  # Output: None
#
# # Test compunere
# f = ops["inmultire"](2)  # x * 2
# g = ops["putere"](2)     # x ^ 2
# h = ops["compunere"](f, g)
# print(h(3))         # Output: 18  (3^2 * 2)


"""
# =====================================================================

# BONUS

# =====================================================================
"""


# Scrie o funcție create_validator care returnează o funcție validate_data(data) ce validează un
# set de date. Aceasta include două funcții interne:

# validate_email(email): Verifică dacă adresa de email este validă (conține @, un domeniu cu
# extensie și partea locală).

# validate_password(password): Verifică dacă parola respectă cerințele de lungime și
# dacă conține cel puțin o literă mare.

# validator = create_validator()
# print(validator({'email': 'test@example.com', 'password': 'Password123'}))
# print(validator({'email': 'invalid-email', 'password': 'weak'}))


def create_validator():
    # TODO: Implementează funcția
    pass

# validator = create_validator()
# print(validator({'email': 'test@example.com', 'password': 'Password123'}))
# print(validator({'email': 'invalid-email', 'password': 'weak'}))