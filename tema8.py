import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import random

def create_visualization():
    window = tk.Tk()
    window.title("Vizualizare Sortare prin Selectie")
    window.geometry("800x600")

    fig = plt.figure(figsize=(12, 6))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Generate random data
    valori = random.randint(10, 50)
    lista = np.random.randint(0, 100, valori)
    x = np.arange(0, valori, 1)
    n = len(lista)
    
    def selection_sort():
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                plt.clf()
                plt.bar(x, lista, color='skyblue')
                plt.bar(min_idx, lista[min_idx], color='red')
                plt.bar(j, lista[j], color='yellow')
                plt.title('Sortare prin Selectie')
                plt.xlabel('Index')
                plt.ylabel('Valoare')
                canvas.draw()
                window.update()
                
                if lista[j] < lista[min_idx]:
                    min_idx = j
                    
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        
        plt.clf()
        plt.bar(x, lista, color='lightgreen')
        plt.title('Sortare prin Selectie')
        plt.xlabel('Index')
        plt.ylabel('Valoare')
        canvas.draw()

    start_button = tk.Button(window, text="Începe sortarea", background='red', command=selection_sort)
    start_button.pack(pady=10)

    window.mainloop()

create_visualization()
