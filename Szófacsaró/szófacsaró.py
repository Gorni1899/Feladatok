import random

print("1.Feladat")

szavak = ['Róma', 'alma', 'megyeszékhely', 'mozdonyvezető', 'hűtőszekrény', 'Szeged', 'görög', 'Tatabánya']

veletlen_szo = random.choice(szavak)

print(veletlen_szo)

print("\n2.Feladat")

if veletlen_szo[0].isupper():
    print(f"A szó tulajdonnén és {len(veletlen_szo)} betűből áll. ")
else:
    print(f'A szó köznév és {len(veletlen_szo)} betűből áll.')

print("\n3.Feladat")

palindrom = veletlen_szo[::-1]

if veletlen_szo == palindrom:
    print("A szó palindrom!")
else:
    print("A szó nem palindrom.")

print("\n4.Feladat")
print("Találd ki a véletlenszót!")

print("a, Megadhatom a szó maszkját, amelyben a magánhabgzók helyén csillagszerepel, pl: h*z*f*l*d*t"
      "b, Megadhatom a szót alkotó betüket, pl: fldtáiehaza ")

valasztas = input("Milyen formában segítsek? (a/b) ")

"""
Ennél a feladatnál a b opciót nem értem még.
"""

if valasztas == 'a':
    for index, ertek in enumerate(veletlen_szo):
        if index % 2 == 0:
            print("*", end="")
        else:
            print(ertek, end="")

else:
    # veletlen szo nevű változóban tárolt sztring karaktereinek indexét
    # állítjuk elő véletlen sorrendben, és ezeket eltároljuk egy listában
    kevert_szo = []
    while len(kevert_szo) != len(veletlen_szo):
        veletlen_index = random.randint(0, len(veletlen_szo)-1)
        if veletlen_index not in kevert_szo:
            kevert_szo.append(veletlen_index)
    # a véletlenszerű indexsorrendnek megfelelően írjuk ki a sztring karaktereit
    for veletlen_index in kevert_szo:
        print(veletlen_szo[veletlen_index], end="")

tipp = input("\nAdd meg a tipped: ")

if tipp == veletlen_szo:
    print("Gratulálok, eltaláltad!")

else:
    print(f"Sajnos nem talált, a keresett szó a(z) {veletlen_szo} lett volna.")