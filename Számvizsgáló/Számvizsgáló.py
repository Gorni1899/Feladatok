print("1.Feladat")
"""
Kérjen be a felhasználótól a [-1000; 1000] intervallumba eső egész számot!
"""
bekert_szam = int(input("Adj meg egy a [-1000;1000] tartományba eső egész számot! "))

if bekert_szam > 1000:
    print("A bekért szám nagyobb mint 1000")
    quit()

elif bekert_szam < -1000:
    print("A bekért szám kissebb mint -1000")
    quit()
aktualis_szam = 0
while bekert_szam > -1000 and bekert_szam < 1000:
    aktualis_szam = bekert_szam
    bekert_szam = int(input("Adj meg egy a [-1000;1000] tartományba eső egész számot! "))

print(aktualis_szam)

print("\n2.Feladat")
"""
2. Vizsgálja meg, és jelezze, hogy a megadott szám páros vagy páratlan és osztható-e hárommal!
"""
if aktualis_szam % 2 == 0 and aktualis_szam % 3 == 0:
    print("A megadott szám páros és osztható hárommal.")

elif aktualis_szam % 2 == 0 and aktualis_szam % 3 != 0:
    print("A megadott szám páros és nem osztható hárommal.")


elif aktualis_szam % 2 != 0 and aktualis_szam % 3 == 0:
    print("A megadott szám páratlan és osztható hárommal.")

elif aktualis_szam % 2 != 0 and aktualis_szam % 3 != 0:
    print("A megadott szám páratlan és nem osztható hárommal.")

print("\n3.Feladat")
print(f"A szám abszolút értéke {abs(aktualis_szam)} ")

print("\n4.Feladat")
while aktualis_szam % 5 != 0:
    aktualis_szam += 1
print(f"A szám abszolút értékéhez legközelebb eső, nála nagyobb öttel osztható szám a {aktualis_szam}")

print("\n5.Feladat")
# A középső számjegy(ek)
szamsztring = str(aktualis_szam)
print(f'A középső számjegy(ek) {szamsztring[1]}')