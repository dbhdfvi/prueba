import numpy
import msvcrt

lista_rut = []
lista_nombredueño = []
lista_identificador = []
lista_nombremascota = []
lista_cantidad = []

def validar_rut():
    while True:
        try:
            rut = int(print("Ingrese su rut: "))
            if rut >= 7 and rut <=8:
                return rut
            else:
                print ("Error!! Su rut debe tener entre 7 y 8 digitos")
        except:
            print ("Error!! Debe ingresar números enteros!")

def validar_nombredueño():
    while True:
        try:
            nombredueño = str(print("Ingrese su nombre: "))
            if nombredueño >= 3: 
                return nombredueño
            else:
                print ("Error!! Su nombre debe tener más de 3 caracteres")
        except:
            print ("Error!!")         

def validar_identificador():
    while True:
        try:
            identificador = int(print ("Creando identificador: "))
            if identificador >= 1
                return identificador
            else:
                print ("")
        except:
            print ("")

def validar_nombremascota():
    while True:
        try:
            nombremascota = str(print("Ingrese el nombre de su mascota: "))
            if nombremascota >= 3
                return nombremascota
            else:
                print ("Error!! El nombre debe tener al menos 3 caracteres")
        except:
            print ("Error!!")

def validar_cantidad():
    while True:
        try:
            cantidad = int(print("Ingrese la cantidad de dias que permanecera su mascota: "))
            if cantidad >= 1
                return cantidad
            else:
                print ("Error!! Ingrese un número mayor o igual a 1")
        except:
            print ("Error!! Ingrese un número entero")

def validar_opcion():
    while True:
        try:
            opcion = int(print("Ingrese una opción:")) 
            if opcion in (1,2,3,4):
                return opcion
            else:
                print ("Error!! Debe ingresar un número del 1 al 4")
        except:
            print ("Error!! Debe ingresar números enteros!")       

def validar_retirarse():
    validar = print ("Ingrese su rut: ")
    if validar == lista_rut (x):
        for x in range (lista_rut):
            posicion = x
            pass
        total = int(print("Ingrese cantidad de dias alojados: "))
        pagar = total*15000
        print ("Su total a pagar es ",pagar)

def validar_buscar():
    validar = print ("Ingrese su rut: ")
    if validar == lista_rut (x):
        for x in range (lista_rut):
            posicion = x
            pass
        print ("Su mascota se encuentra en la habitacion: ",validar_habitacion(x))

def validar_habitacion():
    while True:
        try:
            habitacion = int(print("Ingrese la habitación en que desea hospedar a su mascota: "))
            if habitacion in (1,2,3,4,5,6,7,8,9,10): 
                return habitacion
            else:
                ("ERROR!")
        except:
            print ("Error! Debe ingresar un número entero")

def validar_grabar():
    lista_rut.append = (validar_rut)
    lista_nombredueño.append = (validar_nombredueño)
    lista_identificador.append = (validar_identificador)
    lista_nombremascota.append = (validar_nombremascota)
    lista_cantidad.append = (validar_cantidad)



print ("""Bienvenido a Mascota Segura
1. Grabar datos de la mascota
2. Buscar a la mascota
3. Retirar 
4. Salir""")


while True:
    opcion = validar_opcion
    pass

while True:
    if opcion == 1:
        validar_grabar
    elif opcion == 2:
        validar_buscar
    elif opcion == 3:
        validar_retirarse
    else:
        print("Gracias por visitar nuestra página!")
        break
    
