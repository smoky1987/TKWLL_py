"""
# =====================================================================

# Exersare cu clase

# =====================================================================
"""

"""
2. Clasa Produs
Implementați un produs dintr-un magazin online cu:

Atribute:
- nume (str)
- pret (float)
- stoc (int)

Metode:
- este_disponibil(): Returnează True dacă stoc > 0
- actualizeaza_stoc(cantitate): Adaugă sau scade din stoc
- aplica_reducere(procent): Reduce prețul cu procentul dat
"""

# class Produs:
#     def __init__(self, nume, pret, stoc):
#         self.nume = nume
#         self.pret = pret
#         self.stoc = stoc
#
#     def este_disponibil(self):
#         return self.stoc > 0
#     def actualizeaza_stoc(self, cantitate):
#         self.stoc += cantitate
#         print(f"Stoc actualizat. Stoc nou: {self.stoc}!")
#     def aplica_reducere(self, procent):
#         self.pret = self.pret - self.pret/procent
#
# tv = Produs(nume="Samsung 10800",pret=900,stoc=1000)
# tv.actualizeaza_stoc(100)
# print(f"Stoc nou: {tv.stoc}!")
# tv.aplica_reducere(10)
# print(f"Pret nou: {tv.pret}!")
"""==================================================================================================="""


"""
Clasa ContBancar

Cerințe:
1. Atribute
   - titular (str): Numele deținătorului contului
   - sold (float, default=0): Suma disponibilă în cont

2. Metode
   - depune(suma): Adaugă bani în cont 
   - retrage(suma): Scoate bani din cont

Exemplu:
>>> cont = ContBancar("Ion Popescu", 1000)
>>> cont.depune(500)   # Output: "S-au depus 500 lei. Sold nou: 1500 lei"
>>> cont.retrage(2000) # Output: "Fonduri insuficiente!"
"""
# class ContBancar:
#     def __init__(self, titular: str, sold=0):
#         self.titular = titular
#         self.sold = sold
#
#     def depune(self, suma):
#         self.sold += suma
#         return f"A fost depusa suma {suma}, sold curenta: {self.sold}"
#     def retrage(self, suma):
#         if self.sold<suma:
#             return f"fonduri insuficiente"
#         else:
#             self.sold -= suma
#             return f"a fost retrasa suma {suma}, sold curenta: {self.sold}"
#
# cont = ContBancar("Ion Popescu", 1000)
# print(cont.depune(500))
# print(cont.retrage(700))
"""==================================================================================================="""


"""
Extindeți clasa Student pentru a:
1. Valida notele (1-10)
2. Nu permite adăugarea aceleiași materii de două ori
3. Permite modificarea notei la o materie
4. Returnează lista materiilor cu note sub 5

Exemplu:
>>> s = Student("Ana", 20)
>>> s.adauga_nota("Matematica", 11) -> "Notă invalidă!"
>>> s.adauga_nota("Matematica", 8)
>>> s.adauga_nota("Matematica", 9) -> "Materia există deja!"
>>> s.calculeaza_media()
>>> s.afiseaza_situatie()
"""
# class Student:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#         self.note = {}
#     def adauga_nota(self, materia, nota):
#         print(materia, nota)
#         if nota > 10 or nota < 1:
#             return "Nota invalida"
#         elif materia in self.note:
#             return "Materia exista deja"
#         else:
#             self.note[materia] = nota
#             print(f"A fost adaugata nota:{nota} la {materia} pentru studentul {self.nume}")
#         print(self.note,"&&&&&&")
#     def calculeaza_media(self):
#         return round(sum(self.note.values())/len(self.note), 2)
#     def adauga_situatie(self):
#         res = f"Studentul {self.nume} cu varsta {self.varsta} \n"
#
#         res+= "Situatia curenta.\n"
#         for materia, nota in self.note.items():
#             res+= f" {materia}: {nota}\n"
#
#             res+= f"Media totala {self.calculeaza_media()}\n"
#             return res
#
#
# s = Student("Ana", 20)
# print(s.note,"#########")
# print(s.adauga_nota("Matematica", 11))
# s.adauga_nota("Matematica", 11)
# print(s.adauga_nota("Romana", 8))
# s.adauga_nota("Romana", 8)
# print(s.adauga_nota("Bio", 9))
# s.adauga_nota("Bio", 9)
# print(s.note,"XXXXXXXXXX")
# print(s.calculeaza_media())
# print(s.adauga_situatie())
"""
# =====================================================================

# Exersare aditionala

# =====================================================================
"""


"""
Sistem de Comenzi Restaurant

Creați o clasă Comanda care gestionează comenzile dintr-un restaurant folosind un stoc global.
Stocul conține produse cu nume, preț și cantitate disponibilă.

Clasa trebuie să:
1. Permită adăugarea produselor cu verificarea stocului
2. Actualizeze automat stocul la adăugarea produselor
3. Calculeze și afișeze nota de plată

Exemplu:
>>> cmd = Comanda(1)
>>> cmd.adauga_produs("Pizza Margherita", 2)  # True
>>> cmd.adauga_produs("Suc", 1)               # True
>>> cmd.adauga_produs("Pizza Margherita", 4)  # False (stoc insuficient)

>>> cmd.afiseaza_nota()
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

class Comanda:
    def __init__(self, nr_masa):
        self.nr_masa = nr_masa
        self.orders = {} # produs:cantitate

    def adauga_produs(self, produs, cantitate):
        in_stoc = self.is_available(produs, cantitate)
        if not in_stoc:
            print(f"Stoc insuficient, XXXXXXXXXX")
            return


        self.orders[produs] = self.orders.get(produs, 0) + cantitate
        self.actualizeaza_stoc(produs, cantitate)

    def is_available(self, produs, cantitate):
        for p in stoc:
            if p["produs"] == produs:
                return p["cantitate"] >= cantitate

    def actualizeaza_stoc(self, produs, cantitate):
        for p in stoc:
            if p["produs"] == produs:
                p["cantitate"] -= cantitate
                return

    def afiseaza_nota(self):
        total=0
        res=f"Nota masa {self.nr_masa}:\n"

        for produs, cantitate in self.orders.items():
            pret = self.afla_pretul(produs) * cantitate
            res += f"{produs}: x {cantitate}:{pret}lei\n"
            total+=pret

        res += f"Total: {total}\n"
        return res

    def afla_pretul(self, produs):
        for p in stoc:
            if p["produs"] == produs:
                return p["pret"]

cmd = Comanda(1)
cmd.adauga_produs("Pizza Margherita", 2)  # True
cmd.adauga_produs("Suc", 1)  # True
print(cmd.adauga_produs("Pizza Margherita", 4))