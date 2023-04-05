print("1.Feladat")

kosar = {}
vasarlasok = []

with open("penztar.txt", "r", encoding="utf-8") as file:
    for termek in file:
        if termek.strip() == "F":
            vasarlasok.append(kosar)
            kosar = {}
        # Belepakoljuk a termékeket a kosárba
        else:
            if termek.strip() not in kosar:
                kosar[termek.strip()] = 1
            else:
                kosar[termek.strip()] += 1
print(vasarlasok)

print("2.Feladat")
print(f"A fizetések száma: {len(vasarlasok)}")

print("3.Feldat")
szamlalo = 0

for termek_db in vasarlasok[0]:
    szamlalo += vasarlasok[0][termek_db]
print(f'Az első vásárló {szamlalo} darab árucikket vásárolt.')