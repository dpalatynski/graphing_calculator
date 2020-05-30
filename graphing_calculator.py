from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import math

def zakoncz(args=None):
    """Funkcja, która jest odpowiedzialna za zakończenie działania programy po naciśnięcu przycisku typu Button."""
    masterpiece.quit()
    masterpiece.destroy()

def oddziel(x):
    """Funkcja, która podane przez użytownika wzory funkcji oddziela, kiedy pojawia się znak ';' oraz zwraca listę wzorów funkcji.
    Argumentem funkcji jest string.
    Funkcja zwraca listę."""
    return x.split(";")

def funkcje_matematyczne(x):
    """Funkcja jest odpowiedzialna za konwersje elementów w stringu (wzorów funkcji), aby program narysował funkcje na płótnie używając moduły numpy do funkcji matematycznych.
    Argumentem funkcji jest string.
    Funkcja zwraca string, który został przekonwertowany w odpowiedni sposób, aby funkcja została narysowana na płótnie.
    Obsługiwane funkcje i stałe matematyczne:
        sin(x)
        cos(x)
        tg(x)
        ctg(x)
        log(x)
        a^(x)
        e
        π
        """
    x=x.replace('sin','np.sin')
    x=x.replace('cos','np.cos')
    x=x.replace('tan','np.tan')
    x=x.replace('ln','np.log')
    x=x.replace('ctg','1/(np.tan)')
    x=x.replace('^','**')
    x=x.replace('e',str(math.e))
    x=x.replace('π',str(math.pi))
    x=x.replace(ent.get(),'x')
    return x

def rysuj(args=None):
    """Funkcja, która jest odpowiedzialna, za pojawienie się wykresów na płótnie.
    Funkcja pobiera wartości wpisane do odpowiednich etykiet i na ich podstawie reguluje długość osi OX i OY oraz rysuje wykresy funkcji.
    Rezultatem jest pojawienie się wykresów funkcji na płótnie."""
    try:
        wzor = funkcje_matematyczne(entwzor.get())  #pobieranie danych wpisanych przez użytkownika i konwersja funkcji podanych jako
        llimit = funkcje_matematyczne(left.get())   #string na funkcje matematyczne
        rlimit = funkcje_matematyczne(right.get())
        tlimit = funkcje_matematyczne(top.get())
        blimit = funkcje_matematyczne(bottom.get())

        fig = plt.figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(1, 1, 1)

        plt.grid()
        plt.ylim(ymin=eval(blimit),ymax=eval(tlimit))
        plt.xlim(xmin=eval(llimit),xmax=eval(rlimit))
        plt.title(etitle.get())
        plt.xlabel(xlabel.get())
        plt.ylabel(ylabel.get())

        x=np.arange(eval(llimit),eval(rlimit),0.01)

        g=0

        zestaw_funkcji = oddziel(wzor)  #lista funkcji potrzebnych do wyprintowania ich na płótno
        legenda = oddziel(entwzor.get()) #lista funkcji potrzebnych do legendy

        for i in zestaw_funkcji:
            if 'x' in i: #jeżeli funkcja zawiera w sobie zmienną x
                ax.plot(x,eval(i), label=legenda[g])
                g=g+1
            else: #jeżeli funkcja jest stała
                ax.plot([eval(llimit),eval(rlimit)],[eval(i),eval(i)],label=legenda[g])
                g=g+1

        if var.get()==1:
            plt.legend(loc='best')
        else:
            pass

        canvas = FigureCanvasTkAgg(fig, master=masterpiece)
        canvas.draw()
        canvas.get_tk_widget().grid(row=14,columnspan=16)
    except:
        messagebox.showinfo("Błąd","Niepoprawnie wprowadzone dane")


def callback(x):
    """Funkcja, która wpisuje do etykiety wprowadzającej wzór funkcji określone funkcje matematyczne.
    Argumentem funkcji jest string.
    Funkcja zwraca string, który pojawia się w etykiecie wprowadzającej funkcje."""
    widget=rysowanie_wykresow_funkcji.focus_get()
    if widget==entwzor:
        widget.insert('insert',x)
        widget.grid(row=1, column=4,columnspan=4)
    else:
        pass

def wyczysc(args=None):
    """Funkcja, która usuwa zawartość etykiet wprowadzających dane"""
    widget=rysowanie_wykresow_funkcji.focus_get()
    if widget==entwzor:
        widget.delete(0, END)
    elif widget==right:
        widget.delete(0, END)
    elif widget==left:
        widget.delete(0, END)
    elif widget==bottom:
        widget.delete(0, END)
    elif widget==top:
        widget.delete(0, END)
    elif widget==ent:
        widget.delete(0, END)
    elif widget==xlabel:
        widget.delete(0, END)
    elif widget==ylabel:
        widget.delete(0, END)
    elif widget==etitle:
        widget.delete(0, END)
    else:
        pass

######################
#
#
# Interfejs graficzny
#
#
######################

masterpiece = Tk()  #okno
masterpiece.title("Rysowanie wykresów funkcji") #tytuł
masterpiece.geometry("+0+0")

fig = plt.figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
plt.grid()
plt.title("Wpisz wzór funkcji w odpowiednim miejscu")

canvas = FigureCanvasTkAgg(fig, master=masterpiece)
canvas.draw()
canvas.get_tk_widget().grid(row=14,columnspan=16)

rysowanie_wykresow_funkcji = Label(masterpiece, text="Rysowanie wykresów funkcji", font=("Arial",30),foreground="green") #napis główny
rysowanie_wykresow_funkcji.grid(row=0,columnspan=16)


Label(masterpiece, text="Podaj wzór funkcji:").grid(row=1,column=0,columnspan=4) #napis + funkcja (entwzor)
entwzor = Entry(masterpiece)
entwzor.grid(row=1, column=4,columnspan=4)

Label(masterpiece, text="Zmienna:").grid(row=2,column=0,columnspan=4) #zmienna (ent)
v = StringVar(masterpiece, value='x')
ent = Entry(masterpiece, textvariable=v)
ent.grid(row=2, column=4,columnspan=4)

var=IntVar()
c=Checkbutton(masterpiece,text="Legenda",variable=var,onvalue = 1, offvalue = 0)
c.grid(row=2,column=10)

Label(masterpiece, text="Tytuł wykresu:").grid(row=1, column=8,columnspan=4) #tytuł wykresu (etitle)
v = StringVar(masterpiece, value='Tytuł wykresu')
etitle = Entry(masterpiece, textvariable=v)
etitle.grid(row=1, column=12,columnspan=4)


Label(masterpiece, text="Oś OX:").grid(row=5,column=0,columnspan=8)
Label(masterpiece, text="Oś OY:").grid(row=5,column=8,columnspan=8)

Label(masterpiece, text="Lewy zakres: ").grid(row=6,column=0,columnspan=4) #left
v = StringVar(masterpiece, value='-10')
left = Entry(masterpiece, textvariable=v)
left.grid(row=6, column=4,columnspan=4)

Label(masterpiece, text="Prawy zakres: ").grid(row=7,column=0,columnspan=4) #right
v = StringVar(masterpiece, value='10')
right = Entry(masterpiece, textvariable=v)
right.grid(row=7, column=4, columnspan=4)

Label(masterpiece, text="Dolny zakres:").grid(row=6,column=8,columnspan=4) #bottom
v = StringVar(masterpiece, value='-10')
bottom = Entry(masterpiece, textvariable=v)
bottom.grid(row=6, column=12,columnspan=4)

Label(masterpiece, text="Górny zakres:").grid(row=7,column=8,columnspan=4) #top
v = StringVar(masterpiece, value='10')
top = Entry(masterpiece, textvariable=v)
top.grid(row=7, column=12,columnspan=4)

Label(masterpiece, text="Podpis osi OX:").grid(row=8,column=0,columnspan=4) #xlabel
v = StringVar(masterpiece, value='nazwa osi OX')
xlabel = Entry(masterpiece, textvariable=v)
xlabel.grid(row=8, column=4,columnspan=4)

Label(masterpiece, text="Podpis osi OY:").grid(row=8,column=8,columnspan=4) #ylabel
v = StringVar(masterpiece, value='nazwa osi OY')
ylabel = Entry(masterpiece, textvariable=v)
ylabel.grid(row=8, column=12,columnspan=4)

btn = Button(masterpiece,text='Koniec',command=zakoncz) #end
btn.grid(row=10, column=8,columnspan=8,sticky=N+S+E+W)

btn = Button(masterpiece, text='Oblicz', command=rysuj)
btn.grid(row=10, column=0,columnspan=8,sticky=N+S+E+W)

btn = Button(masterpiece,text="sin(x)",command=(lambda: callback('sin(x)')))
btn.grid(row=11, column=0,sticky=N+S+E+W)

btn = Button(masterpiece,text="tan(x)",command=(lambda: callback('tan(x)')))
btn.grid(row=11, column=4,sticky=N+S+E+W)

btn = Button(masterpiece,text="cos(x)",command=(lambda: callback('cos(x)')))
btn.grid(row=11, column=2,sticky=N+S+E+W)

btn = Button(masterpiece,text="ctg(x)",command=(lambda: callback('ctg(x)')))
btn.grid(row=11, column=6,sticky=N+S+E+W)

btn = Button(masterpiece,text="ln(x)",command=(lambda: callback('ln(x)')))
btn.grid(row=11, column=8,sticky=N+S+E+W)

btn = Button(masterpiece,text="π",command=(lambda: callback('π')))
btn.grid(row=11, column=14,sticky=N+S+E+W)

btn = Button(masterpiece,text="x^()",command=(lambda: callback('^()')))
btn.grid(row=11, column=10,sticky=N+S+E+W)

btn = Button(masterpiece,text="e",command=(lambda: callback('e')))
btn.grid(row=11, column=12,sticky=N+S+E+W)

btn = Button(masterpiece,text="+",command=(lambda: callback('+')))
btn.grid(row=12, column=0,sticky=N+S+E+W)

btn = Button(masterpiece,text="-",command=(lambda: callback('-')))
btn.grid(row=12, column=2,sticky=N+S+E+W)

btn = Button(masterpiece,text="*",command=(lambda: callback('*')))
btn.grid(row=12, column=4,sticky=N+S+E+W)

btn = Button(masterpiece,text="/",command=(lambda: callback('/')))
btn.grid(row=12, column=6,sticky=N+S+E+W)

btn = Button(masterpiece,text="(",command=(lambda: callback('(')))
btn.grid(row=12, column=8,sticky=N+S+E+W)

btn = Button(masterpiece,text=")",command=(lambda: callback(')')))
btn.grid(row=12, column=10,sticky=N+S+E+W)

btn = Button(masterpiece,text=".",command=(lambda: callback('.')))
btn.grid(row=12, column=12,sticky=N+S+E+W)

btn = Button(masterpiece,text="CE")
btn.grid(row=12, column=14,sticky=N+S+E+W)
btn.bind("<Button-1>", wyczysc)

masterpiece.mainloop()
