# Exercitiu 1:
# Calculați numărul de elemente comune între două seturi
# set13_1 = {10, 20, 30, 40}
# set13_2 = {20, 30, 50, 60}
# print(f" numarul de elemente comune este: {len(set13_2.intersection(set13_1))}")
from time import process_time_ns

# Exercitiu 2:
# Aveți două seturi de studenți. Un set pentru studenții care au trecut examenul și
# altul pentru cei care nu au trecut examenul.
# Creați un nou set cu toți studenții care au trecut examenul și cei care nu l-au trecut

# set14_passed = {"Ion", "Maria", "Ana"}
# set14_failed = {"Vasile", "Elena", "George"}
# print(set14_passed.union(set14_failed))

# Exercitiu 3:
# Aveți un set cu numele produselor într-un magazin și un set cu produsele care au fost vândute.
# Afișați produsele care nu au fost vândute

# produse_in_magazin = {"laptop", "telefon", "mouse", "televizor"}
# produse_vandute = {"telefon", "mouse"}
# print(produse_in_magazin.difference(produse_vandute))

# Exercitiu 4:
# Verificați dacă există cel puțin un element comun între două seturi de hobby-uri

# hobbyuri_persona1 = {"fotbal", "muzica", "jocuri"}
# hobbyuri_persona2 = {"citit", "muzica", "calatorii"}
# print(hobbyuri_persona1.intersection(hobbyuri_persona2))

# Exercitiu 5:
# Aveți un set cu numele jucătorilor într-un echipament sportiv. Dacă un jucător nu mai face parte din echipă,
# el este eliminat din set.
# Eliminați un jucător și afișați noul set

# jucatori = {"Ion", "Maria", "George", "Vasile"}
# jucatori.remove("Maria")
# print(jucatori)

# Exercitiu 6:
# Adăugați 5 noi jucători într-un set și verificați câți jucători există acum


# jucatori = {"Ion", "Maria", "George", "Vasile"}
# noi_jucatori = ["Andrei", "Alex", "Cristian", "Mihai", "Gabriel"]
# juc_fin=set()
# juc_fin = jucatori | set(noi_jucatori)
# print(len(juc_fin))

# Exercitiu 7:
# Aveți două seturi de clienți, un set pentru clienții noi și un alt set pentru clienții vechi.
# Creați un set cu toți clienții care au fost fie noi, fie vechi
# clienti_noi = {"Ana", "Ion", "Maria"}
# clienti_vechi = {"Vasile", "Elena", "Ion"}
#
# all_set = set()
# all_set = clienti_noi | clienti_vechi  ########## ??????????????????????????????????????
# print(all_set)


# Exercitiu 8:
# Aveți un set de produse expirate și un set de produse în stoc.
# Găsiți produsele care sunt încă în stoc și care nu sunt expirate

# produse_expirate = {"lapte", "brânză", "pâine"}
# produse_in_stoc = {"lapte", "ouă", "brânză", "carne"}
# all_good = produse_in_stoc.difference(produse_expirate)
# print(all_good)




# Exercitiu 9:
# Aveți două seturi de angajați, fiecare reprezentând o echipă diferită.
# Determinați numărul de angajați care fac parte din ambele echipe și afișați numele lor.
# echipa1 = {"Ana", "Ion", "Maria", "Cristian", "George"}
# echipa2 = {"Cristian", "Vasile", "Maria", "Elena"}

# print(f"in echipa 1 sunt: {len(echipa1)} angajati,in echipa 2 sunt:{len(echipa2)} angajati, total angajati in echipe: {len(echipa1)+len(echipa2)},numele ce coincid {echipa1.intersection(echipa2)}")  ########## ????????????? loose brackets


# Exercitiu 10:
# Aveți un set de produse în stoc și un set de produse comandate de un client.
# Verificați dacă toate produsele comandate de client sunt disponibile în stoc.
produse_stoc = {"laptop", "telefon", "mouse", "televizor"}
produse_comandate = {"telefon", "mouse"}

# print(not(produse_comandate in produse_stoc))  ############3 not shure

# Exercitiu 11:
# Aveți două seturi: unul cu studenții care au completat un proiect și altul cu studenții care au dat un test.
# Afișați studenții care au făcut doar proiectul, doar testul și pe cei care au făcut ambele activități.
# studenti_proiect = {"Ana", "Ion", "George"}
# studenti_test = {"Ion", "Maria", "George", "Elena"}
#
# print(f"studentii ce au facut proiectul {studenti_proiect}")
# print(f"studentii ce au facut testul {studenti_test}")
# print(f" cei ce au facut amindoua {studenti_proiect|studenti_test}")



# Exercitiu 12:
# Aveți un set de zile în care s-a desfășurat un eveniment și un set de zile libere.
# Afișați zilele în care s-a desfășurat evenimentul și care au fost zile libere.

# zile_eveniment = {"Luni", "Miercuri", "Vineri"}
# zile_libere = {"Miercuri", "Sâmbătă", "Duminică"}
# print(f"zile cu eveniment: {", ".join(zile_eveniment)}, si zile libere: {", ".join(zile_libere)} ")

# Exercitiu 13:
# Aveți două seturi de cuvinte dintr-un text și dintr-o listă de cuvinte interzise.
# Afișați toate cuvintele din text care nu se regăsesc în lista de cuvinte interzise.

# cuvinte_text = {"programare", "Python", "exercițiu", "exemple", "restricție"}
# cuvinte_interzise = {"restricție", "exercițiu"}
# print(f"text final: {", ".join(cuvinte_text-cuvinte_interzise)}")

# Exercitiu 14:
# Aveți un set de cursuri de bază și un set de cursuri avansate. Creați un set care include doar
# cursurile care nu sunt comune.
# cursuri_baza = {"Matematică", "Fizică", "Chimie"}
# cursuri_avansate = {"Fizică", "Chimie", "Informatica", "Biologie"}
#
# print(f"sefu!, what for biologie?: {", ".join((cursuri_avansate.union(cursuri_baza)).difference(cursuri_avansate.intersection(cursuri_baza)))}")
#

# Exercitiu 15:
# Aveți un set cu numele unor prieteni și un alt set cu persoane invitate la o petrecere.
# Afișați prietenii care nu au fost invitați la petrecere.
# prieteni = {"Ion", "Maria", "George", "Elena"}
# invitati_petrecere = {"Maria", "Elena", "Vasile"}
#
# print(f"n-ai chemat pe: {", ".join(prieteni.difference(invitati_petrecere))}")
