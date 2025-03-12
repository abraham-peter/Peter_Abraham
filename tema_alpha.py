lista_cnp=[]
import random

def generare_cnp():
    global lista_cnp
    Femeie=[6,2]
    Barbati=[5,1]
    ani=[i for i in range(1950,2026)]
    zi=[k for k in range(1,32)]
    luni={"Ianuarie":31,"Februarie":28,"Martie":31,"Aprilie":30,"Mai":31,"Iunie":30,"Iulie":31,"August":31,"Septembrie":30,"Octombrie":31,"Noiembrie":30,"Decembrie":31}
    judete_cnp = {1: "Alba", 2: "Arad", 3: "Argeș", 4: "Bacău", 5: "Bihor", 6: "Bistrița-Năsăud", 7: "Botoșani",
                  8: "Brașov", 9: "Brăila", 10: "Buzău", 11: "Caraș-Severin", 12: "Cluj", 13: "Constanța",
                  14: "Covasna", 15: "Dâmbovița", 16: "Dolj", 17: "Galați", 18: "Gorj", 19: "Harghita", 20: "Hunedoara",
                  21: "Ialomița", 22: "Iași", 23: "Ilfov", 24: "Maramureș", 25: "Mehedinți", 26: "Mureș", 27: "Neamț",
                  28: "Olt", 29: "Prahova", 30: "Satu Mare", 31: "Sălaj", 32: "Sibiu", 33: "Suceava", 34: "Teleorman",
                  35: "Timiș", 36: "Tulcea", 37: "Vaslui", 38: "Vâlcea", 39: "Vrancea", 40: "București",
                  41: "Giurgiu"}

    numar_secvential=[i for i in range(0,1000)]
    for i in range(0,500001): # Barbati
        sex=random.choice(Barbati)
        an=random.randint(1950,1999) % 100
        luna=random.randint(1,12)
        key = random.randint(0, 11)
        ziua=luni[key]
        key2 = random.randint(0,41)
        judet=judete_cnp[key2]
        for j in range(0,101):
            x=j
            j=100



        else:
            an=random.randint(2000,2025) % 100
            luna=random.randint(1,12)
            key = random.randint(0, 11)
            ziua=luni[key]
            key2 = random.randint(0,41)
            judet=judete_cnp[key2]
            for j in range(0,101):
                x=j
                j=100


generare_cnp()
for cnp in lista_cnp[:10]:  # Afișăm primele 10 rezultate
    print(cnp)