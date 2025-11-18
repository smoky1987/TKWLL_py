"""
Sistem de Comenzi Restaurant

Creați o clasă Comanda care gestionează comenzile dintr-un restaurant folosind un stoc global.
Stocul conține produse cu nume, preț și cantitate disponibilă.

Clasa trebuie să:
1. Permită adăugarea produselor cu verificarea stocului
2. Actualizeze automat stocul la adăugarea produselor
3. Calculeze și afișeze nota de plată

Exemplu:
# >>> cmd = Comanda(1)
# >>> cmd.adauga_produs("Pizza Margherita", 2)  # True
# >>> cmd.adauga_produs("Suc", 1)               # True
# >>> cmd.adauga_produs("Pizza Margherita", 4)  # False (stoc insuficient)
#
# >>> cmd.afiseaza_nota()
Nota masa 1:
Pizza Margherita x2: 70 lei
Suc x1: 8 lei
Total: 78.00 lei
"""


stoc = [
   {"produs": "Pizza Margherita", "pret": 35, "cantitate": 5},
   {"produs": "Pizza Quattro", "pret": 40, "cantitate": 3},
   {"produs": "Paste", "pret": 30, "cantitate": 10},
   {"produs": "Suc", "pret": 8, "cantitate": 15},
   {"produs": "Tiramisu", "pret": 25, "cantitate": 7},
   {"produs": "Panna Cotta", "pret": 20, "cantitate": 10},
   {"produs": "Cheesecake", "pret": 30, "cantitate": 5},
   {"produs": "Clătite cu Nutella", "pret": 18, "cantitate": 12},
   {"produs": "Înghețată", "pret": 10, "cantitate": 20},
   {"produs": "Tort de ciocolată", "pret": 35, "cantitate": 6}
]


# class Comanda:
#     def __init__(self, nr_masa):
#         self.nr_masa = nr_masa
#         self.orders = {} # produs: cantitate
#
#     def adauga_produs(self, produs, cantitate):
#         in_stoc = self.is_available(produs, cantitate)
#         if not in_stoc:
#             print("stoc insuficient")
#             return
#
#         self.orders[produs] = self.orders.get(produs, 0) + cantitate
#         self.actualizeaza_stoc(produs, cantitate)
#
#     def is_available(self, produs, cantitate):
#         for p in stoc:
#             if p['produs'] == produs:
#                 return p['cantitate'] >= cantitate
#
#     def actualizeaza_stoc(self, produs, cantitate):
#         for p in stoc:
#             if p['produs'] == produs:
#                 p['cantitate'] -= cantitate
#                 return
#
#     def afiseaza_nota(self):
#         total = 0
#         res = f"Nota masa {self.nr_masa}:\n"
#
#         for produs, cantitate in self.orders.items():
#             pret = self.afla_pretul(produs) * cantitate
#             res += f"{produs}: x{cantitate}: {pret}lei\n"
#             total += pret
#
#         res += f"Total: {total}\n"
#         return res
#
#     def afla_pretul(self, produs):
#         for p in stoc:
#             if p['produs'] == produs:
#                 return p['pret']
#
# cmd = Comanda(3)
# cmd.adauga_produs("Pizza Margherita", 2)
# cmd.adauga_produs("Suc", 1)
# cmd.adauga_produs("Pizza Margherita", 4)  # Va eșua - stoc insuficient
# cmd.adauga_produs("Pizza Margherita", 1)
# cmd.adauga_produs("Tiramisu", 2)
# cmd.adauga_produs("Înghețată", 3)
# print(cmd)
"""
# =====================================================================

# Recapitulare

# =====================================================================
"""

"""
Creați o clasă Biblioteca care:
1. Inițializează o listă goală pentru cărți
2. Are metodă de adăugare carte (titlu, autor, an_publicare)
3. Are metodă de împrumut carte (titlu) - returnează False dacă cartea nu există
4. Are metodă de returnare carte (titlu)
5. Are metodă de afișare status bibliotecă

Exemple test:
>>> bib = Biblioteca()
>>> bib.adauga_carte("Poezii", "Eminescu")
>>> bib.afiseaza_carti()
"""


"""
# =====================================================================

# __str__    VS    __repr__

# =====================================================================
"""
# class Biblioteca:
#     def __init__(self):
#         self.carti={}
#         self.imprumuturi={}
#
#     def adauga_carte(self, titlu, autor, an_publicare=None):
#         if titlu not in self.carti:
#             self.carti[titlu]={'autor':autor, 'an_publicare':an_publicare}
#         print("Cartea deja exista")
#
#     def imprumut_carte(self,titlu, nume):
#         if titlu in self.carti:
#             self.imprumuturi[titlu]=nume
#             del self.carti[titlu]
#         print("Cartea nu este disponibila")
#
#     def __str__(self):
#         return (f"In biblioteca sunt: \n"
#                 f" {len(self.carti)} carti \n"
#                 f" {len(self.imprumuturi)} imprumuturi \n")
#
# bib = Biblioteca()
# bib.adauga_carte("Poezii", "Eminescu")
# print(bib.carti)
# print(bib.carti["Poezii"])
# print(bib.carti["Poezii"]["autor"])
# carte1 = Biblioteca()
# carte1.adauga_carte("Python pentru Începători", "John Doe")
# print(repr(carte1))  # Output: Carte(titlu='Python pentru Începători', autor='John Doe')
# print(str(carte1))  # Output: 'Python pentru Începători' scrisă de John Doe
#
# print(carte1.__repr__())
# print(carte1.__str__())
#
# print(carte1)

"""==================================================================================================="""

# import datetime
# # Creăm un obiect datetime cu fusul orar UTC, offset - aware
# a = datetime.datetime.now(datetime.UTC)
# # Convertim obiectul `a` la string folosind metoda __str__
# b = str(a)
#
# # Afișăm reprezentările __str__ și __repr__
# # Metoda __str__ implicită
# print(f"str(a): {str(a)}")
# # String-ul convertit
# print(f"str(b): {str(b)}")
#
# print()
#
# # Metoda __repr__ implicită
# print(f"repr(a): {repr(a)}")
# # Repr aplicat pe string-ul b
# print(f"repr(b): {repr(b)}")
#
# # Offset - naive
# c = datetime.datetime.now()
# print(str(c))
# print(repr(c))

# print(a < c)

"""==================================================================================================="""

"""Foloseste __str__"""

# 4. O clasă pentru Student care folosește liste
# class Student:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#         self.note = {}
#
#     def adauga_nota(self, materia, nota):
#         if nota > 10 or nota < 1:
#             return "Notă invalidă!"
#         elif materia in self.note:
#             return "Materia există deja!"
#         else:
#             self.note[materia] = nota
#             print(f"A fost adaugata nota: {nota} la {materia} pentru studentul {self.nume}")
#
#     def calculeaza_media(self):
#         return round(sum(self.note.values()) / len(self.note), 2)
#
#     def afiseaza_situatie(self):
#         res = f"Studentul {self.nume} cu varsta {self.varsta}\n"
#
#         res += "Situatia curenta:\n"
#         for materia, nota in self.note.items():
#             res += f"{materia}: {nota}\n"
#
#         res += f"Media totala {self.calculeaza_media()}\n"
#         return res
#
# s = Student("Ana", 20)
# s.adauga_nota("Matematica", 11) # -> "Notă invalidă!"
# s.adauga_nota("Matematica", 8)
# s.adauga_nota("Matematica", 9)  #-> "Materia există deja!"
# s.calculeaza_media()
# s.afiseaza_situatie()


"""
# =====================================================================

# Exersare staticmethod

# =====================================================================
"""

stoc = [
   {"produs": "Pizza Margherita", "pret": 35, "cantitate": 5},
   {"produs": "Pizza Quattro", "pret": 40, "cantitate": 3},
   {"produs": "Paste", "pret": 30, "cantitate": 10},
   {"produs": "Suc", "pret": 8, "cantitate": 15},
   {"produs": "Tiramisu", "pret": 25, "cantitate": 7},
   {"produs": "Panna Cotta", "pret": 20, "cantitate": 10},
   {"produs": "Cheesecake", "pret": 30, "cantitate": 5},
   {"produs": "Clătite cu Nutella", "pret": 18, "cantitate": 12},
   {"produs": "Înghețată", "pret": 10, "cantitate": 20},
   {"produs": "Tort de ciocolată", "pret": 35, "cantitate": 6}
]

# class Comanda:
#     def __init__(self, nr_masa):
#         self.nr_masa = nr_masa
#         self.orders = {} # produs: cantitate
#
#     def adauga_produs(self, produs, cantitate):
#         in_stoc = self.is_available(produs, cantitate)
#         if not in_stoc:
#             print("stoc insuficient")
#             return
#
#         self.orders[produs] = self.orders.get(produs, 0) + cantitate
#         self.actualizeaza_stoc(produs, cantitate)
#
#     def is_available(self, produs, cantitate):
#         for p in stoc:
#             if p['produs'] == produs:
#                 return p['cantitate'] >= cantitate
#
#     def actualizeaza_stoc(self, produs, cantitate):
#         for p in stoc:
#             if p['produs'] == produs:
#                 p['cantitate'] -= cantitate
#                 return
#
#     def afiseaza_nota(self):
#         total = 0
#         res = f"Nota masa {self.nr_masa}:\n"
#
#         for produs, cantitate in self.orders.items():
#             pret = self.afla_pretul(produs) * cantitate
#             res += f"{produs}: x{cantitate}: {pret}lei\n"
#             total += pret
#
#         res += f"Total: {total}\n"
#         return res
#
#     def afla_pretul(self, produs):
#         for p in stoc:
#             if p['produs'] == produs:
#                 return p['pret']

# cmd = Comanda(3)
# cmd.adauga_produs("Pizza Margherita", 2)
# cmd.adauga_produs("Suc", 1)
# cmd.adauga_produs("Pizza Margherita", 4)  # Va eșua - stoc insuficient
# cmd.adauga_produs("Pizza Margherita", 1)
# cmd.adauga_produs("Tiramisu", 2)
# cmd.adauga_produs("Înghețată", 3)
# print(cmd)

# # Test
# cmd = Comanda(3)
# cmd.adauga_produs("Pizza Margherita", 2)
# cmd.adauga_produs("Suc", 1)
# cmd.adauga_produs("Pizza Margherita", 4)  # Va eșua - stoc insuficient
# cmd.adauga_produs("Pizza Margherita", 1)
# cmd.adauga_produs("Tiramisu", 2)
# cmd.adauga_produs("Înghețată", 3)
# cmd.afiseaza_nota()
#
#
# cmd = Comanda(5)
# cmd.adauga_produs("Pizza Margherita", 1)
# cmd.adauga_produs("Pizza Margherita", 4)  # Va eșua - stoc insuficient
# cmd.adauga_produs("Tiramisu", 2)
# cmd.adauga_produs("Înghețată", 3)
# cmd.afiseaza_nota()

"""
# =====================================================================

# Exersare aditionala

# =====================================================================
"""

"""
Creați o clasă JocZaruri care:
- Permite aruncări multiple
- Ține scorul jucătorilor
- Determină câștigătorul

Staticmethods pentru:
- arunca_zar() - returnează 1-6
- verifica_combinatie(zar1, zar2) - "Dublu", "Sum pară", etc.
- determina_castigator(scor1, scor2)
"""


"""
Exercițiu: Implementarea unui Stack cu Urmărirea Minimului

Implementați o clasă Stack care să permită următoarele operații:
- Adăugarea unui element nou în stivă
- Eliminarea ultimului element adăugat
- Găsirea elementului minim din stivă în timp constant O(1)

Cerințe:
- Clasa trebuie să mențină ordinea elementelor ca într-o stivă normală (Last-In-First-Out)
- Metoda minim() trebuie să returneze cel mai mic element din stivă în timp constant O(1)
- Toate operațiile (adauga, scoate, minim) trebuie să fie eficiente

Indicație: 
Gândiți-vă cum ați putea urmări minimul curent pe măsură ce adăugați și eliminați elemente din stivă.
"""


class Stack:
    def __init__(self):
        self.elementele = []
        self.minimuri = []

    def adauga(self, nr):
        if len(self.elementele) == 0 or self.minim() >= nr:
             self.minimuri.append(nr)
        self.elementele.append(nr)


    def scoate(self):
        nr = self.elementele.pop()
        if nr == self.minim():
            self.minimuri.pop()


    def minim(self):
        return self.minimuri[-1] if self.minimuri else None

    def __str__(self):
        return f" in stiva {self.elementele}"



stack = Stack()
print("Adăugăm numere în Stack:")
stack.adauga(5)
print(stack)
stack.adauga(3)
print(stack)
stack.adauga(7)
print(stack)
print("Elementul minim in Stack este:")
print(stack.minim())
stack.adauga(2)
print(stack)

print("Elementul minim in Stack este:")
print(stack.minim())

print("Scoatem două numere:")
stack.scoate()  # Scoatem 2
print(stack)
stack.scoate()  # Scoatem 7
print(stack)

print("Elementul minim in Stack este:")
print(stack.minim())

stack.scoate()
print(stack)
print(stack.minim())

stack.scoate()
print(stack)
print(stack.minim())
