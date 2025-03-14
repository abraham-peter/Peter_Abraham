#1980-2025
import random
import csv 
lista_cnp=[]
cnp_cu_nume_si_prenume={}
def generare_cnp():
    global lista_cnp
    ani_inainte_de_2000=[ani_inainte for ani_inainte in range(1950,2000)]
    ani_dupa_2000=[ani_dupa for ani_dupa in range(2001,2025)]
    luna={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    judete_cnp=[judete for judete in range(1,42)]
    nr_secvential=[sec for sec in range(0,1000)]
    for cnp_barbati in range(250001):
        cnp_barbati_generat_mai_mic_de_2000=0
        cnp_barbati_generat_mai_mic_de_2000+=1
        cnp_barbati_generat_mai_mic_de_2000*=100+random.choice(ani_inainte_de_2000)
        luna_aleasa=random.choice(list(luna.keys()))
        cnp_barbati_generat_mai_mic_de_2000*=100+random.choice(luna[luna_aleasa])
        cnp_barbati_generat_mai_mic_de_2000*=100+luna[luna_aleasa]
        cnp_barbati_generat_mai_mic_de_2000*=100+random.choice(judete_cnp)
        cnp_barbati_generat_mai_mic_de_2000*=1000+random.choice(nr_secvential)
        def calculeaza_cifra_control(cnp_barbati_generat_mai_mic_de_2000):
            constanta = "279146358279"
            suma = 0
            cnp_str = str(cnp_barbati_generat_mai_mic_de_2000)
            for i in range(12):
                suma += int(cnp_str[i]) * int(constanta[i])
            
            rest = suma % 11
            cifra_control = 1 if rest == 10 else rest
            
            return cifra_control

        
        cifra_control = calculeaza_cifra_control( cnp_barbati_generat_mai_mic_de_2000 )
        cnp_final =cnp_barbati_generat_mai_mic_de_2000 * 10 + cifra_control
        lista_cnp.append(cnp_final)

        cnp_barbati_generat_mai_mare_de_2000+=0
        cnp_barbati_generat_mai_mare_de_2000+=5
        cnp_barbati_generat_mai_mare_de_2000*=100+random.choice(ani_inainte_de_2000)
        luna_aleasa=random.choice(list(luna.keys()))
        cnp_barbati_generat_mai_mare_de_2000*=100+random.choice(luna[luna_aleasa])
        cnp_barbati_generat_mai_mare_de_2000*=100+luna[luna_aleasa]
        cnp_barbati_generat_mai_mare_de_2000*=100+random.choice(judete_cnp)
        cnp_barbati_generat_mai_mare_de_2000*=1000+random.choice(nr_secvential)
        def calculeaza_cifra_control(cnp_barbati_generat_mai_mare_de_2000):
            constanta = "279146358279"
            suma = 0
            cnp_str = str(cnp_barbati_generat_mai_mare_de_2000)
            for i in range(12):
                suma += int(cnp_str[i]) * int(constanta[i])
            
            rest = suma % 11
            cifra_control = 1 if rest == 10 else rest
            
            return cifra_control

        
        cifra_control = calculeaza_cifra_control( cnp_barbati_generat_mai_mare_de_2000 )
        cnp_final =cnp_barbati_generat_mai_mare_de_2000 * 10 + cifra_control
        lista_cnp.append(cnp_final)

    for cnp_femei in range(250001):
            cnp_femei_generat_mai_mic_de_2000=0
            cnp_femei_generat_mai_mic_de_2000+=1
            cnp_femei_generat_mai_mic_de_2000*=100+random.choice(ani_inainte_de_2000)
            luna_aleasa=random.choice(list(luna.keys()))
            cnp_femei_generat_mai_mic_de_2000*=100+random.choice(luna[luna_aleasa])
            cnp_femei_generat_mai_mic_de_2000*=100+luna[luna_aleasa]
            cnp_femei_generat_mai_mic_de_2000*=100+random.choice(judete_cnp)
            cnp_femei_generat_mai_mic_de_2000*=1000+random.choice(nr_secvential)
            def calculeaza_cifra_control(cnp_femei_generat_mai_mic_de_2000):
                constanta = "279146358279"
                suma = 0
                cnp_str = str(cnp_barbati_generat_mai_mic_de_2000)
                for i in range(12):
                    suma += int(cnp_str[i]) * int(constanta[i])
                
                rest = suma % 11
                cifra_control = 1 if rest == 10 else rest
                
                return cifra_control

            
            cifra_control = calculeaza_cifra_control( cnp_femei_generat_mai_mic_de_2000 )
            cnp_final =cnp_femei_generat_mai_mic_de_2000 * 10 + cifra_control
            lista_cnp.append(cnp_final)

            cnp_femei_generat_mai_mare_de_2000+=0
            cnp_femei_generat_mai_mare_de_2000+=5
            cnp_femei_generat_mai_mare_de_2000*=100+random.choice(ani_inainte_de_2000)
            luna_aleasa=random.choice(list(luna.keys()))
            cnp_femei_generat_mai_mare_de_2000*=100+random.choice(luna[luna_aleasa])
            cnp_femei_generat_mai_mare_de_2000*=100+luna[luna_aleasa]
            cnp_femei_generat_mai_mare_de_2000*=100+random.choice(judete_cnp)
            cnp_femei_generat_mai_mare_de_2000*=1000+random.choice(nr_secvential)
            def calculeaza_cifra_control(cnp_femei_generat_mai_mare_de_2000):
                constanta = "279146358279"
                suma = 0
                cnp_str = str(cnp_femei_generat_mai_mare_de_2000)
                for i in range(12):
                    suma += int(cnp_str[i]) * int(constanta[i])
                
                rest = suma % 11
                cifra_control = 1 if rest == 10 else rest
                
                return cifra_control

            
            cifra_control = calculeaza_cifra_control( cnp_femei_generat_mai_mare_de_2000 )
            cnp_final =cnp_femei_generat_mai_mare_de_2000 * 10 + cifra_control
            lista_cnp.append(cnp_final)
def alocare_prenume_nume(lista_cnp):
     prenume = ['Alexandru', 'Andrei', 'Adrian', 'Bogdan', 'Cristian', 'Daniel', 'Elena', 'Florin', 
               'Gabriel', 'George', 'Ioan', 'Ioana', 'Maria', 'Mihai', 'Nicolae', 'Paul', 'Radu', 
               'Stefan', 'Tudor', 'Victor']
    
     nume = ['Popescu', 'Ionescu', 'Popa', 'Pop', 'Constantin', 'Stan', 'Dumitrescu', 'Dima',
            'Gheorghiu', 'Iordache', 'Marin', 'Nistor', 'Oprea', 'Preda', 'Rusu', 'Stanciu',
            'Toma', 'Ursu', 'Vasile', 'Zamfir']
     prenume_aleasa=random.choice(prenume)
     nume_aleasa=random.choice(nume)
     nume_complet=prenume_aleasa+" "+nume_aleasa
     global cnp_cu_nume_si_prenume
     for cnp in lista_cnp:
         cnp_cu_nume_si_prenume[nume_complet]=lista_cnp[cnp]
     return cnp_cu_nume_si_prenume
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for item in my_list:
        writer.writerow([item])

                

        
        
        

        
        
        
    