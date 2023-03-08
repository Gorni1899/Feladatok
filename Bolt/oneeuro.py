
print("1.Feladat")
"""
1. Olvassa be és tárolja el a penztar.txt fájl tartalmát! 
"""
vasarlasok = []
kosar = {}
with open('penztar.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        if sor.strip() == 'F':
            vasarlasok.append(kosar)
            kosar = {}
        else:
            if sor.strip() not in kosar:
                kosar[sor.strip()] = 1
            else:
                kosar[sor.strip()] += 1

print(vasarlasok)