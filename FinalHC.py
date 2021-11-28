##################################
##
##Autor: Ghina Garces
##Fecha: 11/28/2021
##Clase: Herramientas de comunicacion
##
##Este archivo permite recolectar datos para el test de aptitud y el posterior
##registro de un paciente a vacunar.
##
##################################

from sys import stdin
import fileinput

#Roles, descuento
roles = [["estudiante",50], ["profesor", 20]]

#Lista de productos
productos = [["Papas fritas", 1000],["Coca cola", 2300],["Croissant",1200],
             ["Arepa de queso",1800],["Arepa con carne",2000],["Milo", 1500],
             ["Almojabana",1200],["Jugo de naranja", 2500],["Brownie",2000],
             ["Platanitos",1300]]

"""Validar valores
Objetivo: No permitir que el usuario ingrese un valor diferente a los 2 especificados

Entradas:
prompt: string del mensaje a mostrar para cada intento
entrada: string que el usuario ingreso
valor1: string Primer valor aceptado
valor2: string segundo valor aceptado

Salida: string de la opcion elegida por el usuario
"""
def validar_valores(prompt, entrada, valor1, valor2):
    while entrada != valor1 and entrada != valor2:
        print(prompt)
        entrada = stdin.readline().strip()
    return entrada

"""Validar int
Objetivo: No permitir que el usuario ingrese un valor que no sea numerico

Entradas:
prompt: string del mensaje a mostrar para cada intento
entrada: string que el usuario ingreso

Salida: int del valor ingresado por el usuario
"""
def validar_int(entrada):
    val = 0
    done = False
    while not done:
        try:
            val = int(entrada)
            done = True
        except ValueError:
            print("Debe ser un numero mayor a 0")
            entrada = stdin.readline().strip()
    return val

"""Validar producto
Objetivo: No permitir que el usuario ingrese un producto que no exista

Entradas:
entrada: string que el usuario ingreso

Salida: int codigo del producto
"""
def validar_prod(entrada):
    val = 0
    done = False
    while not done:
        try:
            val = int(entrada)
            if val < len(productos) and val >= 0:
                done = True
            else:
                print("No existe un producto con ese codigo")
                done = False
        except ValueError:
            print("Debe ser un numero mayor a 0")
            #print(prompt)
            entrada = stdin.readline().strip()
    return val

"""Main"""
def main():
    rol = -1
    compras = []

    #cedula
    print("Numero de cedula: ",end =" ")
    cedula = validar_int(stdin.readline().strip())
    #rol
    print("Estudiante o profesor? [e: Estudiante/p: Profesor]")
    r = validar_valores("Estudiante o profesor? [e: Estudiante / p: Profesor]",stdin.readline().strip(),"e","p")
    if r == "e":
        rol = 0
    elif r=="p":
        rol = 1
        
    #productos
    print("Inserte codigo del producto a comprar:")
    print("Para terminar escriba 'END'")
    print("Productos:")
    #Print products
    for i in range(len(productos)):
        print(str(i)+": "+productos[i][0]+" $"+str(productos[i][1]))
    print()
    
    buy = True
    while buy:
        print("Codigo: ",end=" ")
        prodID = stdin.readline().strip()
        if prodID == "END":
            buy = False
        else:
            validar_prod(prodID)
            print("Cantidad: ",end=" ")
            cantidad = validar_int(stdin.readline().strip())
            compras.append([productos[int(prodID)], cantidad])
            

    #Imprimir recibo
    print()
    print("***********Recibo***********")
    print ("El "+str(roles[rol][0])+" con cedula "+str(cedula)+" debe pagar:")
    total = 0
    for i in compras:
        descuento = roles[rol][1]
        precio = i[0][1]*(descuento/100)
        total += precio
        print("  -"+i[0][0]+" x"+str(i[1])+" $"+str(precio))
    print("TOTAL: $"+str(total))
    print("****************************")
        
        
main()
