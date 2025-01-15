import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


lista = []
is_sorting = False
is_paused = False


window = tk.Tk()
window.title("Vizualizator Algoritmi de Sortare")
window.geometry("800x600")


fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)

def update_visualization():
    ax.clear()
    ax.bar(range(len(lista)), lista)
    canvas.draw()

def randomize():
    global lista
    size = int(valoare_vizibila.get())
    lista = [random.randint(1, 100) for _ in range(size)]
    update_visualization()

def toggle_pause():
    global is_paused
    is_paused = not is_paused

def bubble_sort():
    global is_sorting
    if is_sorting:
        return
        
    is_sorting = True
    n = len(lista)
    
    def bubble_step(i, j):
        if is_paused:
            window.after(100, bubble_step, i, j)
            return
            
        if j < n - i - 1:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            update_visualization()
            speed = int((2.1 - speed_scale.get()) * 1000)
            window.after(speed, bubble_step, i, j + 1)
        elif i < n - 1:
            window.after(0, bubble_step, i + 1, 0)
        else:
            global is_sorting
            is_sorting = False
            
    window.after(0, bubble_step, 0, 0)
def selection_sort():
    global is_sorting
    if is_sorting:
        return
        
    is_sorting = True
    n = len(lista)
    
    def selection_step(current_idx):
        if is_paused:
            window.after(100, selection_step, current_idx)
            return
            
        if current_idx < n:
            min_idx = current_idx
            for j in range(current_idx + 1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
                    
            lista[current_idx], lista[min_idx] = lista[min_idx], lista[current_idx]
            update_visualization()
            delay_time = int((2.1 - speed_scale.get()) * 1000)
            window.after(delay_time, selection_step, current_idx + 1)
        else:
            is_sorting = False
            
    window.after(0, selection_step, 0)

def insertion_sort():
    global is_sorting
    if is_sorting:
        return
        
    is_sorting = True
    
    def insertion_step(current_idx):
        if is_paused:
            window.after(100, insertion_step, current_idx)
            return
            
        if current_idx < len(lista):
            key = lista[current_idx]
            j = current_idx - 1
            while j >= 0 and lista[j] > key:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
            
            update_visualization()
            delay_time = int((2.1 - speed_scale.get()) * 1000)
            window.after(delay_time, insertion_step, current_idx + 1)
        else:
            is_sorting = False
            
    window.after(0, insertion_step, 1)

def bogo_sort():
    global is_sorting
    if is_sorting:
        return
        
    is_sorting = True
    
    def is_sorted():
        return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))
    
    def bogo_step():
        if is_paused:
            window.after(100, bogo_step)
            return
            
        if not is_sorted():
            random.shuffle(lista)
            update_visualization()
            delay_time = int((2.1 - speed_scale.get()) * 1000)
            window.after(delay_time, bogo_step)
        else:
            global is_sorting
            is_sorting = False
            
    window.after(0, bogo_step)

def reset():
    global is_sorting, is_paused
    is_sorting = False
    is_paused = False
    randomize()
def start_sorting():
    algorithm = sortare_string.get()
    if algorithm == "Bubble Sort":
        bubble_sort()
    elif algorithm == "Selection Sort":
        selection_sort()
    elif algorithm == "Insertion Sort":
        insertion_sort()
    elif algorithm == "Bogo Sort":
        bogo_sort()


control_frame = ttk.Frame(window)
control_frame.pack(pady=10)

sortari = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Bogo Sort"]
sortare_string = tk.StringVar(value=sortari[0])
sortare_combobox = ttk.Combobox(control_frame, textvariable=sortare_string, values=sortari)
sortare_combobox.pack(pady=5)

valori = [i for i in range(10, 101, 5)]
valoare_vizibila = tk.StringVar(value='50')
size_combo = ttk.Combobox(control_frame, textvariable=valoare_vizibila, values=valori)
size_combo.pack(pady=5)

speed_frame = ttk.LabelFrame(control_frame, text="Viteza Sortării")
speed_frame.pack(pady=5)
speed_scale = ttk.Scale(speed_frame, from_=0.1, to=2.0, orient='horizontal')
speed_scale.pack(pady=5)

buttons_frame = ttk.Frame(control_frame)
buttons_frame.pack(pady=5)

buton_de_start=ttk.Button(buttons_frame, text="Start", command=start_sorting)
buton_de_start.pack(side=tk.LEFT, padx=5)
buton_de_pauza=ttk.Button(buttons_frame, text="Pauză", command=toggle_pause)
buton_de_pauza.pack(side=tk.LEFT, padx=5)
buton_de_reset=ttk.Button(buttons_frame, text="Reset", command=reset)
buton_de_reset.pack(side=tk.LEFT, padx=5)
buton_de_random=ttk.Button(buttons_frame, text="Randomizare", command=randomize)
buton_de_random.pack(side=tk.LEFT, padx=5)
buton_de_iesire=ttk.Button(buttons_frame, text="Ieșire", command=window.destroy)
buton_de_iesire.pack(side=tk.LEFT, padx=5)

canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


randomize()


window.mainloop()
