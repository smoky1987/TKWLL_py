"""
Creați o funcție process_list care:
1. Primește o listă de numere
2. Are un parametru opțional 'filter_even' (implicit False)

Cerințe:
- Dacă filter_even este True, păstrează doar numerele pare
- Transformă fiecare număr astfel: dacă e par îl dublează, dacă e impar îl triplează
- Returnează lista rezultată

Bonus:
- Folosește o funcție lambda pentru a transforma numerele

Exemple:
process_list([1, 2, 3, 4], filter_even=True) -> [4, 8]  # doar pare, apoi dublate
process_list([1, 2, 3, 4]) -> [3, 4, 9, 8]  # impare triple, pare duble
"""
# def process_list(data,filter_even=False):
#     dubl=[]
#     for num in data:
#         if filter_even == True:
#             if num % 2 == 0:
#                 dubl.append(num*2)
#         else:
#             dubl.append(num*3)
#     return dubl
# print(process_list([1, 2, 3, 4], filter_even=True))
# print(process_list([1, 2, 3, 4]))

# def process_list(data, filter_even=False):
#     res = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, data))
#     if filter_even:
#         res = list(filter(lambda x: x % 2 == 0, res))
#     return res
#
# print(process_list([1, 2, 3, 4], filter_even=True))
# print(process_list([1, 2, 3, 4]))