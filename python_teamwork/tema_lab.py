lista_cnp = []
cnp_cu_nume_si_prenume = {}
import random
from collections import Counter


def statistica_sex():
    varsta_aleasa = ["0-17","18-64","65+"]
    procente_varsta = [14.5, 67.7, 17.8]  # Procente aproximative din structura populației 2023din toata România
    varsta_speciala=False
    alegere_varsta = random.choices(varsta_aleasa, weights=procente_varsta, k=1)[0]
    #persoane minore
    if alegere_varsta == "0-17":
        gender_choices = ["Băiat", "Fată"]
        gender_weights = [50, 50]  # Distribuție aproximativ egala a sexului
        alegere_sex = random.choices(gender_choices, weights=gender_weights, k=1)[0]#alegem sexul persoanei folosind procentajul de ma sus
        varsta_persoana = random.randint(0,17)#aleg o vârstă random dupa procentajul ales din rangeul definit
        an_persoana = 2023-varsta_persoana#calculam varsta finala
    #persoane adulte
    elif alegere_varsta == "18-64":
        gender_choices = ["Bărbat", "Femeie"]
        gender_weights = [46, 54]   # Distribuție aproximativ egala a sexului
        alegere_sex = random.choices(gender_choices, weights=gender_weights, k=1)[0]    #alegem sexul persoanei folosind procentajul de ma sus
        varsta_persoana = random.randint(18,64)#aleg o vârstă random dupa procentajul ales din rangeul definit
        if varsta_persoana>18 and varsta_persoana<24:
            varsta_speciala=True
              
        an_persoana = 2023-varsta_persoana  #calculam varsta finala
    #persoane bătrâne
    else:
        gender_choices = ["Bărbat", "Femeie"]
        gender_weights = [40.3,59.6]    # Distribuție aproximativ egala a sexului
        alegere_sex = random.choices(gender_choices, weights=gender_weights, k=1)[0]    #alegem sexul persoanei folosind procentajul de ma sus
        varsta_persoana = random.randint(65,100)#aleg o vârstă random dupa procentajul ales din rangeul definit
        an_persoana = 2023-varsta_persoana   #calculam varsta finala

    # Determinam care e
    if alegere_sex == "Băiat" and alegere_varsta == "0-17":
        cod = 5
        an_final=an_persoana%100
    elif alegere_sex == "Fată" and alegere_varsta == "0-17":
        cod = 6
        an_final=an_persoana%100
    elif alegere_sex == "Bărbat" and alegere_varsta == "18-64" and varsta_speciala==True:
        cod = 5
        an_final=an_persoana%100
    elif alegere_sex == "Femeie" and alegere_varsta == "18-64" and varsta_speciala==True:
        cod = 6
        an_final=an_persoana%100
    elif alegere_sex == "Bărbat" and alegere_varsta == "18-64" and varsta_speciala==False:
        cod = 1
        an_final=an_persoana%100
    elif alegere_sex == "Femeie" and alegere_varsta == "18-64" and varsta_speciala==False:
        cod = 2
        an_final=an_persoana%100
    elif alegere_sex == "Bărbat" and alegere_varsta == "65+":
        cod = 1
        an_final=an_persoana%100
    elif alegere_sex == "Femeie" and alegere_varsta == "65+":
        cod = 2
        an_final=an_persoana%100

    return cod, an_final

def calculeaza_cifra_control(cnp_final):
    constanta = "279146358279"
    suma = 0
    cnp_temporar = str(cnp_final)
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
        cod=0
        an_final=0
        cod,an_final=statistica_sex()#primele 2 variabile preiau valorile returnate de functia statistica_sex
        luna = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        judete_cnp = [judete for judete in range(1, 43)]
        numar_secvential=[i for i in range(0,1000)]
        statistica_sex()
        cnp_final=0
        cnp_final+=cod
        print("An ultimele 2 cifre",an_final)
        cnp_final=cnp_final*100+an_final
        luna_aleasa=random.choice(list(luna.keys()))
       
        zi_aleasa=random.choice(list(range(1,luna[luna_aleasa]+1)))#daca nu pun +1 se duce numai pana la 11 pt ca range mereu se duce numai la n-1
        
        cnp_final=cnp_final*100+luna_aleasa #random.choice=alege un element random din lista|random.randint(a,b)-alege un nr random din intervalul dat
        cnp_final=cnp_final*100+zi_aleasa
        
        judet_procentaj=[1.48,1.87,2.81,2.81,2.50,1.26,1.88,2.50,1.45,1.91,1.25,1.30,3.30,3.12,0.96,2.26,2.82,2.31,1.24,1.51,1.41,1.81,1.15,4.40,2.47,2.08,1.08,2.40,2.14,1.77,3.31,1.50,0.97,1.83,2.87,1.53,3.11,0.88,1.80,1.68,1.63,9.72]#procentaj de populatie din judetele din Romania

        #judete_cnp=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]
        judet_aleatoriu=random.choices(judete_cnp,weights=judet_procentaj,k=1)[0]
        cnp_final=(cnp_final*100)+judet_aleatoriu
        numar_aleatoriu=random.choice(numar_secvential)
        cnp_final=cnp_final*1000+numar_aleatoriu
        #cifra_control=calculeaza_cifra_control(cnp_final)
        cifra_control=0
        cnp_final=cnp_final*10+cifra_control
        #lista_cnp.append([cnp_final,len(str(cnp_final))])
        if len(str(cnp_final))==14:
            lista_cnp.append(cnp_final)
            print("Codsex:",cod,"An:",an_final,"Luna:",luna_aleasa,"Zi:",zi_aleasa,"judeet:",judet_aleatoriu,"Numar:",numar_aleatoriu)
            print(cnp_final)
        return lista_cnp

    
    


if __name__ == "__main__":
        for i in range(1000):
            generare_cnp()