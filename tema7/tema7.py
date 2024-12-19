import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import random

def create_visualization():
    window = tk.Tk()
    window.title("Vizualizare Sortare cu metoda Bulelor")
    window.geometry("800x600")

    fig = plt.figure(figsize=(12, 6))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Generate random data
    valori = random.randint(10, 50)
    lista = np.random.randint(0, 100, valori)
    x = np.arange(0, valori, 1)
    n = len(lista)
    
    def bubble_sort():
        sortat = False
        while not sortat:
            sortat = True
            for i in range(0, n-1):
                plt.clf()
                plt.bar(x, lista, color='skyblue')
                plt.title('Sortare prin metoda bulelor')
                plt.xlabel('Index')
                plt.ylabel('Valoare')
                canvas.draw()
                window.update()
                
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    sortat = False
        
        
        plt.clf()
        plt.bar(x, lista, color='lightgreen')
        plt.title('Sortare prin metoda bulelor')
        plt.xlabel('Index')
        plt.ylabel('Valoare')
        canvas.draw()

    
    start_button = tk.Button(window, text="Începe sortarea",background='red', command=bubble_sort)
    start_button.pack(pady=10)

    window.mainloop()

create_visualization()
