import random

print("1.Feladat")

hatarertek = int(input("Add meg a határértéket: "))

print("\n2.Feladat")
veletlenszam = random.randint(1, hatarertek)

print("\n3. és 4. Feladat")
szamlalo = 1
tipp = int(input("Add meg a tipped: "))

while tipp != veletlenszam:
    if tipp == -1:
        quit(f"Sajnálom a kitalálandó szám a {veletlenszam} lett volna.")

    elif tipp < veletlenszam:
        tipp = int(input("Nagyobb számra gondoltam!\nAdd meg a tipped: "))
    else:
        tipp = int(input("Kisebb számra gondoltam!\nAdd meg a tipped: "))
    szamlalo += 1

print("\n5.Feladat")
print(f'Kitaláltad {szamlalo} próbálkozásból.')

print("\n6.Feladat")
print("A program vége!")