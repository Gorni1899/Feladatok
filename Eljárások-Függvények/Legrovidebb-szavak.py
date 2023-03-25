"""
Írj egy programot, amely a felhasználótól bekér három szót, ezeket egy listában tárolja
és egy eljárás segítségével meghatározza, és a képeryőre kiírja, melyik a legrövidebb szó!

Az adatbekérés az eljáráson kívűl történjen és a létrehozott listát paraméterként add át az eljárásnak,
amely a vizsgálatot és a kiírást végzi!
"""


def legrovidebb(lista):
    legrovidebb_szo = lista[0]
    for szo in lista:
        if len(szo) < len(legrovidebb_szo):
            legrovidebb_szo = szo

    print(f"A legrövidebb szó a(z) {legrovidebb_szo}")


    """
    Amennyiben több azonosságú legrövidebb szó van akkor így tudjuk kiíratni:
    """

    for szo in lista:
        if len(szo) == len(legrovidebb_szo):
            print(f"Több legrövidebb szó van: {szo} ")


tartolt_szavak = []

while len(tartolt_szavak) != 3:
    bekert_szo = input("Adj meg egy szót: ")
    tartolt_szavak.append(bekert_szo)

legrovidebb(tartolt_szavak)