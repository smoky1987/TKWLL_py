"""
Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
Utilizați list comprehension.
"""

# CODUL TĂU VINE MAI JOS:
# def task_1():
#     return [print(i) for i in range(1, 11)]
# # CODUL TĂU VINE MAI SUS:
# task_1()
"""
Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
Utilizați list comprehension în proces
"""

# CODUL TĂU VINE MAI JOS:
# def task_2():
#     return [print(i**2) for i in range(1, 11)]
# # CODUL TĂU VINE MAI SUS:
# task_2()
"""
Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
Utilizați list comprehension în proces.
"""

# CODUL TĂU VINE MAI JOS:
# def task_3():
#     return [print(i) for i in range(1, 11) if i%2!=0]
# # CODUL TĂU VINE MAI SUS:
# task_3()
"""
Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum 
[[1, 2], [3, 4], [5, 6]]
va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , 
adică [1, 2, 3, 4, 5, 6]
"""

# CODUL TĂU VINE MAI JOS:
# def task_4(data):
#     myArr=[]
#     for i in data:
#         for j in i:
#             myArr.append(j)
#     print(myArr)
# # CODUL TĂU VINE MAI SUS:
# task_4([[1, 2], [3 , 4], [5, 6]])
"""
Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până n (inclusiv n).
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
"""

# CODUL TĂU VINE MAI JOS:
# def task_5(n):
#     return [print('par')if i%2==0 else print('impar') for i in range(1, n)]
# # CODUL TĂU VINE MAI SUS:
# task_5(101)
"""
Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care 
mappează fiecare număr de la 1 la 5 la cubul său.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# CODUL TĂU VINE MAI JOS:
# def task_6(n):
#     cubDict={}
#     for i in range(1,n+1):
#         cubDict[i]=i**3
#     print(cubDict)
# # CODUL TĂU VINE MAI SUS:
# task_6(8)
"""
Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii 
de 3 de la 1 la n, unde n este un argument al funcției.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face multiplicarea.
Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
"""

# CODUL TĂU VINE MAI JOS:
# def task_7(n):
#     myDict = {}
#     print(sorted({i*3 for i in range(1,n+1)}))
# # CODUL TĂU VINE MAI SUS:
# task_7(10)
# task_7(50)
"""
Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna 
media aritmetică a numerelor din listă.
Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
"""

# CODUL TĂU VINE MAI JOS:
# def task_8(data):
#     sum= 0
#
#     for i in data:
#         sum= sum + i
#     mean = sum / len(data)
#     return mean
# # CODUL TĂU VINE MAI SUS:
# print(task_8([1, 2, 3, 4, 5, 6, 7]))
"""
Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` 
dacă numărul este par, altfel `False`.
Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# def task_9(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
# print(task_9(2))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane 
ca argumente poziționale și orașul ca un argument opțional,
apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
"""

# CODUL TĂU VINE MAI JOS:
# def task_10(n,v,o):
#    return f"Nume: {n}, Varsta: {v}, Oras: {o}"
#
# print(task_10("Ana",32,"Bucuresti"))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_11" care acceptă o listă
 variabilă de numere și returnează valoarea maximă.
Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
"""

# CODUL TĂU VINE MAI JOS:
# def task_11(data):
#     max=0
#     for i in data:
#         if i > max:
#             max=i
#         else:
#             pass
#     print(f"max = {max}")
#
# task_11([10, 20, 30, 40, 50])
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
Exemplu: Pentru numărul 5 rezultatul va fi 120
"""

# CODUL TĂU VINE MAI JOS:
# def task_12(n):
#     factorial = 1
#     if n <= 0:
#         return 1
#     else:
#         for i in range(1, n + 1):
#             factorial = factorial * i
#     print(factorial)
#     return factorial
#
# task_12(4)
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
"""

# CODUL TĂU VINE MAI JOS:
# def task_13(n,m):
#     sum = n+m
#     prod = n*m
#     print(f"suma {sum}, produs {prod}")
#     return f"suma {sum}, produs {prod}"
#
# task_13(5,12)
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane 
și returnează textul "minor" dacă vârsta este sub 18 ani, 
"adult" dacă vârsta este între 18 și 65 ani și "senior" 
dacă vârsta este peste 65 de ani.
Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
"""

# CODUL TĂU VINE MAI JOS:
# def task_14(virsta):
#     if virsta > 65:
#         print("senior")
#         return "senior"
#     elif virsta < 18:
#         print("minor")
#         return "minor"
#     else:
#         print("adult")
#         return "adult"
#
# task_14(12)
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` 
dacă string-ul este un palindrom, altfel `False`.
Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# def task_15(info):
#     if info == info[::-1]:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
#
# task_15("ana")
# task_15("abba")
# task_15("test")
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_16" care acceptă un string și 
returnează același string cu literele inversate.
Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
"""

# CODUL TĂU VINE MAI JOS:
# def task_16(text):
#     return text[::-1]
#
# print(task_16("test"))
# print(task_16("Alexandr"))
# print(task_16("rdnaxelA"))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează
 numărul de cuvinte din string.
Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
"""

# CODUL TĂU VINE MAI JOS:
# def task_17(loremIpsum):
#     return len(loremIpsum.split(" "))
#
# print(task_17("Hello, World!"))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă 
temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
"""
##	(0°C × 9/5) + 32 = 32°F

# CODUL TĂU VINE MAI JOS:
# def task_18(temperatura):
#    return f"{(temperatura * 9/5) + 32} °F"
# # CODUL TĂU VINE MAI SUS:
# print(task_18(2))
"""
Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă 
numărul este prim, altfel `False`.
Exemplu: Pentru numărul 7 rezultatul va fi `True`, 
iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# def task_19(n):
#     if n <= 1:
#         print(False)
#     else:
#         is_prime = True
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         print(is_prime)
# task_19(16)
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` \
dacă numărul este un număr perfect, altfel `False`.
Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, 
excluzând numărul însuși.
Exemplu: Pentru numărul 28 rezultatul va fi `True`, 
iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# def task_20(num):
#     sumi=1
#     for i in range(2,num):
#         # print(i, num//i)
#         if num%i==0:
#             sumi = sumi+num//i
#     if sumi==num:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False

# CODUL TĂU VINE MAI SUS:
# task_20(6)
# task_20(28)
# task_20(496)

"""
Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` 
dacă numărul este un număr Armstrong, altfel `False`.
Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
Exemplu: Pentru numărul 153 rezultatul va fi `True`, 
iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# def task_21(num):
#     suma=0
#     for i in str(num):
#         suma=suma+(int(i)**len(str(num)))
#     if suma==num:
#         return True
#     else:
#         return False
# # CODUL TĂU VINE MAI SUS:
# print(task_21(153))
# print(task_21(1634))
"""
Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# def task_22(nr):
#     suma= 0
#     for i in str(nr):
#         suma += int(i)
#     return nr % suma == 0
# # CODUL TĂU VINE MAI SUS:
# print(task_22(18))
# print(task_22(14))
"""
Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și 
returneaeză o listă cu primele n numere ale seriei Fibonacci.
Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
"""

# # CODUL TĂU VINE MAI JOS:
# def task_23(n):
#     res=[0,1]
#     a,b=0,1
#     if n== 0:
#         return []
#     elif n==1:
#         return [0]
#     elif n==2:
#         return [0,1]
#     while len(res)<n:
#         c = a + b
#         res.append(c)
#         a = b
#         b = c
#     return res
# # CODUL TĂU VINE MAI SUS:
# print(task_23(5))
# print(task_23(10))
"""
Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
"""

# CODUL TĂU VINE MAI JOS:
# def task_24(nr):
#     res = []
#     for i in range(1,nr+1):
#         if nr % i == 0:
#             res.append(i)
#     return res
# # CODUL TĂU VINE MAI SUS:
# print(task_24(10))
# print(task_24(100))