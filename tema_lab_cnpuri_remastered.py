import random
from collections import Counter
import csv
#Declare variabile globale
lista_cnp = []
dict_cnp = {}
hash_table_pe_mod1000 = {i: [] for i in range(1000)}
hash_table_judet={}
prenume_baieti = [
    "Andrei", "Mihai", "Gabriel", "Florin", "Cristian", "Alexandru", "Radu", 
    "Stefan", "Ionut", "Vlad", "Bogdan", "Daniel", "Paul", "Victor", "Emil", 
    "Ciprian", "Razvan", "George", "Lucian", "Doru"
]

prenume_fete = [
    "Elena", "Maria", "Ioana", "Andreea", "Cristina", "Raluca", "Diana", "Ana", 
    "Simona", "Lavinia", "Monica", "Oana", "Bianca", "Georgiana", "Alina", 
    "Claudia", "Denisa", "Gabriela", "Laura", "Nicoleta"
]

nume_familie = [
    "Popescu", "Ionescu", "Dumitrescu", "Stoica", "Radu", "Tudor", "Moldovan", 
    "Georgescu", "Marinescu", "Lazar", "Enache", "Filip", "Neagu", "Grigorescu", 
    "Petrescu", "Iliescu", "Serban", "Barbu", "Sandu", "Ciobanu"
]


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
    set_lista_cnp=set()
    while len(set_lista_cnp)<1000000:
        global lista_cnp
        global nume_familie
        global prenume_baieti
        global prenume_fete
        cod=0
        an_final=0
        cod,an_final=statistica_sex()#primele 2 variabile preiau valorile returnate de functia statistica_sex
        luna = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        judete_cnp = [judete for judete in range(0, 42)]
        numar_secvential=[i for i in range(0,1000)]
        cnp_final=0
        cnp_final+=cod
        cnp_final=cnp_final*100+an_final
        luna_aleasa=random.choice(list(luna.keys()))
        zi_aleasa=random.choice(list(range(1,luna[luna_aleasa]+1)))#daca nu pun +1 se duce numai pana la 11 pt ca range mereu se duce numai la n-1
        cnp_final=cnp_final*100+luna_aleasa #random.choice=alege un element random din lista|random.randint(a,b)-alege un nr random din intervalul dat
        cnp_final=cnp_final*100+zi_aleasa
        judet_procentaj=[1.48,1.87,2.81,2.81,2.50,1.26,1.88,2.50,1.45,1.91,1.25,1.30,3.30,3.12,0.96,2.26,2.82,2.31,1.24,1.51,1.41,1.81,1.15,4.40,2.47,2.08,1.08,2.40,2.14,1.77,3.31,1.50,0.97,1.83,2.87,1.53,3.11,0.88,1.80,1.68,1.63,9.72]#procentaj de populatie din judetele din Romania
        judet_aleatoriu=random.choices(judete_cnp,weights=judet_procentaj,k=1)[0]#alege un judet random din lista de judete cu procentele precizate
        cnp_final=(cnp_final*100)+judet_aleatoriu
        numar_aleatoriu=random.choice(numar_secvential)
        cnp_final=cnp_final*1000+numar_aleatoriu
        cifra_control=calculeaza_cifra_control(cnp_final)
        cnp_final=cnp_final*10+cifra_control
        set_lista_cnp.add(cnp_final)
    lista_cnp=list(set_lista_cnp)
        
    return lista_cnp
def asociaza_nume_la_cnp(lista_cnp):
    global dict_cnp
    for cnp in lista_cnp: #iau cnpurile din lista
        cnp_str = str(cnp)
        # ia prima valoare din cnp
        prima_cifra = int(cnp_str[0])
        if prima_cifra ==1 or prima_cifra == 5:
            prenume = random.choice(prenume_baieti)
        elif prima_cifra == 2 or prima_cifra == 6:
            prenume = random.choice(prenume_fete)
            
        nume = random.choice(nume_familie)
        nume_complet = f"{nume} {prenume}"
        
        dict_cnp[cnp] = nume_complet
    
    return dict_cnp

def afiseaza_cnp_si_nume(dict_cnp, filename="cnp_nume.csv"):
    # Deschidem un fișier CSV pentru scriere
    with open(filename, 'w', newline='') as csvfile:
        # Creăm un writer CSV
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['CNP', 'Nume', 'Prenume'])#definim headerul coloanelor
        
        for cnp, nume_complet in dict_cnp.items():#lucram cu fiecare pereche din dictionar
            nume_partial = nume_complet.split(' ', 1)#separam numele si prenumele
            nume = nume_partial[0]#primul element din lista
            prenume = nume_partial[1] if len(nume_partial) > 1 else ""#daca avem mai mult de un nume, prenumele va fi al doilea element din lista
            
            csv_writer.writerow([cnp, nume, prenume])#scriem in fisier
    
    print(f"Datele au fost scrise in fisierul {filename}")

def hash_table_pe_mod1000_functie(lista_cnp):
      global hash_table_pe_mod1000
      for cnp in lista_cnp:
          hash_value = cnp % 1000
          hash_table_pe_mod1000[hash_value].append(cnp)

      return hash_table_pe_mod1000


def cautare_hash_table_pe_mod1000(hash_table_pe_mod1000, cnp_random_de_cautat):
        counter_iteratii_lista=[]
        for cnp_random in cnp_random_de_cautat:
            iteratii=0
            for keys,values in hash_table_pe_mod1000.items():
                iteratii+=1
                for i in range(len(values)):
                    iteratii+=1
                    if cnp_random==values[i]:
                        counter_iteratii_lista.append(iteratii)
        if counter_iteratii_lista:
            min_iterations = min(counter_iteratii_lista)
            max_iterations = max(counter_iteratii_lista)
            print("Statistici de cautare")
            print(f"Minimum iterations: {min_iterations}")
            print(f"Maximum iterations: {max_iterations}")

def procentaj_pe_judete(lista_cnp,filename="procentaj_pe_judete.csv"):
    judete=[]
    for cnp in lista_cnp:
        string_judet=str(cnp)[7:9]
        judete.append(string_judet)
    counter_valori=Counter(judete)
    percentaj_judete = {key: format((count / len(lista_cnp)) * 100, '.2f') for key, count in counter_valori.items()}
    judete_dictyonary = {
    "00": "Alba", "01": "Arad", "02": "Arges", "03": "Bacau", "04": "Bihor", "05": "Bistrita-Nasaud", 
    "06": "Botosani", "07": "Braila", "08": "Brasov", "09": "Buzau", "10": "Caras-Severin", 
    "11": "Cluj", "12": "Constanta", "13": "Covasna", "14": "Dambovita", "15": "Dolj", 
    "16": "Galati", "17": "Giurgiu", "18": "Gorj", "19": "Harghita", "20": "Hunedoara", 
    "21": "Ialomita", "22": "Iasi", "23": "Ilfov", "24": "Maramures", "25": "Mehedinti", 
    "26": "Mures", "27": "Neamt", "28": "Olt", "29": "Prahova", "30": "Salaj", 
    "31": "Satu Mare", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timis", 
    "36": "Tulcea", "37": "Valcea", "38": "Vaslui", "39": "Vrancea", "40": "Bucuresti", 
    "41": "Bucuresti-Ilfov"
}
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Judet', 'Procentaj'])#definim headerul coloanelor
        for key, value in percentaj_judete.items():
            csv_writer.writerow([judete_dictyonary[key], value])#scriem in fisier
        print(f"Datele au fost scrise in fisierul {filename}")


if __name__ == "__main__":
    # Etapa 1
    generare_cnp()
    asociaza_nume_la_cnp(lista_cnp)
    afiseaza_cnp_si_nume(dict_cnp)
    procentaj_pe_judete(lista_cnp)
    # Etapa 2
    hash_table_pe_mod1000_functie(lista_cnp)
    # Etapa 3
    cnp_random_de_cautat=[]
    for _ in range(1000):
         cnp_random_de_cautat.append(random.choice(lista_cnp))
    cautare_hash_table_pe_mod1000(hash_table_pe_mod1000, cnp_random_de_cautat)
    
   
    