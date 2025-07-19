# AGENDA  DE CONTACTOS INTERACTIVA
# se deja la agenda por fuera del while para que no se inicalice a cada rato y se guarden los contactos
agenda = {}
# Hacer un menu con las opciones disponibles a hacer
while True:
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar un contacto")
    print("5. Mostrar todos los contactos")
    print("Ingrese 0 para salir")
    opcion = int(input("¿Que opcion deseas realizar?\n"))

    # creamos la agenda usando un diccionario, por que usaremos pares de datos

    nombre = ""
    telefono = ""

    # desarrollar cada una de las opciones
    # Añadir contacto

    if opcion == 1:
        nombre = input("Por favor ingresa el nombre del contacto\n")
        telefono = input("Ingresa el numero de telefono\n")
        agenda[nombre] =  telefono
        print("el contacto se ha agregado con exito\n")
    elif opcion == 2:
        nombre = input("ingrese el nombre del contacto que desea buscar\n")
        if nombre in agenda:
            telefono = agenda[nombre]
            print(f"El numero del contacto {nombre} es: {telefono}")
        else:
            print("El contacto que ingreso no existe")
    elif opcion == 3:
        nombre = input("Ingresa el nombre del contacto que deseas editar\n")
        if nombre in agenda:
            telefono = input("Ingresa nuevo telefono del contacto\n")
            agenda.update({nombre: telefono})
            print("El contacto fue actualizado")
        else:
            print("El contacto que ingreso no existe")
    elif opcion == 4:
        nombre = input("Ingresa el nombre del contacto que desea eliminar\n")
        if nombre in agenda:
            agenda.pop(nombre)
            print("El contacto a sido eliminado")
        else:
            print("El contacto que ingreso no existe")
    elif opcion == 5:
        print("Los contactos que se encuentran en la agenda son los siguientes")
        print(agenda.items())
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("opcion no valida")
