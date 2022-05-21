import imp
from functools import partial
from funcoes import *
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import font

# criação da janela da calculadora
app = Tk()
app.title('Calculadora')


# visor da calculadora
visor = Entry(
    app, 
    bg="#0B0B0B",
    foreground='white',
    font=('verdana', 20, "bold"),
    bd=0)
visor.pack()
visor.place(x=15,y=35, height=60, width=242)






#Primeira fileira:
btn1 = Button(app, text='1', bg="black", pady=17, padx=18.5, foreground='white', bd=0, command=lambda: calculadora.click_button(visor, 1))
btn1.place(x=10, y=100)

btn2 = Button(app, text='2', bg="black", pady=17, padx=18.5, foreground='white', bd=0, command=lambda: calculadora.click_button(visor, 2))
btn2.place(x=10, y=155)

btn3 = Button(app, text='3', bg="black", pady=17, padx=18.5, foreground='white', bd=0, command=lambda: calculadora.click_button(visor, 3))
btn3.place(x=10, y=210)

btn0 = Button(app, text='0', bg="black", pady=17, padx=18.5, foreground='white', bd=0, command=lambda: calculadora.click_button(visor, 0))
btn0.place(x=10, y=265)



#Segunda fileira:
btn4 = Button(app, text='4', bg="black", pady=17, padx=18.5, foreground='white', bd=0, command=lambda: calculadora.click_button(visor, 4))
btn4.place(x=60, y=100)

btn5 = Button(app, text='5', bg="black", pady=17, padx=18.5, foreground='white',bd=0, command=lambda: calculadora.click_button(visor, 5))
btn5.place(x=60, y=155)

btn6 = Button(app, text='6', bg="black", pady=17, padx=18.5, foreground='white',bd=0, command=lambda: calculadora.click_button(visor, 6))
btn6.place(x=60, y=210)

btnponto = Button(app, text='.', bg="black", pady=17, padx=45.3, foreground='white',bd=0, command=lambda: calculadora.click_ponto(visor))
btnponto.place(x=60, y=265)



#Terceira fileira:
btn7 = Button(app, text='7', bg="black", pady=17, padx=18.5, foreground='white',bd=0, command=lambda: calculadora.click_button(visor, 7))
btn7.place(x=110, y=100)

btn8 = Button(app, text='8', bg="black", pady=17, padx=18.5, foreground='white',bd=0, command=lambda: calculadora.click_button(visor, 8))
btn8.place(x=110, y=155)

btn9 = Button(app, text='9', bg="black", pady=17, padx=18.5, foreground='white',bd=0, command=lambda: calculadora.click_button(visor, 9))
btn9.place(x=110, y=210)


#Quarta fileira:
btnsoma = Button(app, text='+', bg="#222222", pady=19, padx=19, foreground='white',bd=0, command=lambda: calculadora.click_soma(visor))
btnsoma.place(x=160, y=100)

btnsub = Button(app, text='-', bg="#222222", pady=22, padx=22, foreground='white',bd=0, command=lambda: calculadora.click_sub(visor))
btnsub.place(x=160, y=155)

btnmult = Button(app, text='x', bg="#222222", pady=17, padx=21, foreground='white',bd=0, command=lambda: calculadora.click_mult(visor))
btnmult.place(x=160, y=210)

btndiv = Button(app, text='/', bg="#222222", pady=17, padx=22, foreground='white',bd=0, command=lambda: calculadora.click_div(visor))
btndiv.place(x=160, y=264)


#botao do CE
btnce = Button(app, text='CE', bg="#222222", pady=99.43, padx=15, foreground='white',bd=0, command=lambda: calculadora.click_ce(visor))
btnce.place(x=210, y=100)

#botao do =
btnigual = Button(app, text='=', bg="#005D28", pady=14, padx=119, foreground='white',bd=0, command=lambda : calculadora.click_igual(visor))
btnigual.place(x=10, y=320)




app.geometry('275x380')
app.resizable(False, False)
app.configure(background='#0B0B0B')
app.mainloop()
