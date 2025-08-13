import tkinter
from tkinter import *
from tkinter import messagebox
from validacionU import *
from arreglos import *


def crear_ventana2(ventana2):

    ventana2.title("Abuelitos Plenos")
    ventana2.geometry("400x500")
    ventana2.configure(background="#fbdfdf")

    regis = Label(ventana2, text="Ingrese sus datos para registrarse", bg="indian red", fg="black", font=("arial", 16))
    regis.place(in_=ventana2, anchor="c", relx=0.5, rely=0.1)
    regis.config(width=200)

    registro = Frame(ventana2, bd=1, relief=RAISED, background="#58D68D")
    registro.place(in_=ventana2, anchor="c", relx=0.5, rely=0.5)

    #registro de usuario y contraseña
    #usuario
    registrolabel = Label(registro, text="Crear Usuario", background="#7DCEA0")
    registrolabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    regisusuario= Entry(registro)
    regisusuario.grid(row=0, column=1, padx=10, pady=10)
    regisusuario.config(justify="center")

    #contraseña
    contraseña = Label(registro, text="Crear Contraseña", background="#7DCEA0")
    contraseña.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    regicontraseña= Entry(registro)
    regicontraseña.grid(row=1, column=1, padx=10, pady=10)
    regicontraseña.config(show="*", justify="center")

    #edad
    edad = Label(registro, text="Elegir rango de Edad", background="#7DCEA0")
    edad.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    var2= StringVar(registro)
    var2.set("Seleccionar una opción")
    opciones2=[" 65 a 70 ", " 71 a 75 ", " 76 a 80 ", " 81 a 85 "]
    regiedad=OptionMenu(registro, var2, *opciones2)
    regiedad.grid(row=2, column=1, padx=10, pady=10)
    regiedad.config(justify="center")

    #enfermedad
    oplabel = Label(registro, text="Enfermedad", background="#7DCEA0")
    oplabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    var = StringVar(registro)
    var.set("Seleccionar una opción")
    opciones=[" Hipertensión ", " Obesidad ", " Cirugía ", " Diabetes "]
    opcion=OptionMenu(registro, var, *opciones)
    opcion.config(justify="center")
    opcion.grid(row=3, column=1, padx=10, pady=10)

    #boton de registrarse
    def validacion(usuario, password, edad, enfermedad):
        global usuin 
        global passin

        correcto=False
        cont = 0
        correcto2=False
        cont2 = 0
        verify = False
        

        while cont==0:
            if nickname(usuario) == True: 
                correcto=True
                cont = cont + 1
            else:
                cont = cont + 1


        while cont2==0:
            if clave(password) == True:
                correcto2=True
                cont2 = cont2 + 1
            else:
                cont2 = cont2 + 1
        
        if correcto == True and correcto2 == True:
            usuin.append(usuario)
            print(usuin)
            passin.append(password)
            print(passin)
            messagebox.showinfo("Registro Exitoso.", "\nlos Datos han sido guardados. \n\nPor favor regrese a la paguina anterior he inicie sesión")
            edadin.append(edad)
            print(edadin)
            enfermin.append(enfermedad)
            print(enfermin)
            regisusuario.delete(0, 'end')
            regicontraseña.delete(0, 'end')
            

    botonregistrar = Button(registro, text="Registrarse", command=lambda: validacion(regisusuario.get(), regicontraseña.get(), var2.get(), var.get()))
    botonregistrar.grid(row=4, column=0, sticky="w", padx=10, pady=10)
    regisusuario.delete(0, 'end')
    regicontraseña.delete(0, 'end')
        
    #fin ventana2




def crear_barra2(ventana2, f1):
    
    barra = Frame(ventana2, bd=1, relief=RAISED)

    volver = Button(barra,text= "volver", command=f1)
    volver.pack(side=LEFT, padx=2, pady=2)

    def salir():
        respuesta = messagebox.askquestion("salir", "\n¿esta seguro de que desea salir?")
        if respuesta == "yes":
            ventana2.quit()
        

    salir = Button(barra,text= "salir", command=salir)

    salir.pack(side=RIGHT, padx=2, pady=2)
    
    barra.pack(side=BOTTOM, fill=X)




def iniciar_ventana2(principal):
    ventana2 = Toplevel()

    crear_ventana2(ventana2)
    def volver(event=None):
        ventana2.destroy()
        principal.update()
        principal.deiconify()

    crear_barra2(ventana2, volver)


