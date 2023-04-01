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
    pass