"""
Tema pentru acasă: Moștenirea și Polimorfismul în Python

Cerințe:
Creați un proiect care să îmbine noțiunile de moștenire și polimorfism. Respectați pașii de mai jos pentru
 a implementa o aplicație simplă de gestionare a vehiculelor și a caracteristicilor acestora.

1. Clasa de bază Vehicle
Definiți clasa de bază Vehicle cu următoarele atribute:
- brand (string): marca vehiculului.
- model (string): modelul vehiculului.
- year (int): anul de fabricație.
Adăugați metoda:
- get_info(): Returnează un string cu toate informațiile despre vehicul în formatul:
"{brand} {model}, fabricat în anul {year}".

2. Clase derivate
a) Clasa Car
    Moștenește clasa Vehicle.
    Constructorul primește:
        - Toate atributele din clasa Vehicle.
        - fuel_type (string): tipul de combustibil (ex.: benzină, motorină, electric).
        - doors (int): numărul de uși.
    * Suprascrie metoda get_info() pentru a include și fuel_type și doors.
    Exemplu de mesaj returnat:
    "Tesla Model S, fabricat în anul 2022, electric, cu 4 uși."

b) Clasa Bicycle
    Moștenește clasa Vehicle.
    Constructorul primește:
        - Toate atributele din clasa Vehicle.
        - type (string): tipul bicicletei (ex.: șosea, MTB, pliabilă).
        - gear_count (int): numărul de viteze.
    * Suprascrie metoda get_info() pentru a include type și gear_count.
    Exemplu de mesaj returnat:
    "Merida Crossway, fabricat în anul 2021, tip: șosea, cu 21 viteze."

c) Clasa Motorcycle
    Moștenește clasa Vehicle.
    Constructorul primește:
        - Toate atributele din clasa Vehicle.
        - engine_capacity (int): capacitatea motorului (cm³).
        - has_sidecar (bool): dacă motocicleta are sau nu ataș.
    * Suprascrie metoda get_info() pentru a include engine_capacity și has_sidecar.
    Exemplu de mesaj returnat:
    "Honda Shadow, fabricat în anul 2020, motor de 745 cm³, fără ataș."

3. Cerințe suplimentare
Creați o listă de vehicule care să includă cel puțin câte un exemplu din fiecare
clasă (Car, Bicycle, Motorcycle).
Parcurgeți lista și afișați informațiile pentru fiecare vehicul utilizând metoda get_info().
"""



class Vehicle:
    def __init__(self, brand:str, model:str, year:int):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model}, fabricat în anul {self.year}\n"

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type:str, doors:int):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def get_info(self):
        return f"{self.brand} {self.model}, fabricat în anul{self.year},motor {self.fuel_type},cu {self.doors} usi\n"


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type:str, gear_count:int):
        super().__init__(brand, model, year)
        self.type = type
        self.gear_count = gear_count

    def get_info(self):
        return f"{self.brand}{self.model}, fabricat în anul{self.year},tip: {self.type} cu numar de viteze: {self.gear_count}\n"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity: int, has_sidecar: bool):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{self.brand} {self.model}, fabricat în anul{self.year},Vol motor: {self.engine_capacity} motocicleta are sau nu ataș: {self.has_sidecar}\n"

v= Vehicle
masina = Car("Tesla","Model S",2022, "electric", 4)
bicicleta = Bicycle("Merida","Crossway",2021, "șosea", 21)
motocicleta= Motorcycle("Honda", "Shadow", 2020, 745, False)

print(masina.get_info())
print(bicicleta.get_info())
print(motocicleta.get_info())
