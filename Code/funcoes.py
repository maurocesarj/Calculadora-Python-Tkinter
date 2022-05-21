from tkinter import END
import imp

class calculadora(object):

    #numeros 
    def click_button(visor, numero):
        atual = visor.get()
        visor.delete(0, END)
        visor.insert(END, str(atual) + str(numero))

    #ponto
    def click_ponto(visor):
        visor.insert(END, ".")

    #Apagar (CE)
    def click_ce(visor):
        visor.delete(0, END)
