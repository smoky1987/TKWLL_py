# TODO: 1 - Aflati suma primelor 5000 de numere
sum = 0
for i in range(0,5001):
    sum+=i
print(sum)


# TODO: 2 - Creati in consola, cu ajutorul functiei print aceasta piramida
"""
#     1
#    22
#   333
#  4444
# 55555
"""
for i in range(1,6):
    var =(6-i)*(" ")+i*str(i)
    print(var)
