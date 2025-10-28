from tkinter import *

wnd = Tk()
wnd.title('Отчёт успеваемости')
wnd.geometry('700x700')

btn_go = Button(text='Сравнить') #кнопка запуска сравнения
btn_go.pack()

btn_c = Button(text='Выбрать файлы') #выбор файлов для сравнения
btn_c.pack()



lbl_file1 = Label() #отображение файл1
lbl_file1.pack()

lbl_file2 = Label() #отображение файл2
lbl_file2.pack()

wnd.mainloop()