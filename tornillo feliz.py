from tkinter import *
from tkinter import messagebox as MessageBox

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

    
root.title('Ferretería El tornillo feliz') # nombre del titulo de mi ventana
    root.config(bg= "#BDDCE1") # background o fondo de mi ventana
#root.iconbitmap('imagen.ico')# imagen con el icono de mi ventana
    root.resizable(False,False) #Evita que se expanda mi ventana

    miFrame.pack() #empaquetando
    miFrame.config(bg = "#A4D8D4")#fondo de mi primer frame
    miFrame.config(cursor = "pirate") #miniatura del raton (pirata)

    
