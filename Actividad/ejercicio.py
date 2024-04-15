# En esta area se encuentran todas las funciones del programa
# ------------------------------------------------------------

# Funcion para mostrar la bienvenida al programa
def bienvenida():
    print("")
    print("----------------------------------------")
    print("Bienvenido al programa multifuncional")
    print("----------------------------------------" + "\n" + "")



# Funcion para mostrar el menu de opciones principal
def menuOpciones():
    print("")
    print("Seleccione una opción:")
    print("1. Para entrar al area de lecturas de energia")
    print("2. Para mostrar la sumatoria de los divisores primos de un número")
    print("3. Para entrar al area de los números curiosos")
    print("4. Para finalizar el programa")
    print("")


# Funcion para mostrar el menu de opciones del area de lecturas de energía
def opcionesLecturas():
    print("Seleccione una opción:")
    print("1. Para ingresar una nueva lectura")
    print("2. Para calcular el promedio de lecturas")
    print("3. Para mostrar la lectura maxima")
    print("4. Para mostrar la lectura minima")
    print("5. Para mostrar la cantidad de lecturas registradas")
    print("6. Para salir del area de lecturas")
    print("")





# ------------------------------------------------------------


# Aqui se encuentra la ejecución del programa
# ------------------------------------------------------------

# Se llama al metodo de bienvenida
bienvenida()

registroLecturas = []

while True:

# Se llama al metodo de MenuOpciones para listar las opciones disponibles
    menuOpciones()

    opcion = int(input())


    # Condicional para la funcionalidad del programa
    if opcion == 1:
        print("----------------------------------------")
        print("Usted ha entrado al area de lecturas de energía")
        print("----------------------------------------")
        print("")

        while True:
            opcionesLecturas()

            segundaOpcion = int(input());
            print("")
            
            if segundaOpcion == 1:
                while True:
                    try:
                        nuevaLectura = float(input("Ingrese una nueva lectura en voltios: "))
                        registroLecturas.append(nuevaLectura)
                        break
                    except ValueError:
                        print("----------------------------------------")
                        print("Por favor, ingrese solo números.")
                        print("----------------------------------------")

                print("La lectura se ha sido registrada con exito")

            elif segundaOpcion == 2:
                suma = 0.0;
                for lectura in registroLecturas:
                    suma = suma + lectura

                # Obtener el tamaño de la lista
                tamano = len(registroLecturas)

                if tamano == 0:
                    print("----------------------------------------")
                    print("No hay lecturas registradas para obtener el promedio")
                    print("----------------------------------------")
                else:
                    promedio = (suma / tamano)
                    print("----------------------------------------")
                    print(f"El promedio de lecturas es de: {promedio} V")
                    print("----------------------------------------")


            elif segundaOpcion == 6:
                print("----------------------------------------")
                print("Ha salido del area de lecturas")
                print("----------------------------------------")
                break

    elif opcion == 4:
        print("----------------------------------------")
        print("El programa ha finalizado, vuelva pronto :)")
        print("----------------------------------------")
        break







# ------------------------------------------------------------