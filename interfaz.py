from tkinter import *

#root se pondra por cada cosa que se quiera modificar la ventana
root= Tk()
root.title("Samanta")
root.resizable(0,0)# 0,0 no se puede modificar ni de ancho y ni alto, 1,1 puede modificar de los dos lados
#root.resizable(true,false)#se modifica de ancho y no de alto
root.iconbitmap("fuego.ico")#agrega una imagen que debe ser extension ico


root.mainloop()#que no se cierre hasta que nosotros le digamos
