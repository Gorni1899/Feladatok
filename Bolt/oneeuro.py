
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

print("\n2.Feladat")
"""
Határozza meg, hogy hányszor fizettek a pénztárnál.
"""
print(f'A pénztárnál {len(vasarlasok)} fizettek.')

print("\n3.Feladat")
"""
Írja ki, hogy az első vásárlónak hány darab árucikk volt a kosarában.
"""
arucikk = sum(vasarlasok[0].values())
print(f'Az első vásárlónak a kosarában {arucikk} árucikk volt.')

print('\n4.Feladat')
'''
Függvényt fogok használni, hogy később ezt könnyen újra tudjam használni a kódban.
'''
sorszam =  2#int(input("Adja meg a vásárlás sorszámát: "))
aru = 'kefe'#input("Árucikk neve: ")
darabszam = 2 #int(input("Adja meg a darbszámot: "))


print("\n5.Feladat")

meg_nem = True
szamlalo = 0
utolso = 0

# Ilyenkor tuple-t kapunk vissza ami két értékből áll.
# Az egyik az index érték a másik pedig maga a kosár változóban ami van.
for index, kosar in enumerate(vasarlasok):
    for arucikk in kosar:
        if arucikk == aru and meg_nem:
            print(f'Az első vásárlás sorszáma: {index + 1}')
            meg_nem = False
        if arucikk == aru:
            szamlalo += 1
            utolso = index
print(f'Az utolsó vásárlás sorszáma: {utolso + 1}')
print(f'{szamlalo} vásárlás során vettek belőle.')
