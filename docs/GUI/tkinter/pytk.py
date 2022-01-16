
# [Grafos-2021/tkinter_test5-check-plot.py at main · makaires77/Grafos-2021](https://github.com/makaires77/Grafos-2021/blob/main/testes/tkinter_test5-check-plot.py)
# %%

"""
https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/?ref=lbp
https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
First, we need to create the figure object using the Figure() class. 
Then, a Tkinter canvas(containing the figure) is created using FigureCanvasTkAgg() class. 
Matplotlib charts by default have a toolbar at the bottom. 
When working with Tkinter, however, this toolbar needs to be embedded in the canvas separately using the NavigationToolbar2Tk() class.
In the implementation below, a simple graph for x=y²
"""
from tkinter import *
from math import factorial, log
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

# Cria a janela principal do Tkinter
window = Tk()

# Define o título da janela principal
window.title('Simulação do Problema do Caixeiro Viajante - TSP')

# Define as dimensões da janela principal
window.geometry("1200x600")

w = Label(window, text='Posição das Cidades', font="50")
# w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()

Button1 = Checkbutton(window, text="Aleatória",
                      variable=Checkbutton1,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)

Button2 = Checkbutton(window, text="Definida",
                      variable=Checkbutton2,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)


# Button1.pack()
# Button2.pack()


# plot function is created for plotting the graph in tkinter window
def plot():

    # criação da tela de figura que exibirá o gráfico
    fig = Figure(figsize=(10, 5), dpi=100)

    # função a ser plotada
    p = [i for i in range(101)]
    q = [i*100 for i in range(101)]
    y = [i**2 for i in range(101)]
    z = [factorial(i) for i in range(9)]

    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plot1 = fig.add_subplot(121)

    # comando para plotar o gráfico
    print("Checkbutton1", Checkbutton1, Checkbutton1.get(), dir(Checkbutton1))
    if Checkbutton1.get():
        plot1.plot(p, label='constante', linewidth=2)
    if Checkbutton2.get():
        plot1.plot(q, label='linear', linewidth=2)
    plot1.plot(y, label='polinomial', linewidth=2)
    plot1.plot(z, label='fatorial', linewidth=2)

# creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    # canvas.get_tk_widget().pack()
    canvas.get_tk_widget().grid(row=3, column=0)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    # canvas.get_tk_widget().pack()
    canvas.get_tk_widget().grid(row=4, column=0)


# Cria o botão que exibirá a plotagem
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# Posiciona o botão criado na janela principal
# plot_button.pack()

w.grid(row=0, column=0)
Button1.grid(row=1, column=1)
Button2.grid(row=1, column=2)
plot_button.grid(row=1, column=0)

# Dispara a interface com o usuário criada acima
window.mainloop()
