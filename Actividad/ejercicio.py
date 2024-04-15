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

# Se llama al metodo de MenuOpciones para listar las opciones disponibles
menuOpciones()

opcion = int(input())


# Condicional para la funcionalidad del programa
if opcion == 1:
    print("----------------------------------------")
    print("Usted ha entrado al area de lecturas de energía")
    print("----------------------------------------")
    print("")

    opcionesLecturas()

    segundaOpcion = int(input());
    print("")
    
    if segundaOpcion == 1:
        while True:
            try:
                nuevaLectura = float(input("Ingrese una nueva lectura en voltios: "))
                break
            except ValueError:
                print("Por favor, ingrese solo números.")

print(f"Ha ingresado la lectura: {nuevaLectura} V")







# ------------------------------------------------------------