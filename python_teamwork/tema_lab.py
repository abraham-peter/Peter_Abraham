# etapa1
lista_cnp = []
cnp_cu_nume_si_prenume = {}

import random


def statistica_sex():
    varsta_aleasa = ["0-17" "15-64", "65+"]
    procente_varsta = [14.5, 67.7, 17.8]  # Procente aproximative din structura populației 2023

    alegere_varsta = random.choices(varsta_aleasa, weights=procente_varsta, k=1)[0]
    #persoane minore
    if alegere_varsta == "0-17":
        gender_choices = ["Băiat", "Fată"]
        gender_weights = [50, 50]  # Distribuție aproximativ egala a sexului
        alegere_sex = random.choices(gender_choices, weights=gender_weights, k=1)[0]#alegem sexul persoanei folosind procentajul de ma sus
        varsta_persoana = random.choices(range(0,18),gender_weights, k=1)[0]#aleg o vârstă random dupa procentajul ales din rangeul definit
        an_persoana = 2023-varsta_persoana#calculam varsta finala
    #persoane adulte
    elif alegere_varsta == "18-64":
        gender_choices = ["Bărbat", "Femeie"]
        gender_weights = [46, 54]   # Distribuție aproximativ egala a sexului
        alegere_sex = random.choices(gender_choices, weights=gender_weights, k=1)[0]    #alegem sexul persoanei folosind procentajul de ma sus
        varsta_persoana = random.choices(range(18,65),gender_weights,k=1)[0]  #aleg o vârstă random dupa procentajul ales din rangeul definit
        an_persoana = 2023-varsta_persoana  #calculam varsta finala
    #persoane bătrâne
    else:
        gender_choices = ["Bărbat", "Femeie"]
        gender_weights = [40.3,59.6]    # Distribuție aproximativ egala a sexului
        alegere_sex = random.choices(gender_choices, weights=gender_weights, k=1)[0]    #alegem sexul persoanei folosind procentajul de ma sus
        varsta_persoana = random.choices(range(65,100),gender_weights,k=1)[0]  #aleg o vârstă random dupa procentajul ales din rangeul definit
        an_persoana = 2023-varsta_persoana   #calculam varsta finala

    # Determinam care e
    if alegere_sex == "Băiat" and alegere_varsta == "0-17":
        cod = 1
        an_final=an_persoana%100
    elif alegere_sex == "Fată" and alegere_varsta == "0-17":
        cod = 2
        an_final=an_persoana%100
    elif alegere_sex == "Bărbat" and alegere_varsta == "18-64":
        cod = 5
        an_final=an_persoana%100
    elif alegere_sex == "Femeie" and alegere_varsta == "18-64":
        cod = 6
        an_final=an_persoana%100
    elif alegere_sex == "Bărbat" and alegere_varsta == "65+":
        cod = 7
        an_final=an_persoana%100
    elif alegere_sex == "Femeie" and alegere_varsta == "65+":
        cod = 8
        an_final=an_persoana%100

    return cod, an_final

def calculeaza_cifra_control(cnp_temporar):
    constanta = "279146358279"
    suma = 0
    cnp_temporar = str(cnp_temporar)
    for i in range(12):
        suma += int(cnp_temporar[i]) * int(constanta[i])

    rest = suma % 11
    if rest==10:
        cifra_control=1
    else:
        cifra_control=rest

    return cifra_control

def generare_cnp():
    global lista_cnp
    ani_inainte_de_2000 = [ani_inainte for ani_inainte in range(1950, 2000)]
    ani_dupa_2000 = [ani_dupa for ani_dupa in range(2001, 2025)]
    luna = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    judete_cnp = [judete for judete in range(1, 42)]
    numar_secvential=[i for i in range(0,1000)]
    for i in range(0,500001): #Barbati
        sex=random.randint(5,1)
        if sex==1:
            an=random.randint(1950,1999) % 100
            luna=random.randint(1,12)
            key = random.randint(0, 11)
            ziua=luni[key]
            key2 = random.randint(0,42)
            judet=judete_cnp[key2]
            for j in range(0,101):
                x=j
                j=100

def hashing(cnp):
    for keys,values in 


if __name__ == "__main__":
    statistica_sex()