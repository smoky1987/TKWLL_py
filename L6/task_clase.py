"""
Task: Sistem de Management al unei Biblioteci

Timp alocat: 15-20 minute

Creați următoarele clase pentru a gestiona o bibliotecă:

1. Clasa Book:
   - Atribute: title, author, year, isbn
   - Metodele __str__ și __repr__
   - O staticmethod care validează ISBN-ul (trebuie să aibă 13 cifre)

2. Clasa Library:
   - Moștenește o clasă de bază Building (cu atribute: address, floors)
   - Atribute adiționale: books (listă), staff (listă)
   - Metode pentru:
     * adăugare carte
     * căutare carte după ISBN
     * afișare toate cărțile unui autor

Bonus:
- Implementați o metodă de sortare a cărților după anul publicării
- Adăugați management al erorilor pentru ISBN invalid

Test data:
book1 = Book("Amintiri din copilărie", "Ion Creangă", 1892, "1234567890123")
book2 = Book("Luceafărul", "Mihai Eminescu", 1883, "9876543210123")
"""

# class Book:
#     def __init__(self, title, author, year, isbn):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.isbn = isbn
#
#     def __str__(self):
#         return f"{self.title}, {self.author}, {self.year}, {self.isbn}\n"
#
#     def __repr__(self):
#         return f"Title: {self.title}, Autor: {self.author}, Year: {self.year}, ISBN: {self.isbn}\n"
#
#     @staticmethod
#     def validate(isbn):
#         return int(str(isbn)[0])>0 and len(str(isbn)) == 13
#
# class Building:
#     def __init__(self, address, floors):
#         self.address = address
#         self.floors = floors
#
#
# class Library(Building):
#     def __init__(self, address, floors, books=None, staff=None):
#         super().__init__(address, floors)
#         self.books = books if books is not None else []
#         self.staff = staff if staff is not None else []
#
#
#     def adauga_carte(self, carte:Book):
#         if isinstance(carte, Book):
#             self.books.append(carte)
#
#     def cauta_carte_dupa_isbn(self, isbn):
#         for book in self.books:
#             if isbn == book.isbn:
#                 return book
#         return f"Carte cu acest ISBN nu exista in Biblioteca."
#
#     def afisare_carti_a_unui_autor(self, autor):
#         carti = []
#         for book in self.books:
#             if autor == book.author:
#                 carti.append(book)
#         return carti
#
# carte = Book("Luceafarul", "Mihai Eminescu", 1850, 1200000000000000)
# book1 = Book("Amintiri din copilărie", "Ion Creangă", 1892, "1234567890123")
# book2 = Book("Luceafărul", "Mihai Eminescu", 1883, "9876543210123")
# librarie = Library("Stefan cel Mare", 4)
# librarie.adauga_carte(carte)
# librarie.adauga_carte(book1)
# librarie.adauga_carte(book2)
# print(librarie.cauta_carte_dupa_isbn(carte.isbn))
# print(librarie.afisare_carti_a_unui_autor("Mihai Eminescu"))