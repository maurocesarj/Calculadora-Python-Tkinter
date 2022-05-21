from tkinter import END


class calculadora(object):

    # Números
    def click_button(visor, numero):
        atual = visor.get()
        visor.delete(0, END)
        visor.insert(END, str(atual) + str(numero))

    # Ponto
    def click_ponto(visor):
        visor.insert(END, ".")

    # Apagar (CE)
    def click_ce(visor):
        visor.delete(0, END)

    # Soma
    def click_soma(visor):
        primeiro_numero = visor.get()
        global p_numero
        global matematica
        matematica = "soma"
        p_numero = float(primeiro_numero)
        visor.delete(0, END)

    # Subtração
    def click_sub(visor):
        primeiro_numero = visor.get()
        global p_numero
        global matematica
        matematica = "sub"
        p_numero = float(primeiro_numero)
        visor.delete(0, END)

    # Divisão
    def click_div(visor):
        primeiro_numero = visor.get()
        global p_numero
        global matematica
        matematica = "div"
        p_numero = float(primeiro_numero)
        visor.delete(0, END)

    # Multiplicação
    def click_mult(visor):
        primeiro_numero = visor.get()
        global p_numero
        global matematica
        matematica = "mult"
        p_numero = float(primeiro_numero)
        visor.delete(0, END)

    # Igual
    def click_igual(visor):
        segundo_numero = visor.get()
        visor.delete(0, END)
        if matematica == "soma":
            visor.insert(0, p_numero + float(segundo_numero))
        elif matematica == "sub":
            visor.insert(0, p_numero - float(segundo_numero))
        elif matematica == "mult":
            visor.insert(0, p_numero * float(segundo_numero))
        elif matematica == "div":
            visor.insert(0, p_numero / float(segundo_numero))
