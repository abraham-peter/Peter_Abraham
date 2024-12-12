import matplotlib.pyplot as plt
import time

def bubble_sort(lista):
    timpi_de_executie=[]
    iteratii=0
    sortat=False
    inceput=time.perf_counter()
    while not sortat:
        sortat=True
        for i in range(len(lista)-1):
            iteratii+=1
            inceput_iteratie=time.perf_counter()
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
                sortat=False
            sfarsit_iteratie=time.perf_counter()
            timpi_de_executie.append(sfarsit_iteratie-inceput_iteratie)
    return lista,iteratii,timpi_de_executie

lista=[10,24,1,5,7,9,100,3,2,1000]
if __name__=="__main__":
    lista,iteratii,timpi_de_executie=bubble_sort(lista)
    plt.figure(figsize=(10,10))
    plt.plot(range(iteratii),timpi_de_executie)
    plt.pause(0.001)
    plt.xlabel("Iteratii")
    plt.ylabel("Timp de executie (secunde)")
    plt.title("Timp de executie pentru bubble sort")
    plt.show()