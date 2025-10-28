from tkinter import *
import os
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image


def open_files1():
    global f1
    f1 = askopenfile(mode='r', filetypes=[("excel files", "*.xlsx")])
    if f1 is not None:
        lbl_file1.config(text=f"Ранний файл\nСейчас загружен «{os.path.basename(f1.name)}»")


def open_files2():
    global f2
    f2 = askopenfile(mode='r', filetypes=[("excel files", "*.xlsx")])
    if f2 is not None:
        lbl_file2.config(text=f"Поздний файл\nСейчас загружен «{os.path.basename(f2.name)}»")


wnd = Tk()
wnd.title('Отчёт успеваемости')
imag = Image.open("./Images/background.jpg")
width = (int(imag.size[0]) // 2)
height = (int(imag.size[1]) // 2)
imag = imag.resize((width, height))
image = ImageTk.PhotoImage(imag)
panel = Label(wnd, image=image)
panel.pack(side="top", fill="both")
#panel.pack(side="top", fill="both", expand="no")
wnd.geometry(f'{width}x{height}')

def sravnit():  #функция сравнения 
    pass

btn_c1 = Button(text='Выбрать ранний файл', command=open_files1) #выбор файлов для сравнения
btn_c1.place(x=200, y=100)
btn_c2 = Button(text='Выбрать поздний файл', command=open_files2) #выбор файлов для сравнения
btn_c2.place(x=200, y=200)

btn_go = Button(text='Сравнить',command=sravnit) #кнопка запуска сравнения
btn_go.place(x=200, y=300)


lbl_file1 = Label(text="Ранний файл\nНа данный момент файл не загружен", bg="#f5f5f5") #отображение файл1
lbl_file1.place(x=width//2, y=height//3)

lbl_file2 = Label(text="Поздний файл\nНа данный момент файл не загружен", bg="#f5f5f5") #отображение файл2
lbl_file2.place(x=width//2, y=height//4)



# canvas = tk.Canvas(root, width=width, height=height)
# canvas.pack(side="top", fill="both", expand="no")
#
# canvas.create_image(0, 0, anchor="nw", image=image)
#
# # Создаем кнопку и размещяем ее в "окне" ("контейнере") на Canvas
# button = tk.Button(root, text='Quit', command=root.quit)
# canvas.create_window((250, 250), anchor="nw", window=button)
#
# # Создаем текст через create_text, в отличие от Label у него будет прозрачный фон
# canvas.create_text(100, 100, text="Cat", fill="Yellow", font="Verdana 14")


wnd.mainloop()
