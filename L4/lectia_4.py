# =====================================================================

# Exercitii cu operatori aritmetici


# =====================================================================


# Exercitiul 1: Calculați suma a două numere, scădeți un al treilea număr din rezultat,
# înmulțiți cu un al patrulea număr și împărțiți totul la 2. Afișați rezultatul.
"""
Exemplu:
a = 10, b = 3, c= 5, d = 2
"""
# a = 10
# b = 3
# c= 5
# d = 2
# final = (((a+b)-c)*d)/2
# print(final)


# Exercitiul 2: Ridicați un număr la puterea 2 (pătratul unui număr) și afișați rezultatul.
"""
Exemplu:
a = 157
"""
# import math
# a = 25
# b =2
# c = math.pow(a, b)
# d = a**b
# print(c,d)


# Exercitiul 3: Verificați dacă un număr este par sau impar folosind operatorul %
# și afișați True dacă este par, altfel False.

# a = 22
# b = 2
# print(a%b == 0)


# Exercitiul 4: Calculați restul împărțirii dintre două numere și afișați rezultatul.

# var1 = 436
# var2 = 54
# rez = var1%var2
# print(f"{rez:.2f}")

# Exercitiul 5: Calculați câte zile întregi sunt într-un număr de ore dat
# (folosind împărțirea întreagă //) și afișați rezultatul.

# numarOre = 108
# oNeTimeStandart = 24
# print(f"in {numarOre} ore sunt {numarOre/oNeTimeStandart} zile")

# Exercitiul 6: Calculați câte luni complete sunt într-un număr de zile dat și afișați rezultatul.

# hours = int(input("Enter hours: "))
# print("In", hours,"sunt ",hours/24, "zile")

# =====================================================================

# Exercitii cu operatori de atribuire

# =====================================================================

# Exercitiul 1: inițializați o variabilă x cu valoarea 10 și
# adăugați 5 la valoarea sa folosind operatorul +=. Afișați rezultatul.
# x = 10
# x+=5
# print(x)


# Exercitiul 2: Declarați o variabilă z cu valoarea 8 și înmulțiți valoarea sa cu 4
# folosind operatorul *=. Afișați rezultatul.
# z=8
# z*=4
# print(z)



# Exercitiul 3:  Declarați o variabilă d cu valoarea 37 și folosiți operatorul //=
# pentru a obține rezultatul împărțirii întregi la 4. Afișați rezultatul.
# d=37
# d//=4
# print(d)


# Exercitiul 4: Verificați dacă două șiruri de caractere str1 = "hello" și str2 = "world" sunt egale.
# str1 = "hello"
# str2 = "world"
# print(str1==str2) # false
# print(len(str1)==len(str2)) # true

# Exercițiu 5: Explicați de ce următoarea linie de cod este corectă: f = (2 == 2)
"""
atribuim variabilei f unde 2==2 este adevarat / boolean
"""

# =====================================================================

# Exercitii cu operatori de logici

# =====================================================================


# Exercitiul 1: Verificați dacă un număr x este atât pozitiv, cât și par.
# Folosiți and pentru a verifica ambele condiții și afișați rezultatul.
x=4
print(x%2==0 and x>0)


# Exercitiul 2: Verificați dacă o persoană este eligibilă pentru vot.
# O persoană este eligibilă dacă are cel puțin 18 ani și este cetățean.
# Folosiți and pentru a verifica ambele condiții.
"""
Exemplu:
cetatean = True, varsta = 20
"""
# cetatean = True
# varsta = 20
# print(cetatean and varsta>18)


# Exercitiul 3: Verificați dacă o temperatură este între 20 și 30 de grade inclusiv.
# Folosiți and pentru a confirma că este în această gamă.

# t= 25
# print(t>20 and t<30)


# Exercitiul 4: Verificați dacă un student a obținut note suficiente la toate materiile pentru a promova.
# Folosiți and pentru a verifica condițiile
"""
Exemplu:
nota_mate = 7, nota_fizica = 8, nota_chimie = 6, nota_minima = 5
"""
# nota_mate = 7
# nota_fizica = 8
# nota_chimie = 6
# nota_minima = 5
# print(nota_mate >= nota_minima and nota_fizica >= nota_minima and nota_chimie >= nota_minima)

# Exercițiu 5: Verificați dacă un număr a este pozitiv sau zero.
# Folosiți or pentru a verifica cele două condiții.
# numar = 2
# print(numar>=0 or numar==0)
