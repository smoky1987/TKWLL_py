# =====================================================================

# Exercitii cu operatori aritmetici

# =====================================================================


# Exercitiul 1: Găsiți produsul a trei numere,
# adunați un al patrulea număr și împărțiți rezultatul la 3. Afișați rezultatul.
"""
Exemplu:
a = 10, b = 3, c= 5, d = 2
"""
# a = 10
# b = 3
# c= 5
# d = 2
# print(((a*b*c)+d)/3)

# Exercitiul 2: Calculați valoarea unei expresii de tipul a^b( a la puterea lui b)
# (unde a și b sunt valori introduse de utilizator) și afișați rezultatul.

# var1 = int(input("Enter the first number: "))
# var2 = int(input("Enter the second number: "))
# print(pow(var1, var2))


# Exercitiul 3: Verificați dacă un număr este divizibil cu 3 și afișați True sau False în funcție de rezultat.
# var1 = int(input("Enter the first number: "))
# print(var1%3 == 0)

# Exercitiul 4: Verificați dacă un număr este divizibil atât cu 2, cât și cu 5.
# Afișați True dacă este divizibil cu ambele.
# var1 = int(input("Enter the first number: "))
# div1 = 2
# div2 = 5
# print(var1%div1==0 and var1%div2==0)



# Exercitiul 5: Determinați câte pachete de câte 6 articole se pot face dintr-un număr de articole dat,
# folosind operatorul //, și afișați rezultatul.
# var1 = int(input("articole : "))
# print(var1//6)

# Exercitiul 6: Determinați câți ani întregi sunt într-un număr de luni dat și afișați rezultatul.
# var1 = int(input("luni ?: "))
# var2 = 12 # luni
# print(var1//12, "ani")

# =====================================================================

# Exercitii cu operatori de atribuire

# =====================================================================


# Exercitiul 1: Inițializați o variabilă y cu valoarea 20 și
# scădeți 3 din valoarea sa folosind operatorul -=. Afișați rezultatul..
# x = 20
# x-=3
# print(x)


# Exercitiul 2: Inițializați o variabilă a cu valoarea 50 și împărțiți valoarea
# sa la 5 folosind operatorul /=. Afișați rezultatul.
#
# y = 50
# y/=5
# print(y)


# Exercitiul 3: Inițializați o variabilă c cu valoarea 13 și aplicați operatorul
# de rest (%=) pentru a obține restul împărțirii la 5. Afișați rezultatul.
# c = 13
# c%=5
# print(c)


# Exercitiul 4: Inițializați o variabilă e cu valoarea 5, adăugați 10 la valoarea
# sa folosind +=, apoi folosiți *= pentru a o înmulți cu 3 și afișați rezultatul final.

# e = 5
# e+=10
# e*=3
# print(e)

# =====================================================================

# Exercitii cu operatori de atribuire

# =====================================================================


# Exercitiul 1: Verificați dacă un număr y este fie mai mic de 0, fie mai mare de 100.
# Folosiți or pentru a verifica una dintre condiții.
# ff = int(input("Enter a number: "))
# print(ff<0 or ff>100)



# Exercitiul 2:Verificați dacă o persoană este fie adult (18 ani sau mai mult),
# fie minor (sub 18 ani).
# Folosiți or pentru a verifica una dintre condiții.

# ff = int(input("Virsta por-favor: "))
# etanol = 18
# print(ff<etanol or ff>etanol)


# Exercitiul 3: Verificați dacă un număr z nu este un multiplu de 5. Folosiți not pentru a nega condiția.

# z = 635463
# print(z%5!=0)


# Exercitiul 4: Verificați dacă o persoană nu este nici tânără (sub 18 ani), nici bătrână (peste 65 de ani).
# Folosiți not pentru a verifica ambele condiții.

# virsta = int(input("virsta = "))
# c1 = not virsta <18
# c2 = not virsta > 65
# print(c1 and c2)



# Exercițiu 5: Verificați dacă un cuvânt este fie "Python", fie "Java".
# Folosiți or pentru a verifica cele două condiții.
# wrd = input("Enter the word Python or Java: ")
# w1 = "JAVA"
# w2 = "PYTHON"
# print(wrd.upper() == w1 or wrd.upper() == w2)
