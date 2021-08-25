# -*- coding:utf -8 -*-
# !/usr/bin/python3
__version__ = 'Version: 1.0'
import tkinter as tk
from tkinter import filedialog as fd
def on_closing():
    root.destroy()
    savepass()
def ygy():
    a, b, c = add()
    data_one = b.get()
    data_two = c.get()
    a.destroy()
    return data_one, data_two
def add():
    n = kogda.get()
    if n == "Выбрать дату":
        window2 = tk.Tk()
        window2.title("Дата и время")
        window2.geometry("150x250")
        nn = LabelFrame(text="Выбрать Дату и Время")
        nn.pack()
        rr1 = Label(nn, text="Дата")
        rr1.pack()
        rr = Entry()
        rr.pack()
        rr2 = Label(nn, text="Время")
        rr2.pack()
        r3 = Entry()
        r3.pack()
        b4 = Button(nn, text="Готово!")
        b4.pack()
        return window2, rr, r3
    else:
        tt.insert(END, "Задача" + ' ' + ': ' + wait_what.get() + " Время: " + n + "\n")
def delete_all():
    tt.delete(1.0, END)
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

def savepass():
    file_name = fd.asksaveasfilename(filetypes=(("Текстовые документы", "*.txt"),
                                                ("Все файлы", "*.*")), defaultextension='')
    f = open(file_name, 'w')
    s = tt.get(1.0, END)
    f.write(s)
    f.close()

root = Tk()
root.title("Список дел (Активированно)")
root.geometry("400x700")
root.resizable(False, False)
todoride = LabelFrame(text="Записать дело")
todoride.pack()
w1 = Label(todoride,text="Что надо сделать")
w1.pack(pady=5)
wait_what = Entry(todoride)
wait_what.pack(padx=20, pady=5)
w2 = Label(todoride,text="Когда сделать?")
w2.pack(pady=5)
kogda = ttk.Combobox(todoride, values=("Неизвестно","Постоянно","В ближайший час", "Сегодня", "Завтра", "На неделе", "В этом году", "Выбрать дату"))
kogda.pack(padx=20, pady=5)
start = Button(todoride,text="Добавить задачу", command=add)
start.pack()
tt = Text(width=60, height=30)
tt.pack()
f = Button(text="Удалить все задачи", command=delete_all)
f.pack()
f2 = Button(text="Сохранить все задачи")
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()