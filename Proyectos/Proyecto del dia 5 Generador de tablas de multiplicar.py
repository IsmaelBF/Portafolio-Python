# funcion para calcular las tablas
def calcular_tablas(numero, limite):
    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero*i}")


def funcion_global():
    numero = int(input("Ingresa el numero de la tabla de multiplicar que quieres imprimir\n"))
    limite = int( input("Dime un limite hasta donde quieres llegar en la tabla de multiplicar\n"))
    calcular_tablas(numero, limite)


#ejecucion del programa
while True:
    opcion = int(input("Ingresa el 1 si quieres imprimir alguna tabla de multiplicar\nIngresa un numero diferente de 1 si quieres salir del programa\n"))
    if opcion != 1:
        break
    funcion_global()

