# Tema pentru acasă - Input, Print
from dis import pretty_flags

# Exercițiul 1 - Afișează un mesaj care folosește variabile pentru temperatura într-un oraș,
# creând doua variabile oras si temperatura

# oras = "Chisinau"
# temperatura = 17
# print("In orasul " +oras+", temperatura este: "+str(temperatura)+"\u00b0"+"C" )


# Exercițiul 2 - Folosește .format() pentru a afișa distanța dintre două orașe.
# oras1 = "Bangladesh"
# oras2 ="Chicago"
# distanta = 3000
# print("distanta dintre: {} si {} este {} mile".format(oras1,oras2,distanta))


# Exercițiul 3 - Folosește f-string pentru a afișa raportul între două numere,
# creând doar doua variabile.
# v1 = 22
# v2 = 11
# print(f"Raportul dintre {v1} si {v2} este {v1/v2}")

# Exercițiul 4 - Afișează prețul unui produs după aplicarea unui discount folosind .format().
# produs = "sosete"
# pret_initial = 37
# discount = 5
# pret_final = pret_initial - (pret_initial * (5/100))
# print(f"{produs}le costa {pret_final}")




# Exercițiul 5 - Folosește f-string pentru a afișa volumul unui cub cu latura, citita de la tastatura
# latura = float(input("Lungimea laturei: "))
# print(f"volumul cubului este {latura**3} uc")


# Exercițiul 6 - Afișează timpul total de lucru după n zile folosind .format().
# ore_pe_zi =8
# zile =22
# ore_totale = ore_pe_zi * zile
# print("timpul total de lucru: {} ore".format(ore_totale))



# Exercițiul 7 - Folosește f-string pentru a calcula și afișa procentul de rezolvare a unor exerciții.
# nr_ex_total = 30
# nrExRezolvate = float(input("numarul ex rezolvate: "))
# print(f"procentul de indeplinire {(nrExRezolvate*100)/nr_ex_total:.2f} %")


# Exercițiul 8 - Folosește .format() pentru a afișa prețul final al unui produs cu TVA.

# prets = float(input("Ce pret are produsul? "))
# pretFinal = prets+prets/5     #presupunem ca TVA e 20%
# print("Pretul cu TVA este: {} talere ".format(pretFinal))
# print("Pretul cu TVA este: {} talere ".format(prets+prets/5))

# Exercițiul 9 - Folosește f-string pentru a afișa vârsta pe care o vei avea în 10 ani.
# 1.folosim functia input pentru a afla virsta curenta

# virsta = int(input("Ce virsta ai?: "))
# print(f"Peste zecce ani vei avea {virsta+10} ani")

# Exercițiul 10 - Calculează și afișează suma și media a trei numere folosind f-string,
# citite de la tastatura.
# nr_1 = int(input("Nr_1:"))
# nr_2 = int(input("Nr_2:"))
# nr_3 = int(input("Nr_3:"))
# suma = nr_1 + nr_2 + nr_3
# media = suma / 3
#
# print(f"Suma numerelor este: {suma}")
# print(f"Media numerelor este: {media}")

