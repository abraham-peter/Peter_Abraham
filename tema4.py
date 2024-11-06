import random
from collections import Counter

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = len(cuvant_de_ghicit) + 2
litere_incercate = []
print(" ".join(progres))
correct = 0
cuvant_ghicit_bool = 0
while (incercari_ramase >= 0) and cuvant_ghicit_bool == 0:
    print()
    incercari_ramase -= 1
    litere_de_la_jucator = str(input("Ghiceste o litera:"))

    if not litere_de_la_jucator.isalpha():
        print("Scrie numai litere maaaaiii")

    elif len(litere_de_la_jucator) > 1:
        print("Numai o litera baa")

    elif litere_de_la_jucator in litere_incercate:
        print("Ai folosit deja aceasta litera")

    if litere_de_la_jucator in cuvant_de_ghicit:
        nr_de_aceeasi_litere = Counter(litere_de_la_jucator)
        for _ in nr_de_aceeasi_litere:
            litere_incercate += litere_de_la_jucator

    for char in cuvant_de_ghicit:
        if char in litere_incercate and (Counter(litere_incercate) != Counter(cuvant_de_ghicit)):
            print(char, end=" ")
            correct += 1
        elif Counter(litere_incercate) == Counter(cuvant_de_ghicit):
            print("Cuvantul este: ", end=" ")
            print(cuvant_de_ghicit)
            cuvant_ghicit_bool = 1
            break
            break

        else:
            print("_", end=" ")
        if cuvant_ghicit_bool == 1:
            break
            break
    print("\nInceercari ramase:", incercari_ramase)

if incercari_ramase <= 0 and Counter(litere_incercate) != Counter(cuvant_de_ghicit):
    print()
    print("Ai pierdut papaluciea")
    print(f"Cuvantula a fost {cuvant_de_ghicit}")












