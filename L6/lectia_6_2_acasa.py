"""
Temă: Implementarea unui Sistem de Playlist-uri Muzicale

Creați o clasă Playlist care va gestiona o colecție de melodii.
Clasa trebuie să suporte operațiile de bază pentru gestionarea unui playlist muzical.

Pentru fiecare melodie trebuie să păstrați:
- Titlul
- Artistul
- Durata (în secunde)

Implementați obligatoriu:
__str__ pentru afișarea frumoasă a playlist-ului
__repr__ pentru afișarea tehnică a tuturor detaliilor
@staticmethod pentru validări și conversii de timp

Bonus pentru:
1. Sortare melodii (după artist, titlu sau durată)
2. Căutare melodii
3. Filtrare melodii (ex: doar melodii sub 4 minute)
4. Statistici (ex: artist cu cele mai multe melodii)

Se evaluează:
1. Folosirea corectă a __str__ și __repr__
2. Implementarea metodelor statice
3. Validări implementate
4. Organizarea codului
5. Claritatea implementării
"""

class Playlist:
    def __init__(self, ):
        # nume playlist
        # lista de melodii (fiecare melodie e dict cu artist, titlu, durata)
        pass

    def __str__(self):
        # Afișare frumoasă:
        # "Playlist: Summer Hits | 12 melodii | Durată totală: 45:30"
        pass

    def __repr__(self):
        # Afișare tehnică cu toate melodiile și detaliile
        pass

    def valideaza_melodie(self):
        # artist - minim 2 caractere
        # titlu - minim 3 caractere
        # durata - în secunde, între 30 și 600
        pass

    def converteste_durata(self):
        # Convertește durata din secunde în format "mm:ss"
        # Ex: 185 -> "3:05"
        pass

    def adauga_melodie(self):
        # Adaugă o melodie nouă în playlist
        # Folosește validarea statică
        pass

    def sterge_melodie(self):
        # Șterge o melodie după titlu
        pass

    def amesteca(self):
        # Amestecă aleatoriu melodiile
        pass

    def durata_totala(self):
        # Returnează durata totală în secunde
        pass


"""
Exemplu de utilizare:
# Creare playlist
playlist = Playlist("Summer Hits")

# Adăugare melodii
playlist.adauga_melodie("Queen", "Bohemian Rhapsody", 354)
playlist.adauga_melodie("The Beatles", "Hey Jude", 431)
playlist.adauga_melodie("Pink Floyd", "Time", 425)

# Afișare playlist
print(playlist)  # "Playlist: Summer Hits | 3 melodii | Durată totală: 20:10"

# Conversie durată
print(Playlist.converteste_durata(354))  # "5:54"

# Ștergere melodie
playlist.sterge_melodie("Time")
print(playlist)  # "Playlist: Summer Hits | 2 melodii | Durată totală: 13:05"
"""