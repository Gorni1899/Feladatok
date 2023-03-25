"""
Írj egy programot amely a felhasználótól bekér három szót, ezeket egy listában tárolja, és egy eljárás segítségével
meghatározza, és kiírja a képernyőre melyik a legrövidebb szó!

Az adatbekérést az eljáráson kívűl valósítsd meg, és a létrehozott listát paraméterként add át az eljárásnak,
amely a vizsgálatot és a kiírást végzi.
"""


def legrovidebb(lista):
    legrovidebb_szo = lista[0]
    for szo in lista:
        if len(szo) < len(legrovidebb_szo):
            legrovidebb_szo = szo
    print(f"A legrövidebb szó: {legrovidebb_szo}")

    # Amennyiben több hosszúságú legrövidebb szó van:
    for szo in lista:
        if len(szo) == len(legrovidebb_szo):
            print(f'A legrövidebb szavak {szo}')



tarolt_szavak = []

while len(tarolt_szavak) != 3:
    bekert_szo = input("Adj meg egy szót: ")
    tarolt_szavak.append(bekert_szo)


legrovidebb(tarolt_szavak)