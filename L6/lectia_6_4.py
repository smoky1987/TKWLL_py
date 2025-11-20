"""=================================================================================================="""
from platform import win32_ver

"""
Creează un sistem de gestionare a angajaților unei companii IT, cu următoarele cerințe:

Clasa de bază Employee:
    Atribute:
    - nume (name), 
    - un ID unic (employee_id), 
    - salariu de bază (base_salary)
    - număr de ani de experiență (years_of_experience), inițializat la 0.
    Metode:
    - add_experience(years): adaugă ani de experiență.
    - calculate_salary(): calculează salariul ca fiind salariul de bază plus 5% pentru fiecare an de 
                        experiență.
    - get_details(): returnează informațiile de bază ale angajatului (ID și nume).

Clasa Developer:
* Este derivată din Employee.

    Constructorul primește în plus:
    - limbajul de programare (programming_language)
    - numărul de proiecte finalizate (projects_completed)
    Suprascrie metodele: 
    - calculate_salary() pentru a include un bonus de 1000 lei pentru fiecare proiect finalizat.
    - get_details() pentru a adăuga informațiile despre limbajul de programare și numărul de 
                    proiecte finalizate.

Clasa Manager:
* Este derivată din Employee.
    Constructorul primește în plus:
    - mărimea echipei (team_size), inițial 0.
    Metode:
    - add_team_member(employee): adaugă un angajat (doar de tip Developer) în echipa managerului.
    Suprascrie metodele:
    - calculate_salary() pentru a include un bonus de 500 lei pentru fiecare membru al echipei.
    - get_details() pentru a adăuga informațiile despre mărimea echipei și membrii acesteia.

Clasa QATester:
* Este derivată din Employee.
    Constructorul primește în plus:
    - numărul de bug-uri găsite (bugs_found)
    Metode:
    - add_test_type(test_type): adaugă un tip de testare la o listă de tipuri (fără duplicare).
    Suprascrie metodele: 
    - calculate_salary() pentru a include:
        - 50 lei bonus pentru fiecare bug găsit.
        - 200 lei bonus pentru fiecare tip de testare.
    - get_details() pentru a adăuga informațiile despre bug-uri găsite și tipurile de testare.

Clasa ITCompany:
    Constructorul primește
    - numele companiei (name)
    - inițializează o listă goală de angajați.
    Metode:
    - add_employee(employee): adaugă un angajat în companie.
    - calculate_total_salary(): calculează totalul salariilor tuturor angajaților.
    - display_all_employees(): afișează informațiile despre toți angajații, inclusiv detaliile și 
                               salariul fiecăruia.

Testare:
Creează obiecte de tip Developer, Manager și QATester.
Atribuie experiență, proiecte, echipe și tipuri de testare conform scenariilor date.
Adaugă angajații în companie și afișează informațiile detaliate despre fiecare, împreună cu totalul salariilor.

"""
# class Employee:
#     def __init__(self, name, employee_id, base_salary, years_of_experience):
#         self.name = name
#         self.employee_id = employee_id
#         self.base_salary = base_salary
#         self.years_of_experience = years_of_experience
#
#     def add_experience(self, years):
#         self.years_of_experience += years
#         print(f"Am adaugat la angajatul {self.name}, {years} de experienta")
#
#     def calculate_salary(self):
#         return self.base_salary + self.base_salary * 0.05 * self.years_of_experience
#
#     def get_details(self):
#         return f"Id: {self.employee_id}, Nume: {self.name}\n"
#
#
# class Developer(Employee):
#     AMOUNT_PER_PROJECT = 1000
#
#     def __init__(self, name, employee_id, base_salary, years_of_experience,
#                  programming_language, projects_completed):
#         super().__init__(name, employee_id, base_salary, years_of_experience)
#         self.programming_language = programming_language
#         self.projects_completed = projects_completed
#
#     def calculate_salary(self):
#         base_salary = super().calculate_salary()
#         return base_salary + self.AMOUNT_PER_PROJECT * self.projects_completed
#
#     def get_details(self):
#         base_details = super().get_details()
#         details = f"Programming language: {self.programming_language}, nr. of projects completed: {self.projects_completed}\n"
#         return base_details + details

# class Manager(Employee):
#     pass
#
# class QATester(Employee):
#     pass
#
# # Sistem de gestionare a companiei
# class ITCompany:
#     pass

# # Test
# company = ITCompany("TechCorp")
#
# # Creăm dezvoltatori
# dev1 = Developer("Ana Pop", "DEV001", 6000, "Python", 5)
# dev2 = Developer("Ion Stan", "DEV002", 5500, "Java", 3)
# dev1.add_experience(3)
#
# # Creăm un manager
# mgr = Manager("Maria Ionescu", "MGR001", 8000, 0)
# mgr.add_experience(5)
# mgr.add_team_member(dev1)
# mgr.add_team_member(dev2)
#
# # Creăm un QA tester
# qa = QATester("Radu Popa", "QA001", 4500, 150)
# qa.add_test_type("Manual Testing")
# qa.add_test_type("Automation Testing")
# qa.add_experience(2)
#
# # Adăugăm toți angajații în companie
# company.add_employee(dev1)
# company.add_employee(dev2)
# company.add_employee(mgr)
# company.add_employee(qa)
#
# # Afișăm informațiile
# company.display_all_employees()
# print(f"\nTotal salarii de plătit: {company.calculate_total_salary():.2f}")
"""=================================================================================================="""

"""
Creează un sistem de gestionare a unui magazin online de instrumente muzicale, cu următoarele cerințe:

Clasa de bază Instrument:
   Atribute:
   - nume (name)
   - ID unic (instrument_id) 
   - preț (price)
   - ratings []
   - rating (0-5 stele, inițial 0)
   Metode:
   - add_rating(stars): adaugă un rating nou și recalculează media
   - apply_discount(percent): aplică un discount la preț
   - get_info(): returnează detaliile de bază

Clasa StringInstrument:
* Moștenește din Instrument
   Atribute adiționale:
   - tip corzi (string_type)
   - număr corzi (string_count)
   - material (wood_type)
   - last_maintenance (number of months)
   Metode:
   - change_strings(): resetează data ultimei schimbări
   - needs_maintenance(): returnează true dacă au trecut >6 luni de la ultima întreținere
   Suprascrie:
   - get_info() pentru a include detaliile specifice

Clasa WindInstrument:
* Moștenește din Instrument  
   Atribute adiționale:
   - material (material)
   - tip (type: woodwind/brass)
   - nivel dificultate (difficulty: 1-5)
   Metode:
   - clean(): marchează instrumentul ca fiind curățat
   - needs_cleaning(): verifică dacă au trecut >3 luni de la ultima curățare
   Suprascrie:
   - get_info() pentru a include specificațiile

Clasa PercussionInstrument:
* Moștenește din Instrument
   Atribute adiționale:
   - dimensiune (size)
   - tip (type: drums/cymbals/etc)
   - accesorii incluse (accessories)
   Metode:
   - add_accessory(item): adaugă un accesoriu nou
   - replace_parts(): actualizează data ultimei înlocuiri
   Suprascrie:
   - get_info() pentru detaliile complete

Clasa MusicStore:
   Atribute:
   - nume magazin (store_name)
   - locație (location)
   - inventar (inventory)
   Metode:
   - add_instrument(instrument): adaugă în inventar
   - remove_instrument(id): elimină din inventar
   - search_by_type(type): returnează instrumentele de tipul specificat
   - apply_sale(type, discount): aplică reducere pentru o categorie
   - get_inventory_value(): calculează valoarea totală
   - get_best_rated(): returnează top 5 instrumente după rating

Cerințe testare:
- Creează diverse instrumente din fiecare categorie
- Adaugă-le în magazin și aplică operații de întreținere
- Testează funcționalitățile de căutare și reduceri
- Verifică calculul corect al valorii inventarului
"""


class Instrument:
    def __init__(self, name: str, instrument_id: int,  price: float, ratings: list=None):
        self.name = name
        self.instrument_id = instrument_id
        self.price = price
        self.ratings = ratings if ratings else []
        self.rating = sum(ratings) / len(ratings) if ratings else 0

    def add_rating(self, rating: float):
        self.ratings.append(rating)
        return sum(self.ratings) / len(self.ratings)

    def apply_discount(self, percent: float):
        self.price -= (percent * self.price)

    def __str__(self):
        return f"{self.name} {self.price:.2f} {self.rating:.2f}\n"

class StringInstrument(Instrument):
    def __init__(self, name: str, instrument_id:int, price:float,
                 type: str, string_count:int,wood_type:str,
                 nr_months:int,ratings:list=None):
        super().__init__(name,instrument_id,price,ratings)
        self.type = type
        self.string_count = string_count
        self.wood_type = wood_type
        self.nr_months = nr_months

    def change_strings(self):
        self.nr_months = 0

    def needs_maintenance(self):
        self.nr_months > 6

    def __str__(self):
        info = super().__str__()
        info += f"{self.type} {self.string_count} {self.wood_type}\n"
        info += f" {self.nr_months} {self.needs_maintenance()}\n"
        return info

class WindInstrument(Instrument):
    def __init__(self, name: str, instrument_id: int,  price: float,
                 material: str, type: str, difficulty: int,
                 nr_months:int, ratings: list=None):
        super().__init__(name, instrument_id, price, ratings)
        self.material = material
        self.type = type
        self.difficulty = difficulty
        self.nr_months = nr_months

    def clean(self):
        self.nr_months = 0

    def needs_cleaning(self):
        return self.nr_months > 3

    def __str__(self):
        info = super().__str__()
        info += f"{self.material} {self.type} {self.difficulty}\n"
        info += f" {self.nr_months} {self.needs_cleaning()}\n"
        return info

class PercussionInstrument(Instrument):
    def __init__(self, name: str, instrument_id:int, price:float,size:int, type:str, accessories:str,
                 nr_months:int,ratings:list=None):
        super().__init__(name,instrument_id,price,ratings)
        self.size = size
        self.type = type
        self.accessories = accessories
        self.nr_months = nr_months

    def add_accessory(self, item):
        self.accessories.append(item)

    def replace_parts(self):
        self.nr_months = 0

    def __str__(self):
        info = super().__str__()
        info += f"{self.size} {self.type} {self.accessories}\n"
        info += f"{self.nr_months}"
        return info

class MusicStore:
    def __init__(self, store_name:str, location, inventory=None):
        self.store_name = store_name
        self.location = location
        self.inventory = inventory if inventory else []

    def add_instrument(self, instrument:Instrument):
        self.inventory.append(instrument)

    def remove_instrument(self, id:int):
        for instrument in self.inventory:
            if instrument.id == id:
                self.inventory.remove(instrument)
                print(f"sa sters {instrument.name} cu id: {instrument.id}")

    def apply_sale(self, type:str, discount:float):
        for instrument in self.inventory:
            if instrument.type == type:
                instrument.apply_discount(discount)

    def get_inventory(self):
        return sum(instrument.price for instrument in self.inventory)

    def get_best_rated(self):
        return sorted(self.inventory, key=lambda instrument: instrument.rating, reverse=True)[:5]


myMusicInstrumentStore = MusicStore("Best Melody","Alfonso strasse, 12")

si1 = StringInstrument("Violin",instrument_id=1,
                          price=12000,type="wood",string_count=5,wood_type="Apple",nr_months=1)
si1.add_rating(1)
si2 = StringInstrument("Celoo",instrument_id=2,
                         price=11000,type="wood",string_count=6,wood_type="Oak",nr_months=2)
si2.add_rating(5)
si3 = StringInstrument("Guitar", instrument_id=3,
                          price=10000,type="wood",string_count=7,wood_type="Pine",nr_months=3)
si3.add_rating(4)

wi1 = WindInstrument("Flaute",instrument_id=1,
                     price = 500, material = "wood", type= "wood",difficulty=2,nr_months=1)
wi1.add_rating(8)
wi2 = WindInstrument("Harmonica",instrument_id=2,
                     price = 600, material = "brass", type= "brass",difficulty=3,nr_months=2)
wi2.add_rating(9)
wi3 = WindInstrument("Nai",instrument_id=3,
                     price = 700, material = "wood", type= "wood",difficulty=4,nr_months=1)
wi3.add_rating(2)
pi1 = PercussionInstrument("Drum", instrument_id = 1, price =3000, size =2, type = "Drum", accessories="None",
                 nr_months=2)
pi1.add_rating(3)
pi2 = PercussionInstrument("Cymbal", instrument_id = 2, price =4000, size =2, type = "Cymbal", accessories="None",
                 nr_months=3)
pi2.add_rating(6)
pi3 = PercussionInstrument("Marimba", instrument_id = 3, price =5000, size =2, type = "Marimba", accessories="None",
                 nr_months=4)
pi3.add_rating(6)


myMusicInstrumentStore.add_instrument(si1)
myMusicInstrumentStore.add_instrument(si1)
myMusicInstrumentStore.add_instrument(si1)
myMusicInstrumentStore.add_instrument(wi1)
myMusicInstrumentStore.add_instrument(wi1)
myMusicInstrumentStore.add_instrument(wi1)
myMusicInstrumentStore.add_instrument(pi1)
myMusicInstrumentStore.add_instrument(pi1)
myMusicInstrumentStore.add_instrument(pi1)

print(myMusicInstrumentStore.get_inventory())
print(myMusicInstrumentStore.get_best_rated())
