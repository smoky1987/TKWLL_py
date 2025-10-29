# Exercitiul 1: Scrie un program care cere utilizatorului să introducă un cuvânt și afișează primele 3 caractere.
# cuvint = input("introdu un cuvint: ")
# prime_3 = cuvint[0:3]   #ori [:X] - max sau [:] - all
# print(prime_3)

# Exercitiul 2: Cere utilizatorului un cuvânt și afișează ultimele 2 caractere ale acestuia.
# wordInp = input("Please : ")
# print(wordInp[-2:])


# Exercitiul 3: Afișează caracterele de pe pozițiile pare dintr-un string dat de utilizator.
# evenChar = input("Please : ")
# print(evenChar[0:len(evenChar):2])

# Exercitiul 4: Cere utilizatorului un cuvânt și afișează-l invers.
# myWord = input("introdu un myword: ")
# myWord_invers = myWord[::-1]
# print(myWord)
# print(f"Cuvint initial: {myWord}, \n"
#       f"Cuvint_invers: {myWord_invers}.")

# Exercitiul 5: Cere utilizatorului să introducă un cuvânt și înlocuiește prima și
# ultima literă cu caracterul *.
# myStra  = input("Give me a name :")
# V1
# fstLT =myStra[:1:]
# fstLT="*"
# lstLT = myStra[-1:]
# lstLT="*"
# numero =myStra[1:len(myStra)-1:]
# finality = "{}{}{}".format(fstLT,numero,lstLT)
# print(finality)
#V2
# lside = myStra.lstrip(myStra[:1:])
# rside = lside.rstrip(myStra[-1:])
# print("*"+rside+"*")

# Exercitiul 6: Scrie un program care cere utilizatorului un text și un
# substring și afișează de câte ori apare substringul în text.
# inpMy = input("Hey! da un text.. ")
# substMy = input("Mai da si un cuvint de cautare ")
# print(inpMy.count(substMy))  ## nu e cea mai buna solutie!

# Exercitiul 7: Cere utilizatorului un text și un cuvânt de înlocuit și afișează textul după
# înlocuirea acestui cuvânt cu ****.
# inpMy = input("Hey! da un text.. ")
# substMy = input("Mai da si un cuvint de cautare ")
# print(inpMy.replace(substMy,  "*****"))

print("fwefw"*3)

# Exercitiul 8: Cere utilizatorului un text și afișează textul fără primele 2 și ultimele 2 caractere.
# mytxt = input("Hey! da un text..")
# intermidiateValv = mytxt.rstrip(mytxt[-2::])
# print(intermidiateValv.lstrip(mytxt[:2]))

# Exercitiul 9: Cere utilizatorului un text și afișează o combinație din primele 3 caractere și ultimele 3 caractere,
# ambele inversate.
# val1 = input("Inserire una string: ")
# val2 = val1[:3:]
# val3 = val1[-3::]
# fatality = val2[::-1]+val3[::-1]
# print(fatality)


"""BONUS"""
# Exercitiul 10: Cere utilizatorului un text, un string si un substring
# apoi înlocuiește toate aparițiile stringului doar în prima jumătate a textului.
# primotxt = input("Give me text: ")
# secundo = input("Give more text:) ")
# test = primotxt[:int(len(primotxt)/2)]
# print(test.replace(secundo,"***"))