import tkinter
from tkinter import *
from validacionU import *
from arreglos import *




def crear_ventana(ventanaD):
    global numero
    


    ventanaD.title("Abuelitos Plenos")
    ventanaD.geometry("1100x690")
    ventanaD.configure(background="#fbdfdf")               

    
    dietas = Canvas(ventanaD, bd=1, relief=RAISED, background="white")
    dietas.place(in_=ventanaD, anchor="c", relx=0.25, rely=0.42)
    
    abu1 = Label(dietas, text= ("Hola Abuelito, esta es la dieta recomendable para ti"), background= "indian red")
    abu1.grid(row=0, column=0, padx=10, pady=10)
    abu1.config(justify="center", font=27)
    
    from imagenes import image1
    from imagenes import image2
    from imagenes import image3
    from imagenes import image4


    if hipertension[0] == "1":
        labeldietas1=Label(dietas, image=image1)
        labeldietas1.grid(row=1, column=0, padx=10, pady=10)
            
    elif obesidad[0] == "1":
        labeldietas1=Label(dietas, image=image2)
        labeldietas1.grid(row=1, column=0, padx=10, pady=10)
            
    elif artritis[0] == "1":
        labeldietas1=Label(dietas, image=image3)
        labeldietas1.grid(row=1, column=0, padx=10, pady=10)

    elif diabetes[0] == "1":
        labeldietas1=Label(dietas, image=image4)
        labeldietas1.grid(row=1, column=0, padx=10, pady=10)


    ejercicios = Frame(ventanaD, bd=1, relief=RAISED, background="white")
    ejercicios.place(in_=ventanaD, anchor="c", relx=0.7, rely=0.45)

    
    abu2 = Label(ejercicios, text= ("Hola Abuelito, esta es la rutina recomendable para ti"), background= "indian red")
    abu2.grid(row=0, column=0, padx=10, pady=10)
    abu2.config(justify="center", font=27)


    from imagenes import image5
    from imagenes import image6
    from imagenes import image7
    from imagenes import image8

    if edad1[0] == "1":
        labelejer1=Label(ejercicios, image=image5)
        labelejer1.grid(row=1, column=0, padx=10, pady=10)
        
    elif edad2[0] == "1":
        labelejer2=Label(ejercicios, image=image6)
        labelejer2.grid(row=1, column=0, padx=10, pady=10)

    elif edad3[0] == "1":
        labelejer3=Label(ejercicios, image=image7)
        labelejer3.grid(row=1, column=0, padx=10, pady=10)

    elif edad4[0] == "1":
        labelejer4=Label(ejercicios, image=image8)
        labelejer4.grid(row=1, column=0, padx=10, pady=10)
    print(numero)
    
    #aqui se invocan las dietas y ejercicios
       

     
def crear_barra(ventanaD, f1):

    barra = Frame(ventanaD, bd=1, relief=RAISED)
        
    volver = Button(barra,text= "Cerrar Sesion", command=f1)
    volver.pack(side=LEFT, padx=2, pady=2)
    
    def salir():
        respuesta = messagebox.askquestion("salir", "\n¿esta seguro de que desea salir?")
        if respuesta == "yes":
            ventanaD.quit()
        

    salir = Button(barra,text= "salir", command=salir)

    salir.pack(side=RIGHT, padx=2, pady=2)
    
    barra.pack(side=BOTTOM, fill=X)



def iniciar_ventana1(principal):
    ventana1 = Toplevel()

    crear_ventana(ventana1)
    def volver(event=None):
        global numero
        ventana1.destroy()
        principal.update()
        principal.deiconify()
        numero = [0]
        print(numero)

    crear_barra(ventana1, volver)


    
    