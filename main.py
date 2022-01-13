import random

def lisää_sana(sana=""):
    with open("sanalista.txt", "a+") as sanalista:
        sanalista.seek(0)
        if len(sanalista.read()) > 0:
            sanalista.write("\n")
            if sana in open("sanalista.txt").read():
                print("Sana", sana, "on jo listalla!")
            else:
                sanalista.write(sana)
                print("Sana", sana, "lisättiin listalle!")

def lataa_sanalista(sana_pituus):
    with open("sanalista.txt", encoding="utf-8") as sanalista:
        return [sana
                for sana in set(sanalista.read().split())
                if (len(sana) == sana_pituus) and sana[-1].isupper() != True]

def aloita_peli(sana_pituus, max_kierrokset):

    sanalista = lataa_sanalista(sana_pituus)
    sana = (random.choice(sanalista))
    kierrokset = 0
    väärät_kirjaimet = []
    arvaus = ""

    print(sana)

    while(arvaus != sana):

        väärät_kirjaimet.sort()
        arvaus = input("Anna viisi kirjaiminen sana: ")
        print("Väärät kirjaimet:", list(set(väärät_kirjaimet)))

        if arvaus not in sanalista:
            print("Sanaa ei löydy sanalistasta, voit halutessasi lisätä sanan metodin lisää_sana avulla!")

        if (len(arvaus) < 5):
            print("Syötit liian lyhyen sanan")

        if arvaus in sanalista:
            for kirjain in zip(sana, arvaus):
                if kirjain[1] not in sana:
                    väärät_kirjaimet.append(kirjain[1])
                    print("Kirjain", kirjain[1], "on väärin!")
                    continue
                if kirjain[1] in sana:
                    if kirjain[1] == kirjain[0]:
                        print("Kirjain", kirjain[1], "on oikein ja oikeassa kohdassa!")
                        continue
                    else:
                        print("Kirjain", kirjain[1], "on oikein, mutta väärässä kohdassa!")
                        continue
        kierrokset += 1

        if (kierrokset >= max_kierrokset):
            print("Hävisit pelin, oikea sana oli", sana)
            break

        if (arvaus == sana):
            print("Arvasit sanan oikein!")
            break


aloita_peli(5, 6)