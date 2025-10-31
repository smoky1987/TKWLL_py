# Exercițiul 1
# Inversează cheile și valorile din dicționar (cheile devin valori, valorile devin chei)

fructe_preturi = {
    "mar": 5,
    "banana": 3,
    "cireasa": 8,
    "kiwi": 6,
    "mango": 12
}
print({v:k for k,v in fructe_preturi.items()})


# Exercițiul 2
# Găsește toate numerele care apar de cel puțin 2 ori și afișează câte apariții au

numere = [1, 2, 3, 1, 2, 1, 4, 5, 2, 3, 6, 7, 3, 8, 1]
freq= {}
for num in numere:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 0 + 1
final ={}
for x in freq:
    if freq[x] >= 2:
        final[x] = freq[x]

print(final)
