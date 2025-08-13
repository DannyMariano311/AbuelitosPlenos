import tkinter
from tkinter import *
from tkinter import messagebox
from arreglos import *



def nickname(usuario):
    global usuin
    valido = False
    
    long=len(usuario) 
    y=usuario.isalnum() 
        
    if y== False: 
        messagebox.showinfo("Error", "\nEl nombre de usuario puede contener solo letras y números")
            
    if long < 6: 
        messagebox.showinfo("Error", "\nEl nombre de usuario debe contener al menos 6 caracteres")
            
    if long > 12: 
        messagebox.showinfo("Error", "\nEl nombre de usuario no puede contener más de 12 caracteres")
            
    for i in range(len(usuin)):
        if usuario == usuin[i]:
            messagebox.showinfo("Error", "\nEl nombre de usuario ya existe, intenta con uno diferente")
            valido = True
            return False
    if valido = False:
        if long >5 and long <13 and y ==True:
            return False 
            usuin.append(usuario)



def clave(password):
    
    validar=False 
    long=len(password)
    espacio=False  
    mayuscula=False 
    minuscula=False 
    numeros=False 
    y=password.isalnum()
    correcto=True 
        
    for carac in password: 

        if carac.isspace()==True: 
            espacio=True 

        if carac.isupper()== True: 
            mayuscula=True 
                
        if carac.islower()== True: 
            minuscula=True 
                
        if carac.isdigit()== True: 
            numeros=True 
                            
    if espacio==True: 
            messagebox.showinfo("Error", "\nLa contraseña no puede contener espacios")
    else:
        validar=True 
                       
    if long <8 and validar==True:
        messagebox.showinfo("Error", "\n la contraseña debe tener Mínimo 8 caracteres")
        validar=False 

    if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
       validar = True 
    else:
       correcto=False 

    if validar == True and correcto==False:
       messagebox.showinfo("La contraseña elegida no es segura", "\n la contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

    if validar == True and correcto ==True:
       return True

