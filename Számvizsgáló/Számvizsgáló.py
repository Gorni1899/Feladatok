"""
Készíts egy programot, amely a felhasználó által megadott számot illetve annak számjegyeit
vizsgálja! A program forráskódját mentse “szamvizsgalo” néven!
"""

print("1.Feladat")
"""
Kérjen be a felhasználótól a [-1000; 1000] intervallumba eső egész számot!
Az adatbekérés mindaddig folytatódjon, amíg a megadott szám az intervallumba nem esik! (Feltételezheti,
hogy a felhasználó egész számot ad meg.)
"""
intervallum = [-1000, 1000]

bekert_szam = int(input("Adj meg egy számot -1000 és 1000 között: "))

while bekert_szam < intervallum[0] or bekert_szam > intervallum[1]:
    bekert_szam = int(input("Adj meg egy számot -1000 és 1000 között: "))

print("\n2.Feladat")
"""
Vizsgálja meg, és a mintának megfelelően jelezze, hogy a megadott szám páros
vagy páratlan és osztható-e hárommal!
"""
if bekert_szam % 2 == 0:
    print("A megadott szám páros.")
else:
    print("A megadott szám páratlan.")

print("\n3.Feladat")

print(f'A szám abszolút értéke {abs(bekert_szam)}')

print("\n4.Feladat")
"""
4. Amennyiben a szám osztható öttel, jelezze ezt a felhasználónak, ha nem, akkor adja
meg a minta szerint a szám abszolút értékéhez legközelebb eső nála nagyobb öttel
osztható számot!
"""
while bekert_szam % 5 != 0:
    bekert_szam += 1

print(f'A szám abszolút értékéhez legközelebb eső, nála nagyobb öttel osztható szám a {bekert_szam}')


print("\n5.Feladat")
"""
5. A minta szerint jelenítse meg a szám középső számjegyét / számjegyeit!
"""
szam = str(bekert_szam)

if len(szam) == 4:
    print(f"A középső számjegy(ek): {szam[1:3]}")
else:
    print(f'A középső számjegy(ek): {szam[1]}')