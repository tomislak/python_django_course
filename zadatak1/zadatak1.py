brojac = 0
imeD = {}
prezimeD = {}
with open('ulaz.txt', 'r') as f:
    for line in f:
        brojac += 1
        if imeD.get(line.split()[0]):
            imeD[line.split()[0]] += 1
        else:
            imeD[line.split()[0]] = 1
        if prezimeD.get(line.split()[1]):
            prezimeD[line.split()[1]] += 1
        else:
            prezimeD[line.split()[1]] = 1
print(imeD)
print(prezimeD)
maks = max(imeD.values())
print(maks)
for ime, vrijednost in imeD.items():
    if vrijednost == maks:
        print(ime)
maks = max(prezimeD.values())
print(maks)
for ime, vrijednost in prezimeD.items():
    if vrijednost == maks:
        print(ime)
