import tkinter
from tkinter import *
from tkinter import messagebox
from new2 import *
from registrarse import *
from arreglos import *
from validacionU import *


principal = Tk()

image=PhotoImage(file="abuelitos.gif")
image=image.subsample(3,5)
label=Label(image=image)




def crear_ventana(ventana):
    ventana.title("Abuelitos Plenos")
    ventana.geometry("400x500")
    ventana.configure(background="#fbdfdf")


def crear_barra(ventana):
    barra = Frame(ventana, bd=1, relief=RAISED)
    def salir():
        respuesta = messagebox.askquestion("salir", "\n¿esta seguro de que desea salir?")
        if respuesta == "yes":
            ventana.quit()

    salir = Button(barra,text= "salir", command=salir)

    salir.pack(side=RIGHT, padx=2, pady=2)
    barra.pack(side=BOTTOM, fill=X)


def crearpanel_login(ventana):
    
    #inicio panel login
    login = Frame(ventana, bd=1, relief= RAISED, background="indian red")
    login.place(in_=ventana, anchor="c", relx=0.5, rely=0.6)

    usuariolabel = Label(login, text="Usuario", background="indian red" )
    usuariolabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    ingresarusuario= Entry(login)
    ingresarusuario.grid(row=0, column=1, padx=10, pady=10)
    ingresarusuario.config(justify="center")

    passwordlabel = Label(login, text="Contraseña", background="indian red" )
    passwordlabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    passworusuario= Entry(login)
    passworusuario.grid(row=2, column=1, padx=10, pady=10)
    passworusuario.config(show="*", justify="center")

    #boton inicio de sesion

    def funcion_ingresar(usuario, password):
            #usuarios y contraseñas 
            global usuin
            global passin
            global enfermin
            global hipertension
            global obesidad
            global artritis
            global diabetes
            global edad1
            global edad2
            global edad3
            global edad4
            global numero
        
            valiusua = False
            valipass = False

            for i in range(len(usuin)):
                if usuario == usuin[i]:
                    valiusua = True
                     
                    if valiusua == True:

                        #parametro para validar la invocacion de dietas
                        if enfermin[i] == " Hipertensión ":
                            hipertension[0] = ("1")
                        else:
                            hipertension[0] = ("0")
                        print("h", hipertension)
                        if enfermin[i] == " Obesidad ":
                            obesidad[0] = ("1")
                        else:
                            obesidad[0] = ("0")
                        print("o", obesidad)
                        if enfermin[i] == " Cirugía ":
                            artritis[0] = ("1")
                        else:
                            artritis[0] = ("0")
                        print("a", artritis)
                        if enfermin[i] == " Diabetes ":
                            diabetes[0] = ("1")
                        else:
                            diabetes[0] = ("0")
                        print("d", diabetes)
                        
                        #parametro para validar la invocacion de ejercicios

                        if edadin[i] == " 65 a 70 ":
                            edad1[0] = ("1")
                        else:
                            edad1[0] = ("0")
                        print("1", edad1)
                        if edadin[i] == " 71 a 75 ":
                            edad2[0] = ("1")
                        else:
                            edad2[0] = ("0")
                        print("2", edad2)
                        if edadin[i] == " 76 a 80 ":
                            edad3[0] = ("1")
                        else:
                            edad3[0] = ("0")
                        print("3", edad3)
                        if edadin[i] == " 81 a 85 ":
                            edad4[0] = ("1")
                        else:
                            edad4[0] = ("0")
                        print("4", edad4)

            for j in range(len(passin)):
                if password == passin[j]:
                    valipass = True

              
            if valiusua == True and valipass == True:
                iniciar_ventana1(ventana)
                ventana.withdraw()
                
                
            elif not(usuario) and not(usuario.strip()) or (not(password) and not(password.strip())):
                messagebox.showinfo("Error de ingreso", "\nIngrese el usuario. \n\nIngrese el password.")
            else:
                messagebox.showinfo("Error de ingreso", "\nUsuario o Contraseña Incorrecta. \n\nIngrese un usuario valido o regrístrese.")
            
            
            ingresarusuario.delete(0, 'end')
            passworusuario.delete(0, 'end')


    botoningresar = Button(login, text="Ingresar", command=lambda: funcion_ingresar(ingresarusuario.get(), passworusuario.get()))
    botoningresar.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    #ayudas sirve para recuperar contraseña y corrar cuentas
    def ayudas():
        global usuin
        global passin
        global enfermin
        global hipertension
        global obesidad
        global artritis
        global diabetes
        global edad1
        global edad2
        global edad3
        global edad4
        global numero

        ventana_ayudas = Tk()
        ventana_ayudas.title("Ayudas")
        ventana_ayudas.geometry("300x300")
        ventana_ayudas.configure(background="#fbdfdf")

        info = Label(ventana_ayudas, text="Primero ingrese el nombre de usuario \ny a continuación seleccione la acción a ejecutar", background="indian red")
        info.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        usu = Entry(ventana_ayudas)
        usu.grid(row=1, column=0, padx=10, pady=10)
        usu.config(justify="center")

        def recuperar(usu):
            global usuin
            global passin
            ubi = 0

            for i in range(len(usuin)):
                if usu == usuin[i]:
                    ubi = ubi + 1
                    exito = Label(ventana_ayudas, text= "¡Exito!, aquí esta tu contraseña: ")
                    exito.grid(row=2, column=0, sticky="w", padx=10, pady=10)

                    exito2 = Label(ventana_ayudas, text= passin[i], background="indian red")
                    exito2.place(in_=ventana_ayudas, anchor="c", relx=0.68, rely=0.382)
                    exito2.config(justify="center")
                    
            if ubi == 0:
                messagebox.showinfo("Error", "\nEl usuario ingresado NO existe")

        def borrar_perfil(usu):
            global usuin
            global passin
            global enfermin
            
            ubi2 = 0
            for i in range(len(usuin)):
                if usu == usuin[i]:
                    ubi2 = ubi2 + 1
                    exito3 = Label(ventana_ayudas, text= "¡Exito! El usuario ha sido borrado correctamente ")
                    exito3.grid(row=2, column=0, sticky="w", padx=10, pady=10)

                    usuin[i] = 0
                    passin[i] = 0
                    enfermin[i] = 0
                    
                    
            if ubi2 == 0:
                messagebox.showinfo("Error", "\nEl usuario ingresado NO existe")
            


        olvido = Button(ventana_ayudas, text="Olvide mi contraseña", command= lambda: recuperar(usu.get()))
        olvido.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        borrar = Button(ventana_ayudas, text="Borrar perfil", command= lambda: borrar_perfil(usu.get()))
        borrar.grid(row=4, column=0, sticky="w", padx=10, pady=10)


    ayuda = Button(login, text="Ayudas", command= ayudas )
    ayuda.grid(row=4, column=2, sticky="w", padx=10, pady=10)

    #boton ingreso a registros
    def funcion_registro():
        iniciar_ventana2(ventana)
        ventana.withdraw()

    botonregristrar = Button(login, text="Registrarse", command= funcion_registro)
    botonregristrar.grid(row=4, column=0, sticky="w", padx=10, pady=3)

    #fin crear panel login


crear_ventana(principal)
crear_barra(principal)
label.pack()
crearpanel_login(principal)
principal.mainloop()