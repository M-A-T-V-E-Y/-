from tkinter import *
from read_files import open_file
import os
from tkinter.filedialog import askopenfile


def open_files1():
    global f1
    f1 = askopenfile(mode='r', filetypes=[("excel files", "*.xlsx")])
    if f1 is not None:
        lbl_file1.config(text=f"Загрузите файл. Сейчас загружен «{os.path.basename(f1.name)}»")


def open_files2():
    global f2
    f2 = askopenfile(mode='r', filetypes=[("excel files", "*.xlsx")])
    if f2 is not None:
        lbl_file2.config(text=f"Загрузите файл. Сейчас загружен «{os.path.basename(f2.name)}»")


wnd = Tk()
wnd.title('Отчёт успеваемости')
wnd.geometry('700x700')

def sravnit():  #функция сравнения 
    pass

<<<<<<< HEAD

btn_c1 = Button(text='Выбрать ранний файл', command=open_files1) #выбор файлов для сравнения
btn_c1.pack()
btn_c2 = Button(text='Выбрать поздний файл', command=open_files2) #выбор файлов для сравнения
btn_c2.pack()
=======
def choose():   #выбор файлов
    pass

btn_go = Button(text='Сравнить',command=sravnit) #кнопка запуска сравнения
btn_go.place(relx=0.1,rely=0.8)
#btn_go.pack()

btn_c = Button(text='Выбрать файлы',command=choose) #выбор файлов для сравнения
btn_c.place(relx=0.8,rely=0.8)
#btn_c.pack()
>>>>>>> 37c76c185ccc81a006c8b127a14622c2bf8ce712


lbl_file1 = Label(text="gfrdegr") #отображение файл1
lbl_file1.pack()

lbl_file2 = Label(text="r3wgfttre") #отображение файл2
lbl_file2.pack()

<<<<<<< HEAD
wnd.mainloop()
=======


wnd.mainloop()
>>>>>>> 37c76c185ccc81a006c8b127a14622c2bf8ce712
