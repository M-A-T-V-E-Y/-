from tkinter import *

wnd = Tk()
wnd.title('Отчёт успеваемости')
wnd.geometry('700x700')

def sravnit():  #функция сравнения 
    pass

def choose():   #выбор файлов
    pass

btn_go = Button(text='Сравнить',command=sravnit) #кнопка запуска сравнения
btn_go.place(relx=0.1,rely=0.8)
#btn_go.pack()

btn_c = Button(text='Выбрать файлы',command=choose) #выбор файлов для сравнения
btn_c.place(relx=0.8,rely=0.8)
#btn_c.pack()



lbl_file1 = Label() #отображение файл1
lbl_file1.pack()

lbl_file2 = Label() #отображение файл2
lbl_file2.pack()



wnd.mainloop()