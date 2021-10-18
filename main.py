from tkinter import *
from tkinter import messagebox


def clicked1():
    messagebox.showinfo('Кнопка №1', 'Вы нажали на кнопку №1')


def clicked2():
    messagebox.showinfo('Кнопка №2', 'Ура! Кнопка №2 нажата')


def clicked3():
    messagebox.showinfo('Кнопка №3', 'Три из трёх')


window = Tk()
window.title("Тест")
window.geometry('400x250')

btn = Button(window, text='Кнопка №1', command=clicked1)
btn.grid(column=0, row=0)

btn = Button(window, text='Кнопка №2', command=clicked2)
btn.grid(column=0, row=1)

btn = Button(window, text='Кнопка №3', command=clicked3)
btn.grid(column=0, row=2)

window.mainloop()
