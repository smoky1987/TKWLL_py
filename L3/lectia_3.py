# Exercitii cu functia .index()
# Exercitiu 1: Găsește poziția primei apariții a literei 'a' într-un șir de caractere.
# sir = "Exemplificare"
# Răspunsul tau mai jos:

from operator import index
# sir = "Exemplificare"
# print(sir.index("a"))
##############################################
# a = "Slaut"
# print(isinstance(a,str))
# print(type(a))


##############################################




# Exercitiu 2: Găsește poziția literei 'z' într-un șir de caractere dat.
# sir2 ="Python este interesant"
# Răspunsul tau mai jos:
# print(sir2.index("z")) #Da eroare! in stringul de baza nu este z
# print(sir2.find("z"))

# Exercitiu 3: Găsește poziția unui subșir într-un șir de caractere.
# sir3 = "Acesta este un test."
# Răspunsul tau mai jos:
# substring = "este"
# print(f"Substring: {substring} se afla pe pozitia {sir3.index(substring)} in stringul {sir3}")

# Exercitiu 4: Utilizează funcția index() pentru a găsi poziția unei litere și folosește această poziție pentru a tăia șirul în două.
# sir4 = "Divizare"
# litera = "z"
# Răspunsul tau mai jos:
# print(sir4.index(litera), sir4.split(litera))



# Exercitiu 5: Caută prima apariție a literei 'i' într-un șir și
# printează partea din șir care începe de la acea literă.
# sir5 = "Identificare"
# Răspunsul tau mai jos:
# subst = sir5.find("i")
# val1 = int(subst)
# val2 = int(len(sir5)-int(subst))
# print(sir5[val1:])
# =====================================================================


# =====================================================================
# Exercitii cu functia .count()
# Exercitiu 1: Numără câte ori apare litera 'a' într-un șir de caractere.
# sir = "ana are mere."
# Răspunsul tau mai jos:
# print(f"litera 'a' se afla de atitea ori {sir.count("a")} ori in '{sir}'")

# Exercitiu 2: Numără câte ori apare litera 'e' într-un șir de caractere.
# sir2 = "Elefantul este mare."
# Răspunsul tau mai jos:
# print("Litera 'e' apare de {ori} ori in fraza '{sir}' ".format(sir=sir2,ori=sir2.count("e") ))


# Exercitiu 3: Numără câte ori apare subșirul 'are' într-un șir de caractere.
# sir3 = "Mara are o pisica care are blana."
# Răspunsul tau mai jos:
# print(sir3.count("are"))

# Exercitiu 4: Numără câte ori apare litera 'i' într-un șir de caractere.
# sir4 = "Informatica este interesanta."
# Răspunsul tau mai jos:
# print(sir4.count("i")) #2 ori
# print((sir4.lower()).count("i")) #3 ori


# Exercitiu 5: Numără câte ori apare litera 's' într-un șir de caractere.
# sir5 = "Soseaua suspinelor."
# Răspunsul tau mai jos:
# print(sir5.count("s"))  # 3 ori // print(f" Litera 's' apare de {sir5.count("s")} ori")
# print((sir5.lower()).count("s")) # 4 ori


# =====================================================================


# =====================================================================

# Exercitii cu functia .find()
# Exercitiu 1: Găsește poziția primei apariții a literei 'a' într-un șir de caractere.
# sir = "Ana are mere."
# Răspunsul tau mai jos:
# print(sir.find("a"))

# Exercitiu 2: Găsește poziția primei apariții a literei 'e' într-un șir de caractere.
# sir2 = "Elefantul este mare."
# Răspunsul tau mai jos:
# print(sir2.find("e"), sir2[sir2.find("e")])


# Exercitiu 3: Găsește poziția primei apariții a subșirului 'are' într-un șir de caractere.
# sir3 = "Mara are o pisica care are blana."
# Răspunsul tau mai jos:
# print("Incepe din pozitia {} !".format(sir3.index("are")))

# Exercitiu 4: Găsește poziția primei apariții a literei 'i' într-un șir de caractere.
sir4 = "Informatica este interesanta."
# Răspunsul tau mai jos:


# Exercitiu 5: Găsește poziția primei apariții a literei 's' într-un șir de caractere.
#sir5 = "Soseaua suspinelor."
# Răspunsul tau mai jos:
#print(sir5.index("s"))
# =====================================================================


# =====================================================================
# Exercitii cu functia .lower()
# Exercitiu 1: Converteste un șir de caractere la litere mici.
# sir = "ANA ARE MERE."
# Răspunsul tau mai jos:
# print(sir.lower())



# Exercitiu 2: Converteste numele unei zile din săptămână la litere mici.
# ziua = "LUNI"
# Răspunsul tau mai jos:
# print(ziua.lower())
# print(ziua.swapcase())


# Exercitiu 3: Converteste un titlu de carte la litere mici.
# titlu = "Mica Sirena"
# Răspunsul tau mai jos:
# print(titlu.lower())


# Exercitiu 4: Converteste un enunț la litere mici.
# enunt = "Python Este Interesant!"
# Răspunsul tau mai jos:
# print(enunt.lower())
# print(enunt.casefold())


# Exercitiu 5: Converteste numele unei țări la litere mici.
# tara = "ROMANIA"
# Răspunsul tau mai jos:
# print(tara.lower())
# print(tara.casefold())
# print(tara.swapcase())
# ======================================


# =====================================================================
# Exercitii cu functia .upper()
# Exercitiu 1: Converteste un șir de caractere la litere mari.
# sir = "ana are mere."
# Răspunsul tau mai jos:
# print(sir.upper())
# print(sir.swapcase())

# Exercitiu 2: Converteste numele unei zile din săptămână la litere mari.
# ziua = "marti"
# Răspunsul tau mai jos:
# print(ziua.upper())
# print(ziua.swapcase())

# Exercitiu 3: Converteste un titlu de carte la litere mari.
# titlu = "Mica Sirena"
# Răspunsul tau mai jos:
# print(titlu.upper())


# Exercitiu 4: Converteste un enunț la litere mari.
# enunt = "Python este interesant!"
# Răspunsul tau mai jos:
# print(enunt.upper())


# Exercitiu 5: Converteste numele unei țări la litere mari.
# tara = "romania"
# Răspunsul tau mai jos:
# print(tara.capitalize())
# print(tara.swapcase())
# print(tara.upper())
# =====================================================================


# =====================================================================
# Exercitii cu functia .replace()
# Exercitiu 1: Înlocuiește 'ana' cu 'Ana' într-un șir de caractere.
# sir = "ana are mere."
# print(sir.capitalize())
# print(sir.replace("ana","Ana"))


# Exercitiu 2: Înlocuiește 'este' cu 'nu este' într-un șir de caractere.
# sir2 = "El este acasă."
# Răspunsul tau mai jos:
# print(sir2.replace("este", "nu este"))

# Exercitiu 3: Înlocuiește 'alb' cu 'negru' într-un șir de caractere.
# sir3 = "Zăpada este albă."
# Răspunsul tau mai jos:
# print(sir3.replace("alb", "negră"))

# Exercitiu 4: Înlocuiește 'frig' cu 'cald' într-un șir de caractere.
# sir4 = "Afară este frig."
# Răspunsul tau mai jos:
# print(sir4.replace("frig", "cald"))

# Exercitiu 5: Înlocuiește 'pisica' cu 'câinele' într-un șir de caractere.
# sir5 = "pisica doarme pe canapea."
# Răspunsul tau mai jos:
# print(sir5.replace("pisica", "câinele"))

# =====================================================================

"""
Indexarea[start(inclusiv) : stop(exclusiv)]

default start: 0
default end: len()

"""


# =====================================================================
# Exercitii cu string slicing
# Exercitiu 1: Obține primele 5 caractere dintr-un șir de caractere.
# sir = "Programarea este distractivă."
# Răspunsul tau mai jos:
# print(sir[:5])

# Exercitiu 2: Obține ultimele 4 caractere dintr-un șir de caractere.
# sir2 = "Hello, world!"
# Răspunsul tau mai jos:
# print((sir2[:-5:-1])[::-1])

# Exercitiu 3: Obține caracterele de la poziția 3 inclusiv la poziția 7 inclusiv dintr-un șir.
# sir3 = "Învățăm programarea cu Python."
# Răspunsul tau mai jos:
# print(sir3[3:7:])

# Exercitiu 4: Obține fiecare al doilea caracter dintr-un șir.
# sir4 = "abcdefg"
# Răspunsul tau mai jos:
# print(sir4[1::2])


# Exercitiu 5: Inversează un șir de caractere folosind slicing.
# sir5 = "abcde"
# Răspunsul tau mai jos:
# print(sir5[::-1])

# Exercitii cu functia .lower()
# Exercitiu 1: Converteste un șir de caractere la litere mici.
# sir = "ANA ARE MERE."
# # Răspunsul tau mai jos:
# print(sir.lower())
# =====================================================================

