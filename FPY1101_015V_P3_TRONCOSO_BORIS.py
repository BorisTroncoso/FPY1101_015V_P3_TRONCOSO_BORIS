import os
import random as rd

os.system("cls")

personas = []

def grabar():
    while True:
        try:
            nombre = input(" Ingrese su nombre: ")
        except:
            nombre = "a"
        if len(nombre) <8:
            print("intente un nombre mas largo")
        else:
            break
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
        except:
            edad = -1
        if edad >=0:
            break
        else:
            print("edad invalida")
    while True:
        caracteres = "abcdefghijklmnñopqrstuvwxyz"
        try:
            nif = input("Ingrese el NIF(debe contenter 8 numeros, un guion y 3 caracteres respectivamente): ")
        except:
            nif = "a"
        if len(nif) == 12:    
            #if int(nif[:8]) >= 00000000 and int(nif[:8]) <= 99999999:
                #if str(nif[-3:]).lower() in caracteres.split: 
                    #if str(nif). == "-":
                        print("si se pudo burro")
                        break
                
        else:
            print("Ingrese un valor valido")
    
    identificacion = {
                        "nombre" : {nombre},
                        "edad"   : {edad},
                        "NIF"    : {nif}
                    }
    personas.append(identificacion)
    print(f'Sus datos han sido guardados con exito{identificacion}')

def buscar():
    ingreso_nif = input("Ingrese su nif: ")
    buscar = False
    for persona in personas:
        if persona["NIF"] == ingreso_nif:
            if ingreso_nif[-2:].lower() == "sp":
                print("su informacion es:")
                print(f"Nombre : {persona["nombre"]} ")
                print(f"edad: {persona["edad"]}")
                print(f"Nif : {persona["NIF"]}")
                print("Pertenece a : España")
                buscar = True
                break
            else:
                print("su informacion es:")
                print(f"Nombre : {persona["nombre"]} ")
                print(f"edad: {persona["edad"]}")
                print(f"Nif : {persona["NIF"]}")
                print("Pertenece a : Union Europea")
                buscar = True
                break
        
    if not buscar:
            print("NIF no encontrado")
def imprimir():
    
    precio = rd.randint(1500,5000)
    while True:
        try:
            certificados = int(input("---Cual certificado desea?---\n1.- Nacimiento\n2.- Estado conyugal\n3.- Pertenencia a la union europea\nIngrese una opcion: "))
        except:
            certificados = 0
        if certificados <1 or certificados >3:
            print("ingrese una opcion valida")
        else:
            if certificados ==1:
                print(f"valor : {precio}")
                respuesta = input("desea llevarlo (responder si o no): ").lower()
            
                if respuesta == "si":
                    ingrese_nif = input("Ingrese su NIF: ")
                    for persona in personas:
                        if persona["NIF"] == ingrese_nif:
                            if ingrese_nif[-2:].lower() == "sp":
                                print("---Certificado de nacimiento---")
                                print(f"Nombre : {persona["nombre"]}")
                                print(f"Nif : {persona["NIF"]}")
                                print(f"Edad : {persona["edad"]}")
                                print(f"pertenece a : España ")
                                break
                            else:
                                print("---Certificado de nacimiento---")
                                print(f"Nombre : {persona["nombre"]}")
                                print(f"Nif : {persona["NIF"]}")
                                print(f"Edad : {persona["edad"]}")
                                print(f"pertenece a : Union Europea ")
                                break
                        else:
                            print("NIF no encontrado")
                elif respuesta == "no":
                    print("ok")
                    break
                else:
                    print("ingrese opcion valida")
                            
            elif certificados ==2:
                print(f"valor : {precio}")
                respuesta = input("desea llevarlo (responder si o no): ").lower()
            
                if respuesta == "si":
                    ingrese_nif = input("Ingrese su NIF: ")
                    for persona in personas:
                        if persona["NIF"] == ingrese_nif:
                            if ingrese_nif[-2:].lower() == "sp":
                                print("---Certificado de nacimiento---")
                                print(f"Nombre : {persona["nombre"]}")
                                print(f"Nif : {persona["NIF"]}")
                                print(f"Edad : {persona["edad"]}")
                                print(f"pertenece a : España ")
                                break
                            else:
                                print("---Certificado de nacimiento---")
                                print(f"Nombre : {persona["nombre"]}")
                                print(f"Nif : {persona["NIF"]}")
                                print(f"Edad : {persona["edad"]}")
                                print(f"pertenece a : Union Europea ")
                                break
                        else:
                            print("NIF no encontrado")
                elif respuesta == "no":
                    print("ok")
                    break
                else:
                    print("ingrese opcion valida")
                
            elif certificados ==3:
                print(f"valor : {precio}")
                respuesta = input("desea llevarlo (responder si o no): ").lower()
            
                if respuesta == "si":
                    ingrese_nif = input("Ingrese su NIF: ")
                    for persona in personas:
                        if persona["NIF"] == ingrese_nif:
                            if ingrese_nif[-2:].lower() == "sp":
                                print("---Certificado de nacimiento---")
                                print(f"Nombre : {persona["nombre"]}")
                                print(f"Nif : {persona["NIF"]}")
                                print(f"Edad : {persona["edad"]}")
                                print(f"pertenece a : España ")
                                break
                            else:
                                print("---Certificado de nacimiento---")
                                print(f"Nombre : {persona["nombre"]}")
                                print(f"Nif : {persona["NIF"]}")
                                print(f"Edad : {persona["edad"]}")
                                print(f"pertenece a : Union Europea ")
                                break
                        else:
                            print("NIF no encontrado")
                elif respuesta == "no":
                    print("ok")
                    break
                else:
                    print("ingrese opcion valida")
def salir():
    print("¡Gracias por visitarnos!")



while True:
    try:
        menu = int(input("---Bienvenido, Que desea hacer?---\n1.- Guardar datos\n2.- Buscar persona\n3.- Imprimir certificado\n4.- Salir\nIngrese su opcion: "))
    except:
        menu = 0
    if menu < 1 or menu >4:
        print("Opcion no valida")
    else:
        if menu == 1:
            print("guardar datos")
            grabar()

        elif menu == 2:
            print("Buscar persona")
            buscar()        

        elif menu == 3:
            print("Imprimir certificado")
            imprimir()

        elif menu == 4:
            salir()
            break