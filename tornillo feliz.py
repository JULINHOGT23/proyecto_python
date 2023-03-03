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
