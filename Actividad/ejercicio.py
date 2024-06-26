# Integrantes: Johan Ordoñez y Esneyder Ibarra

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


# Funcion para mostrar la entrada al area de lecturas de energía
def entradaLecturasEnergia():
    print("----------------------------------------")
    print("Usted ha entrado al area de lecturas de energía")
    print("----------------------------------------")
    print("")


# Funcion para mostrar el menu de opciones del area de lecturas de energía
def opcionesLecturas():
    print("Seleccione una opción:")
    print("1. Para ingresar una nueva lectura")
    print("2. Para calcular el promedio de lecturas")
    print("3. Para mostrar la lectura maxima")
    print("4. Para mostrar la lectura minima")
    print("5. Para mostrar las lecturas registradas")
    print("6. Para salir del area de lecturas")
    print("")


# Funcion para agregar una nueva lectura.
def agregarLectura(registroLecturas):
    while True:

        try:
            nuevaLectura = float(input("Ingrese una nueva lectura en voltios: "))
            registroLecturas.append(nuevaLectura)
            break
        except ValueError:
            print("----------------------------------------")
            print("Por favor, ingrese solo números.")
            print("----------------------------------------")

    print("La lectura ha sido registrada con exito")


# Funcion para mostrar el promedio de lecturas
def promedioLecturas(registroLecturas):
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


# Funcion para mostrar la lectura maxima registrada
def lecturaMax(registroLecturas):
    # Obtener el tamaño de la lista
    tamano = len(registroLecturas)
    if tamano == 0:
        print("----------------------------------------")
        print("No se han registrado lecturas aún")
        print("----------------------------------------")
    else:
        lecturaMaxima = max(registroLecturas)
        print("----------------------------------------")
        print(f"El valor de la lectura maxima es de: {lecturaMaxima} V")
        print("----------------------------------------")


# Funcion para mostrar la lectura minima registrada
def lecturaMin(registroLecturas):
    # Obtener el tamaño de la lista
    tamano = len(registroLecturas)
    if tamano == 0:
        print("----------------------------------------")
        print("No se han registrado lecturas aún")
        print("----------------------------------------")
    else:
        lecturaMinima = min(registroLecturas)
        print("----------------------------------------")
        print(f"El valor de la lectura minima es de: {lecturaMinima} V")
        print("----------------------------------------")


# Funcion para mostrar las lecturas registradas
def lecturasRegistradas(registroLecturas):
    # Obtener el tamaño de la lista
    tamano = len(registroLecturas)
    numeroLectura = 0
    if tamano == 0:
        print("----------------------------------------")
        print("No se han registrado lecturas aún")
        print("----------------------------------------")
    else:
        print("----------------------------------------")
        for lectura in registroLecturas:
            numeroLectura = numeroLectura + 1
            print(f"Lectura {numeroLectura}: {lectura} V")

        print("----------------------------------------")


# Funcion para salir del area de lecturas
def salirAreaLectura():
    print("----------------------------------------")
    print("Ha salido del area de lecturas :)")
    print("----------------------------------------")

# Funcion para salir del programa
def salirPrograma():
    print("----------------------------------------")
    print("El programa ha finalizado, vuelva pronto :)")
    print("----------------------------------------")


# Funcion para entrar al area de lecturas de energia.
def areaLecturasEnergia():

    entradaLecturasEnergia()

    while True:
        opcionesLecturas()

        segundaOpcion = int(input());
        print("")

#--------------------------------------------------------------------
        
        if segundaOpcion == 1:
            agregarLectura(registroLecturas)

#--------------------------------------------------------------------

        elif segundaOpcion == 2:
            promedioLecturas(registroLecturas)

#--------------------------------------------------------------------

        elif segundaOpcion == 3:
            lecturaMax(registroLecturas)

#--------------------------------------------------------------------

        elif segundaOpcion == 4:
            lecturaMin(registroLecturas)

#--------------------------------------------------------------------

        elif segundaOpcion == 5:
            lecturasRegistradas(registroLecturas)

#--------------------------------------------------------------------

        elif segundaOpcion == 6:
            salirAreaLectura()
            break


# Metodo para definir si un número es primo.
def numeroPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Metodo para sumar los divisores primos de un número
def sumaDivPrimos(numero):
    sumatoria = 0
    for i in range(1, numero + 1):
        if numero % i == 0 and numeroPrimo(i):
            sumatoria += i
    return sumatoria


# Funcion para sumar los divisores primos de un número.
def divisoresPrimos():
    print("----------------------------------------")
    print("Ingrese un número")
    print("----------------------------------------")
    print("")
    while True:
        try:
            numero = int(input())
            break
        except ValueError:
            print("----------------------------------------")
            print("Por favor, ingrese un valor valido")
            print("Vuelva a ingresar un número")
            print("----------------------------------------")
            print("")

    sumaTotal = sumaDivPrimos(numero)

    if sumaTotal == 0:
        print("----------------------------------------")
        print("El número ingresado no tiene divisores primos")
        print("----------------------------------------")
    else:
        print("----------------------------------------")
        print(f"La suma de los divisores primos del número ingresado es de: {sumaTotal}")
        print("----------------------------------------")


# Funcion para sumar los 
def sumaDiv(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def numeroCurioso(num):
    # Devuelve los números curiosos
    suma = sumaDiv(num)
    return suma == num

def mostarNumCuriosos(n):
    numerosCuriosos = []
    i = 1
    while len(numerosCuriosos) < n:
        if numeroCurioso(i):
            numerosCuriosos.append(i)
        i += 1
    return numerosCuriosos

def numerosCuriosos():
    print("---------------------------------------------------------------------")
    print("Ingrese el valor de números curiosos que desea conocer")
    print("---------------------------------------------------------------------")
    print("")
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print("---------------------------------------------------------------------")
            print("Por favor ingrese un valor valido")
            print("---------------------------------------------------------------------")
            print("")
    resultado = []
    print("---------------------------------------------------------------------")
    print("El calculo puede tardar unos minutos, por favor espere")
    print("---------------------------------------------------------------------")
    print("")
    resultado = mostarNumCuriosos(n)
    print(f"Los primeros {n} números curiosos son: {resultado}")

# ------------------------------------------------------------


# Aqui se encuentra la ejecución del programa
# ------------------------------------------------------------

# Se llama al metodo de bienvenida
bienvenida()

registroLecturas = []

while True:

# Se llama al metodo de MenuOpciones para listar las opciones disponibles
    menuOpciones()
    opcion = 0
    try:
        opcion = int(input())
        
    except ValueError:
            print("")


    # Condicional para la funcionalidad del programa
    if opcion == 1:

        areaLecturasEnergia()

    elif opcion == 2:

        divisoresPrimos()

    elif opcion == 3:

        numerosCuriosos()

    elif opcion == 4:

        salirPrograma()
        break

    else: 
        print("----------------------------------------")
        print("Ingrese una opción valida")
        print("----------------------------------------")

# ------------------------------------------------------------

# Integrantes: Johan Ordoñez y Esneyder Ibarra