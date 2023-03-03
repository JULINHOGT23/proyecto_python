import calendar
import datetime
import time
from tkinter import *
from tkinter import messagebox as MessageBox


# Hora en tiempo real
def hora():
    
    class App(Frame):
        def __init__(self,master=None):
            Frame.__init__(self, master)
            self.master = master
            self.label = Label(text="", font=("Calibri", 20))
            self.label.place(x=470,y=30)
            self.update_clock()
            self.config(bg= "#BDDCE1")
 
        def update_clock(self):
            now = time.strftime("%H:%M:%S")
            self.label.configure(text=now)
            self.after(1000, self.update_clock)
           
 
    
    app=App(root)
    root.wm_title("Ferreteria")
    app.config(bg= "#BDDCE1")
    
    root.resizable(width=False, height=False)
    root.after(1000, app.update_clock)
    
   
# Calendario en tiempo real
def calendario():

     
# Obtenemos los valores del año y mes a mostrar
    año = datetime.date.today().year
    mes = datetime.date.today().month
 
    def escrbirCalendario(año,mes):
	# Asignamos el año y mes al calendario
	    str1 = calendar.month(año,mes)
 
	    label1.configure(text=str1)
 
    def mesAnterior():
	    global month,year
	    mes-=1
	    if mes==0:
		    mes=12
		    año-=1
 
	    escrbirCalendario(año,mes)
 
    def mesSiguiente():
	    global month,year
	    mes+=1
	    if mes==13:
		    mes=1
		    año+=1
 
	    escrbirCalendario(año,mes)
 
    root = Tk()
    root.title("Calendario")
    root.resizable(False,False)
    
# Lo posicionamos en un label
    label1 =Label(root, text="", font=('courier', 14, 'bold'), bg='white', justify=LEFT)
    label1.grid(row=1,column=1)
    
# ponemos los botones dendentro
    frame=Frame(root,bd=5)
   
    
    anterior = Button(frame,text="Anterior", command=mesAnterior)
    anterior.grid(row=1, column=1, sticky=W)
    siguiente =Button(frame,text="Siguiente", command=mesSiguiente)
    siguiente.grid(row=1, column=2)
    frame.grid(row=2,column=1)

    escrbirCalendario(año,mes)
 


def administrador():
    """De momento esta funcion está vacio """
    root = Tk() #root = nombre de mi raiz
    
root.title('Ferretería El tornillo feliz') # nombre del titulo de mi ventana
    root.config(bg= "#BDDCE1") # background o fondo de mi ventana
#root.iconbitmap('imagen.ico')# imagen con el icono de mi ventana
    root.resizable(False,False) #Evita que se expanda mi ventana


    miFrame = Frame(root)# primer frame en la funcion administrado
    miFrame.pack() #empaquetando
    miFrame.config(bg = "#A4D8D4")#fondo de mi primer frame
    miFrame.config(cursor = "pirate") #miniatura del raton (pirata)

    
