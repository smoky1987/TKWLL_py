"""
Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente
și returnează suma acestora.
Exemplu: task_1(1, 2, 3) ➞ 6
"""

# CODUL TĂU VINE MAI JOS:
# def task_1(*nums):
#     sum=0
#     for num in nums:
#         sum+=num
#     return sum
# print(task_1(2,4,6,8))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente 
și returnează o listă cu argumentele care sunt numere întregi.
Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
"""

# CODUL TĂU VINE MAI JOS:
# def task_2(*vars):
#     arr=[]
#     for var in vars:
#         if type(var) is int:
#             arr.append(var)
#     return arr
# print(task_2(1, 2, 'a', 'b'))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
Exemplu: task_3(1, 4, 5) ➞ 20
"""

# CODUL TĂU VINE MAI JOS:
# def task_3(*prods):
#     prod = 1
#     for i in prods:
#         prod = prod *i
#     return prod
# print(task_3(1,2,3,4))
# print(task_3(1,4,5))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_4` care primește un număr arbitrar de perechi cheie-valoare și 
returnează un string care conține toate cheile și valorile concatenate separate de un spațiu.
Exemplu: task_4(a=1, b=2, c=3) ➞ 'a 1 b 2 c 3'
"""

# CODUL TĂU VINE MAI JOS:
# def task_4(**data):
#     fin=""
#     for k, v in data.items():
#         fin =fin + f"{k} {v} "
#     return fin
#
# print(task_4(a=1, b=2, c=3))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și 
returnează două liste separate.
Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, 
iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate 
în ordine alfabetică.
Exemplu: task_6(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
"""

# CODUL TĂU VINE MAI JOS:
# def task_5(*data,**kvdata):
#     l1=[]
#     l2=[]
#     for item in data:
#         l1.append(item)
#     for k2, v2 in kvdata.items():
#         if isinstance(v2, str):
#             l2.append(k2)
#     return sorted(l1),l2
#
#
# print(task_5(3, 1, 2, a=10, b=20))
# print(task_5(3, 1, 2, a=10, b=20, c='a'))
# print(task_5(3, 1, 2, a=10, b=20, c='a', d='b'))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și 
returnează un dicționar care conține toate argumentele keyword ca key și valoarea acestora ca value.
Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
"""

# CODUL TĂU VINE MAI JOS:
# def task_6(**data):
#     return {k:v for k,v in data.items()}
# print(task_6(a=1, b=2, c=3))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_7` care poate primi un număr nedeterminat 
de argumente atât string-uri cât și numere și va returna un dicționar cu două chei: 
`str` și `int`.
Cheia `str` va avea o listă cu toate string-urile primite ca argumente, 
iar cheia `int` va avea o listă cu toate numerele primite ca argumente.
Exemplu: task_7(1, 'a', 2, 'b') ➞ {'str': ['a', 'b'], 'int': [1, 2]}
"""

# CODUL TĂU VINE MAI JOS:
# def task_7(*args):
#     string = []
#     intg = []
#     for arg in args:
#         if type(arg) is str:
#             string.append(arg)
#         if type(arg) is int:
#             intg.append(arg)
#     return {'str': string, 'int': intg}
# print(task_7(1, 'a', 2, 'b'))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și 
returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, 
iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 
'non_palindrom': ['hello', 'world']}
"""

# CODUL TĂU VINE MAI JOS:
# def task_8(*argumente):
#     plndrm=[]
#     non_plndrm=[]
#     for item in argumente:
#         if item[::-1]==item:
#             plndrm.append(item)
#         else:
#             non_plndrm.append(item)
#     return {'palindrom':plndrm, 'non_palindrom':non_plndrm}
# print(task_8('madam', 'hello', 'level', 'world'))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_9` care primește un număr variabil de argumente 
de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt multipli ai lui `number`.
Exemplu: task_9(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
# def task_9(*args, **kwargs):
#     fin=[]
#     man_num = list(kwargs.values())
#     for arg in range(1, len(args)+1):
#         if arg % man_num[0]==0:
#             fin.append(arg)
#     return fin
#
# print(task_9(1, 2, 3, 4, 5,6,7,8, number=2))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și 
un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt divizibile cu `number`.
Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
# def task_10(*args, **kwargs):
#     fin=[]
#     item=list(kwargs.values())[0]
#     for i in range(1, len(args)+1):
#         if i%item==0:
#             fin.append(i)
#     return fin
# print(task_10(1, 2, 3, 4, 5, number=2))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip 
integer care reprezintă șirul Fibonacci.
Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
# def task_11(*args):
#     fibo=[]
#
#     a = 0
#     b = 1
#     for i in range(1, len(args)):
#         if i < 0:
#             print("Incorrect input")
#         elif i == 0:
#             return 0
#         else:
#             c=a+b
#             fibo.append(c)
#             a = b
#             b = c
#     fibo.insert(0,1)
#
#     if fibo == list(args):
#         print(fibo,'  ',args)
#         return True
#     else:
#         print(fibo, '  ', args)
#         return False
#
# print(task_11(1, 1, 2, 3, 5, 8))
# print(task_11(1, 1, 2, 3, 5, 9))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente 
de tip integer.
Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
Exemplu: task_12(2, 3, 5, 7) ➞ True
Exemplu: task_12(1, 2, 3, 4) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
# def task_12(*data):
#     for i in data:
#         if i == 1 or i == 0:
#             return False
#         for j in range(2,i):
#             if not i % j:
#                 return False
#         else:
#             return True
# print(task_12(2, 3, 5, 7))
# print(task_12(1, 2, 3, 4))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument 
de tip string și un număr variabil de argumente de tip string.
Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
Exemplu: task_13('listen', 'silent') ➞ True
Exemplu: task_13('hello', 'world') ➞ False
"""

# CODUL TĂU VINE MAI JOS:
# def task_13(*anagrame):
#     intersection_two = set(list(anagrame[0])).intersection(set(list(anagrame[1])))
#     if len(intersection_two) == len(anagrame[0]):
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
# # CODUL TĂU VINE MAI SUS:
# print(task_13('listen', 'silent'))
# print(task_13('hello', 'world'))

"""
Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` 
de tip string și un număr variabil de argumente de tip string.
Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
"""

# CODUL TĂU VINE MAI JOS:
# def task_14(*strng, sub_string=""):
#     data=[]
#     for i in strng:
#         if sub_string in i:
#             data.append(i)
#     return data
#
# print(task_14('home', 'same', 'meme', sub_string="me"))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` 
de tip string și un număr variabil de argumente de tip string.
Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, 
iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') 
➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
"""

# CODUL TĂU VINE MAI JOS:
# def task_15(*strng, sub_string=""):
#         contains=[]
#         not_contains=[]
#         for i in strng:
#             if sub_string in i:
#                 contains.append(i)
#             else:
#                 not_contains.count(i)
#         return {"contains":contains,"not_contains":not_contains}
#
# print(task_15('home', 'same', 'meme', sub_string = 'me'))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
"""

# CODUL TĂU VINE MAI JOS:
# def task_16(*args, operation):
#     if operation == 'add':
#         return sum(args)
#     elif operation == 'sub':
#         return args[0] - sum(args[1:])
#     elif operation == 'mul':
#         res = 1
#         for arg in args:
#             res*= arg
#         return res
#     else:
#         res = args[0]
#         for arg in args[1:]:
#             res/=arg
#         return res
#
# print(task_16(2, 3, 4, 5, operation='add'))
# print(task_16(2, 3, 4, 5, operation='sub'))
# print(task_16(2, 3, 4, 5, operation='mul'))
# print(task_16(2, 3, 4, 5, operation='div'))

# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
"""

# CODUL TĂU VINE MAI JOS:
# def task_17(nr, **kwargs):
#     if kwargs.get('add'):
#         return nr + sum(kwargs['add'])
#     elif kwargs.get('sub'):
#         return nr - sum(kwargs['sub'])
#     elif kwargs.get('mul'):
#         for i in kwargs['mul']:
#             nr *= i
#             return nr
#     else:
#          for i in kwargs['div']:
#             nr /= i
#             return nr
#
# print(task_17(2, add=[3, 4, 5]))
# print(task_17(2, sub=[3, 4, 5]))
# print(task_17(2, mul=[3, 4, 5]))
# print(task_17(2, div=[3, 4, 5]))
# print(task_17(2, add=[3, 4, 5], sub=[1, 2]))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

# CODUL TĂU VINE MAI JOS:
# def task_18(*strings):
#     data = []
#     # fin ={}
#     for i in strings:
#         data += list(i)
#     fin= {i:data.count(i) for i in data}
#     return fin
# print(task_18('hello', 'world'))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente 
de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite 
în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_19(*args):
    def este_prim(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    rezultat = {}
    for numar in args:
        if este_prim(numar):
            rezultat[numar] = rezultat.get(numar, 0) + 1
    return rezultat
print(task_19(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12))
# CODUL TĂU VINE MAI SUS:


"""
Task: Creați o funcție cu numele `task_20` care primește un număr variabil de 
argumente de tip string și va returna un dicționar în care cheile vor fi lungimile 
cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții 
ale lungimilor cuvintelor.
Exemplu: task_20('hello', 'world') ➞ {5: 2}
Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_20(*args):
    rezultat = {}
    for cuvant in args:
        lungime = len(cuvant)
        rezultat[lungime] = rezultat.get(lungime, 0) + 1
    return rezultat
print(task_20('hello', 'world'))
print(task_20('hello', 'world', 'python'))
# CODUL TĂU VINE MAI SUS:
