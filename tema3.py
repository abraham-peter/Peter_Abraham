
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []


for i in range(len(comenzi)):
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f"{student} a comandat {comanda}.")
    tavi.pop()
    istoric_comenzi.append(comanda)

comenzi_count = {"papanasi": 0, "ceafa": 0, "guias": 0}
for comanda in istoric_comenzi:
    comenzi_count[comanda] += 1


print(
    f"S-au comandat {comenzi_count['guias']} guias, {comenzi_count['ceafa']} ceafa, {comenzi_count['papanasi']} papanasi.")
adevarat=0
if "guias" in meniu:
    print("Mai este guias: True")

if "ceafa" in meniu:
    print("Mai este ceafa: True")

if "papanasi" in meniu:
    print("Mai este papanas: True")


total = comenzi_count['guias'] * 5 + comenzi_count['ceafa']*10 + comenzi_count['papanasi'] * 7
print(f"Cantina a incasat {total} lei")

preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
produse_7lei=''
for produs, pret in preturi:
    if pret < 8:
        produse_7lei+=f"[{produs},{pret}] "

print(f"produsele ce costa 7 lei:{produse_7lei}")




