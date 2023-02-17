#perev10vdr(num,p), perev10vrim(num), perevdrv10(num,p), perevrimv10(rim)

from perevod_10_v_dr import *
from perevod_dr_v_10 import *
from perevod_10_v_rim import *
from perevod_rim_v_10 import *
from tkinter import *


#окно
widw=600
heiw=700
window =Tk()
window.title('преобразование чисел') #название окна
window.geometry(f'{widw}x{heiw}') #размеры окна

#функции 

def Click1():

    lbl5['text'] = ent1.get()
    lbl5['text']= perev10vdr(lbl5['text'],ent1v2.get())
    
def Click2():
    lbl6['text'] = ent2.get()
    lbl6['text']= perevdrv10(lbl6['text'],ent2v2.get())
    
def Click3():

    lbl7['text']= perev10vrim(ent3.get())
def Click4():

    lbl8['text']= perevrimv10(ent4.get())



#текст
#выводит текст width размер поля, state можно ли вводить текст, bg=задний фон, font=шрифт
    
lbl = Label(window, text='выберите действие которое хотите выполнить', font=('arial bold', 15))
lbl.pack() #расположение

lblbtn1 = Label(window, text='n=', font=('arial bold', 15))
lblbtn1.place(x=65,y=165)

lblbtn2 = Label(window, text='n=', font=('arial bold', 15))
lblbtn2.place(x=65,y=315)

lbl1 = Label(window, text='перевод 10-ного числа в число с n-ой системой счисления', font=('arial bold', 10))
lbl1.place(x=10, y= 75)#расположение

lbl2 = Label(window, text='перевод числа в n-ой системе счисления в 10-ное число', font=('arial bold', 10))
lbl2.place(x=10, y= 225)#расположение

lbl3 = Label(window, text='перевод 10-ного числа в римское число', font=('arial bold', 10))
lbl3.place(x=10, y= 375)#расположение

lbl4 = Label(window, text='перевод римского числа в 10-ное число', font=('arial bold', 10))
lbl4.place(x=10, y= 525)#расположение


#кнопки
#выводит кнопку с текстом foregroun=цвет текста, bg-цвет фона height=высота, width=ширина, command=функция которая выполняется при нажатии

btn1 = Button(window, text='!!!',width=6, height=3, bg='red', command=Click1)
btn1.place(x=25,y=100) #расположение

btn2 = Button(window, text='!!!',width=6, height=3, bg='red', command=Click2)
btn2.place(x=25,y=250)#расположение

btn3 = Button(window, text='!!!',width=6, height=3, bg='red', command=Click3)
btn3.place(x=25,y=400) #расположение

btn4 = Button(window, text='!!!',width=6, height=3, bg='red', command=Click4)
btn4.place(x=25,y=550) #расположение

#зоны для ввода текста
# width размер поля, state можно ли вводить текст, bg=задний фон, font=шрифт

ent1 = Entry(window, width=10, bg='yellow', font=15)
ent1.place(x=100,y=115) #расположение

ent1v2 = Entry(window, width=10, bg='yellow', font=15)
ent1v2.place(x=100,y=165) #расположение


ent2 = Entry(window, width=10, bg='yellow', font=15)
ent2.place(x=100,y=265)#расположение

ent2v2 = Entry(window, width=10, bg='yellow', font=15)
ent2v2.place(x=100,y=315) #расположение

ent3 = Entry(window, width=10, bg='yellow', font=15)
ent3.place(x=100,y=415) #расположение

ent4 = Entry(window, width=10, bg='yellow', font=15) 
ent4.place(x=100,y=565) #расположение

#зоны вывода текста
# width размер поля, #borderwidth=bd границы , foreground=fg background=bd, font=шрифт, anchor=выравнивание по краю(северб, юг...), justify=выравнивание но работает когда не одна строка,
# relief=вид границы, wraplength=количество символов на линии до перехода на новый ряд

lbl5 = Label(window, width=26, fg='red', font=15, anchor='w', borderwidth=3, relief='sunken', wraplength=300)
lbl5.place(x=250,y=115) #расположение

lbl6 = Label(window, width=26, fg='red', font=15, anchor='w', borderwidth=3, relief='sunken', wraplength=300)
lbl6.place(x=250,y=265)#расположение

lbl7 = Label(window, width=26, fg='red', font=15, anchor='w', borderwidth=3, relief='sunken', wraplength=300)
lbl7.place(x=250,y=415) #расположение

lbl8 = Label(window, width=26, fg='red', font=15, anchor='w', borderwidth=3, relief='sunken', wraplength=300)
lbl8.place(x=250,y=565) #расположение



window.mainloop() #создает цикл окна
