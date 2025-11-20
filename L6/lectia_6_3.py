"""
# =====================================================================

# Inheritance

# =====================================================================
"""
from traceback import print_tb

from encodings.base64_codec import base64_decode

"""
Cerință:
Creați un sistem de gestionare a animalelor de companie folosind programarea orientată pe obiecte.

1. Clasa de bază Animal:
Trebuie să aibă un constructor (init) care primește:
- name (string): numele animalului
- age (int): vârsta animalului în ani

Trebuie să aibă metodele:
- get_name(): returnează numele animalului
- speak(): metodă care returneaza "Sunet generic de animal"


2. Clasele derivate trebuie să includă:
a) Clasa Dog:
    Moștenește din Animal constructor cu parametrii:
    - name (string)
    - age (int)
    * breed (string): rasa câinelui
    * is_guard_dog (boolean): dacă este câine de pază

    
b) Clasa Cat:
    Moștenește din Animal constructor cu parametrii:
    - name (string)
    - age (int)
    * color (string): culoarea blănii
    * indoor (boolean): dacă este pisică de interior
    

c) Clasa Parrot:
    Moștenește din Animal constructor cu parametrii:
    - name (string)
    - age (int)
    * can_speak_words (boolean): dacă poate vorbi cuvinte
    * favorite_phrase (string): fraza favorită (dacă poate vorbi)

- Toate clasele derivate trebuie să folosească super().init() pentru a initializa atributele din clasa părinte
- Trebuie să fie posibilă crearea unei liste cu diferite tipuri de animale și apelarea metodei speak() 
  pentru fiecare
"""

# class Animal:
#     def __init__(self, name, age):
#         self.name= name
#         self.age = age
#     def get_name(self):
#         return self.name
#     def speak(self):
#         return "Sunet generic de animal"
#
#
# class Dog(Animal):
#     def __init__(self, name, age, breed, is_guard_dog):
#         super().__init__(name, age)
#         self.breed = breed
#         self.is_guard_dog = is_guard_dog
#
#     def speak(self):
#         return "Ciine"
#
#
# class Cat(Animal):
#     def __init__(self, name, age, color, indoor):
#         super().__init__(name, age)
#         self.color = color
#         self.indoor = indoor
#
#     def speak(self):
#         return "cat"
#
#
#
# class Parrot(Animal):
#     def __init__(self, name, age, can_speak_words, favorite_phrase):
#         super().__init__(name, age)
#         self.can_speak_words = can_speak_words
#         self.favorite_phrase = favorite_phrase
#
#     def speak(self):
#         return "parrot"
#
#
#
# dog = Dog("Rex", 3, "Labrador", True)
# cat = Cat("Mitzi", 2, "portocalie", True)
# parrot = Parrot("Rico", 1, True, "Bună dimineața!")
#
# animals = [dog, cat, parrot]
#
# print("Prezentarea animalelor:")
# print("-" * 50)
# for animal in animals:
#     print(animal.speak())
#     print(f"Nume verificat prin get_name(): {animal.get_name()}")
#     print("-" * 50)

"""=================================================================================================="""

# Completează clasa Manager care moștenește Employee
# și adaugă o listă de angajați pe care îi supervizează
class Employee:
    pass



class Manager(Employee):
    pass


# manager = Manager("Ana", 5000, ["Ion", "Maria"])
# print(manager)  # Ar trebui să afișeze "Ana câștigă 5000 lei și supervizează 2 angajați"

"""=================================================================================================="""

"""
Clasa Device:
- Are un atribut brand care reprezintă marca dispozitivului.
- Atributul brand este inițializat prin constructor.

Clasa Battery:
- Are un atribut level care indică nivelul bateriei, cu valoarea de 100.
- Include o metodă check_battery() care returnează un string cu nivelul bateriei, sub forma: "Battery level: {level}%".

Clasa Phone:
- Moștenește clasele Device și Battery.
- Constructorul clasei inițializează atât marca dispozitivului (brand), cât și nivelul bateriei (level).
"""
class Device:
    pass


class Battery:
    pass



class Phone(Device, Battery):
    pass



"""
# =====================================================================

# Polymorphism

# =====================================================================
"""

"""
Suprascrie metoda speak din exercitiul anterior cu animalale.
- speak(): metodă care va fi suprascrisă de clase copil

- Trebuie să suprascrie metoda speak() pentru a returna un mesaj care include toate atributele
- Metoda speak() trebuie să returneze un string care conține toate informațiile relevante despre animal.
"""



# # Teste
# dog = Dog("Rex", 3, "Labrador", True)
# cat = Cat("Mitzi", 2, "portocalie", True)
# parrot = Parrot("Rico", 1, True, "Bună dimineața!")
# hamster = Hamster("Hami", 1, 42.5)
#
# animals = [dog, cat, parrot, hamster]
#
# print("Prezentarea animalelor:")
# print("-" * 50)
# for animal in animals:
#     print(animal.speak())
#     print(f"Nume verificat prin get_name(): {animal.get_name()}")
#     print("-" * 50)

"""=================================================================================================="""

# Suprascrie metoda get_info() din exercitiul anterior

class Employee:
    pass


class Manager(Employee):
    pass



# manager = Manager("Ana", 5000, ["Ion", "Maria"])
# print(manager.get_info())  # Ar trebui să afișeze "Ana câștigă 5000 lei și supervizează 2 angajați"

"""=================================================================================================="""

"""
Creează o ierarhie de clase pentru forme geometrice care să calculeze aria. Respectă următoarele cerințe:

Clasa Shape:
- Este o clasă de bază abstractă.
- Conține metoda area() care trebuie suprascrisă în clasele derivate.

Clasa Rectangle:
- Moștenește clasa Shape.
- Constructorul primește două atribute: width și height, care reprezintă lățimea și înălțimea dreptunghiului.
- Metoda area() calculează și returnează aria dreptunghiului (width * height).

Clasa Square:
- Moștenește clasa Rectangle.
- Constructorul primește un atribut: side, care reprezintă latura pătratului.

Clasa Circle:
- Moștenește clasa Shape.
- Constructorul primește un atribut: radius, care reprezintă raza cercului.
- Metoda area() calculează și returnează aria cercului folosind formula - π*radius**2
- Utilizează math.pi.
"""
# import math
#
# class Shape:
#     def __init__(self, latura):
#         self.latura = latura
#
# class Rectangle(Shape):
#     def __init__(self, lungime, latime):
#         super().__init__(lungime)
#         self.latime = latime
#     def area(self):
#         return self.latime * self.latura
#
# class Square(Shape):
#     def area(self):
#         return self.latura**2
#
#
# class Circle(Shape):
#     def area(self):
#         return math.pi * self.latura**2
#
#
# # Test
# rect = Rectangle(5, 3)
# print(rect.area())  # Ar trebui să afișeze 15
#
# square = Square(4)
# print(square.area())  # Ar trebui să afișeze 16
#
# circle = Circle(3)
# print(circle.area())  # Ar trebui să afișeze ~28.27

"""=================================================================================================="""

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


class Employee:
    AMOUNT_PER_PROJECT = 1000

    def __init__(self, name, employee_id, base_salary, years_of_experience):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.years_of_experience = years_of_experience

    def add_experience(self, years):
        self.years_of_experience += years
        print(f"Am adaugat la angajatul {self.name},{years} de experienta.")

    def calculate_salary(self):
        return self.base_salary + self.base_salary * 0.05 *self.years_of_experience

    def get_details(self):
        return f"Id: {self.employee_id}, Nume{self.name}"

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, years_of_experience, programming_language, projects_completed):
        super().__init__(name,employee_id,base_salary,years_of_experience)
        self.programming_language = programming_language
        self.projects_completed = projects_completed

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + self.AMOUNT_PER_PROJECT * self.projects_completed

    def get_details(self):
        base_details = super().get_details()
        details = f"Programming language :{self.programming_language}, projects completed :{self.projects_completed}\n"
        return  base_details + details

class Manager(Employee):
    def __init__ (self, name, employee_id, base_salary, years_of_experience, team_size):
        super().__init__(name, employee_id,base_salary,years_of_experience)
        self.team_size = team_size

    def add_team_member(self, employee: Developer ):
        if not isinstance(employee, Developer):
            print("Nu putem adauga in echipa")
            return
        self.team_size += 1

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary+500*self.team_size

    def get_details(self):
        base_details =super().get_details()
        return base_details +f"Marimea echipei: {self.team_size}\n"

class QATester(Employee):
    def __init__(self, name, employee_id, base_salary, years_of_experience, bugs_found):
        super().__init__(name, employee_id, base_salary, years_of_experience)
        self.bugs_found = bugs_found
        self.test_types = []

    def add_test_type(self, test_type):
        self.test_types.append(test_type)

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + 50 * self.bugs_found + 200 * len(self.test_types)

    def get_details(self):
        base_details = super().get_details()
        base_details += f"Bugs found: {self.bugs_found}\n"
        base_details += f"Test types :{self.test_types}\n"
        return base_details

# Sistem de gestionare a companiei
class ITCompany:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            return
        self.employees.append(employee)

    def calculate_total_salary(self):
        return sum(employee.calculate_salary() for employee in self.employees)

    def get_all_employees(self):
        all_details = f"Compania {self.name}"
        for employee in self.employees:
            all_details += employee.get_details()
        return all_details


company = ITCompany("TechCorp")

# Creăm dezvoltatori
dev1 = Developer("Ana Pop", "DEV001", 6000, 5, "Python", 5)
dev2 = Developer("Ion Stan", "DEV002", 5500, 3, "Java", 3)
dev1.add_experience(3)

# Creăm un manager
mgr = Manager("Maria Ionescu", "MGR001", 8000, 0, 8)
mgr.add_experience(5)
mgr.add_team_member(dev1)
mgr.add_team_member(dev2)

# Creăm un QA tester
qa = QATester("Radu Popa", "QA001", 4500, 150, 3)
qa.add_test_type("Manual Testing")
qa.add_test_type("Automation Testing")
qa.add_experience(2)

# Adăugăm toți angajații în companie
company.add_employee(dev1)
company.add_employee(dev2)
company.add_employee(mgr)
company.add_employee(qa)

# Afișăm informațiile
print(company.get_all_employees())
print(f"\nTotal salarii de plătit: {company.calculate_total_salary():.2f}")