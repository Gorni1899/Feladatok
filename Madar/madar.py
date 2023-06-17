import random

"""
Dominik az ablaknál ült, és látta hogy egy kismadár több alkalommal be- majd kirepült a szobába.
Az ablakon való átrepülések időpontját felírta a füzetébe.
A most készítendő programban ezeket az időpontokat véletlenszámokkal helyettesítse,
és ezek alapján oldja meg a feladatot!
"""

print("1.Feladat")
"""
1. A program a felhasználótól kérje be a kismadár ablakon való átrepüléseinek számát.
Ez egy 5 és 10 közötti szám lehet, de ennek a helyességét nem kell ellenőriznie,
feltételezheti, hogy a felhasználó valóban ebbe az intervallumba eső számot ad meg!
"""
szam = int(input("Adj meg egy 5 és 10 közé eső számot! "))


print("\n2.Feladat")
"""
2. A program a felhasználó által előzőekben megadott darabaszámú véletlenszámot
állítson elő 1 és 30 között, és tárolja el ezeket. Ezek felelnek meg az átrepülések
percben kifejezett időpontjainak.
"""

tarolt_adatok = []

for i in range(szam):
    berepülesek = random.randint(1,30)
    tarolt_adatok.append(berepülesek)
print(tarolt_adatok)

print("\n3.Feladat")
"""
3. A program a lenti mintának megfelelő módon írja ki a képernyőre a generált
véletlenszámokat nagyság szerint növekvő sorrendben!
"""

tarolt_adatok.sort()

print(f"A mérés kezdetét (0. percet) követően mikor (hányadik percben) repült át a madár az ablakon: {tarolt_adatok}")

print('\n4.Feladat')

"""
4. A program állapítsa meg és a mintának megfelelően irja ki, hogy az utolsó átrepülést
követően a madár a szobában vagy a szabadban tartózkodik! (A mérés kezdetén - a
0. percben - a szoba üres volt, tehát az első ablakon való átrepüléskor repült be a
madár a szobába.)
"""

for index in range(len(tarolt_adatok)):
    if len(tarolt_adatok) % 2 != 0:
        print("A madár az utolsó átrepüléskor berepült a szobába.")
        break
    else:
        print("A madár a szabadban tartózkodik.")
        break

print("\n5.Feladat")
"""
5. A mintának megfelelően jelenítse meg, hogy a madár mennyi időt töltött a szobában,
és ezek közül melyik volt a leghosszabb bent tartózkodása!
"""
bent_toltott = 0
tarolt_bent = []

print("A madár által a szobában töltött időszakok hossza:")
for index, ertek in enumerate(tarolt_adatok, start=1):
    if index % 2 != 0:
        bent_toltott += ertek
        tarolt_bent.append(ertek)
        print(f'{index}. alkalommal: {ertek} percet töltött bent a madár.')

print(f"A legtöbb bent töltött idő: {max(tarolt_bent)} perc volt.")