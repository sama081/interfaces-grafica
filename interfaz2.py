from tkinter import *


root = Tk()
root.title("Samanta")

root.resizable(1,1)
root.iconbitmap("fuego.ico")


#frame
miFrame = Frame(root)
miFrame.pack(side="left",anchor="n")#side=en el lugar que aparecera el frame
miFrame.config(width=500, height=300)#tamaño de la ventana
miFrame.config(cursor="pirate")
miFrame.config(bg="red")#cambia el color de la ventana
miFrame.config(bd="20")#le pone el tamaño de un borde
miFrame.config(relief="ridge")#le pone color al borde

#la raiz
root.config(cursor="boat")
root.config(bg="blue")#cambia el color de la ventana
root.config(bd="25")#le pone el tamaño de un borde
root.config(relief="sunken")#le pone color al borde


root.mainloop()
