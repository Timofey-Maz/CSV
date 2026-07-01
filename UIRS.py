import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
def open_file(): #функция, поддерживающая открытие проводника и выбор файла
    command_res = filedialog.askopenfilename()
    if command_res:
        process_file(command_res)
def process_file(file_path): #функция считывания файла, сделанная циклом,а не "потоком" считывателей
    data = pd.read_csv(file_path, sep=";")
    col = data.columns.values
    for sID in range(1, 4): #цикл сбора информации с файла по считывателям
        a = data[data.sID == sID] # фильтрация файла по определенному считывателю
        time = a["internal_time"].values #создание массива времени
        print(f"СЧИТЫВАТЕЛЬ {sID}:")
        start_index = (sID - 1) * 7 + 10 #обозначение начальных и конечных столбцов по определенному считывателю
        end_index = start_index + 7
        for i in range(start_index, end_index): #Построение графиков (Аня, здесь твоя работа)
            c = a[str(col[i])].values
            print(str(col[i]), c)
            plt.figure(figsize=(240, 200))
            plt.plot(time, c)
            plt.ylabel(str(col[i]))
            plt.xlabel('Время')
            plt.title(f'График {col[i]} от времени')
            plt.show()
        print(time)
window = Tk() #Создание окна приложения
window.title("Приложение")
window.geometry('400x250')
btn = Button(window, text="Выберите файл", command=open_file) #Кнопка, активирующая функцию выбора и файла и его считывания
btn.pack(pady=20)
window.mainloop()
