print("1.Feladat")

kosar = {}
vasarlasok = []

with open("penztar.txt", "r", encoding="utf-8") as file:
    for termekek in file:
        if termekek.strip() == "F":
            vasarlasok.append(kosar)
            kosar = {}
        # Feltöltjük a kosarakat termékekkel
        if termekek.strip() not in kosar:
            kosar[termekek.strip()] = 1
        else:
            kosar[termekek.strip()] += 1

print(vasarlasok)

print("\n2.Feladat")

print(f"A pénztárnál a mai napon {len(vasarlasok)} alkalommal fizettek.")

print("\n3.Feladat")

for darabszam in vasarlasok[0]:
    print(f"Az első vásárló {vasarlasok[0][darabszam]} darab árucikket vásárolt.")