# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox



lista = []

def guardar():
    n = nombre.get()
    a = apellidos.get()
    t = telefono.get()
    lista.append(n+"$"+a+"$"+t)
    escribirContacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado correctamente")
    nombre.set("")
    apellidos.set("")
    telefono.set("")
    consultar()
def eliminar():
    eliminado = conteliminar.get()
    borrado = False
    for elemento in lista:
        array = elemento.split("$")
        if(conteliminar.get() == array[2]):
            lista.remove(elemento)
            borrado = True
    consultar()

    escribirContacto()

    if borrado:
        messagebox.showinfo("Eliminar", "Elemento eliminado correctamente"+eliminado)



def consultar():
    r = Text(root, width=80, height=15)
    lista.sort()
    valores = []
    #encabezado
    r.insert(INSERT, "Nombre\t\tApellido \t\tTelefono\n")
    for elemento in lista:
        array = elemento.split("$")
        valores.append(array[2])
        r.insert(INSERT, array[0]+"\t\t"+ array[1]+"\t\t"+array[2]+"\t\n")
        r.place(x=20, y=200)
        spinTelefono = Spinbox(root, value=(valores), textvariable=conteliminar).place(x=320, y=50)
        if lista==[]:
            spinTelefono = Spinbox(root, value=(valores)).place(x=320, y=50)
        r.config(state=DISABLED)

def iniciarArchivo():
    archivo = open("contact.txt", "a")
    archivo.close()

def cargar():
    archivo = open("contact.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open("contact.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()



root = Tk()
nombre = StringVar()
telefono = StringVar()
apellidos = StringVar()
conteliminar = StringVar()
cf = "gray"
cl = "#FFF"

root.title = "Práctica TKINTER"
root.geometry("500x500")
root.configure(bg='gray')
etiquetaTitulo = Label(root, text="Contactos", bg=cf, fg=cl, font=("Helvetica", 16)).place(x=200, y=10)
etiquetaNombre = Label(root, text="Nombre", bg=cf, fg=cl).place(x=50, y=50)
cajaN = Entry(root, textvariable=nombre).place(x=100, y=50)
etiquetaApellido = Label(root, text="Apellido", bg=cf, fg=cl).place(x=50, y=80)
cajaApellido = Entry(root, textvariable=apellidos).place(x=100, y=80)
etiquetaTelefono = Label(root, text="Telefono", bg=cf, fg=cl).place(x=50, y=110)
cajaTelefono = Entry(root, textvariable=telefono).place(x=100, y=110)

etiquetaEliminar = Label(root, text="Telefono", bg=cf, fg=cl).place(x=270, y=50)
spinTelefono = Spinbox(root,text=conteliminar).place(x=320,y=50)
botonGuardar = Button(root, text="Guardar", command=guardar, bg="black",fg=cl).place(x=130, y=150)
botonEliminar = Button(root, text="Eliminar", command=eliminar, bg="black", fg=cl).place(x=350,y=80)

ttk.Button(root,text="Salir", command=quit).pack(side=BOTTOM)
#.App(root)  # Call to the App
iniciarArchivo()
cargar()
consultar()
root.mainloop()




# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
