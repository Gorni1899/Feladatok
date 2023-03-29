print("1.Feladat")

versenyszakaszok = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF.0', 'F2.1', 'NF2']

print("\n2.Feladat")
ossz_km = 0

for km in versenyszakaszok:
    if km[0] == "F":
        ossz_km += float(km[1:])
    else:
        ossz_km += float(km[2:])
print(f'A verseny össztávja {ossz_km} volt.')

print("\n3.Feladat")

if versenyszakaszok[-1][0] == "N":
    print("Olivér gyalogolva ért célba.")

print("\n4.Feladat")
megallt = 0
for all in versenyszakaszok:
    if all[-1] == "0":
        megallt += 1
print(f"Olivér a verseny során {megallt} -szer állt meg. ")

print("\n5.Feladat")
megszakitotta = 0

for index in range(len(versenyszakaszok) -1):
    if versenyszakaszok[index][0] == "F" and versenyszakaszok[index+1][0] == "N":
        megszakitotta += 1

if megszakitotta > 0:
    print(f"Olivér {megszakitotta} -szer szakította meg a futását.")
else:
    print("Olivér nem szakíotta meg a futását.")

print("\n6.Feladat")
kozvetlenul = False

for index in range(len(versenyszakaszok)-1):
    if versenyszakaszok[index][0] == "N" and versenyszakaszok[index+1][-1] == "0":
        kozvetlenul = True

if kozvetlenul:
    print("Volt olyan alkalom, hogy nem futott és teljesen megállt.")