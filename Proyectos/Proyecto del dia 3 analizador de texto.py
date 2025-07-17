#resolucion de el problema del dia 3

texto = input("Ingresa un texto de por lo menos 10 palabras")

#contar el numero total de caracteres en el texto
numero_caracteres = len(texto)

#Contar el número de caracteres sin incluir los espacios
numero_carac_sin_espacios= len(texto.replace(" ",""))

#contar el cantidad de vocales que hay en el texto
a=texto.count('a')
e=texto.count('e')
i=texto.count('i')
o=texto.count('o')
u=texto.count('u')
cantidad_vocales=a+e+i+o+u

#contar el numero total de palabras en el texto
numero_palabras=texto.strip().count(" ")+1

#eliminar la primera palabra
primer_espacio=texto.find(' ')
sin_primer_palabra = texto[5:]

#reemplazar todos los espacios por guines medios(-)
texto_guiones = texto.replace(" ","-")

#cambia las mayusculas por las minusculas y viceversa
texto_cambiado = texto.swapcase()

#mostrar el usuario los resultados
print('Estos son los resultados de su entrada')
print(f"El numero total  de caracteres son: {numero_caracteres}")
print(f"El numero de caracteres sin espacio son: {numero_carac_sin_espacios}")
print(f"La cantidad de vocales son: {cantidad_vocales}")
print(f"El numero de palabras en el texto son: {numero_palabras}")
print(f"El texto sin la primer palabra es:  {sin_primer_palabra}")
print(f"El texto intercambiado los espacio por giones medios es: {texto_guiones}")
print(f"El texto cambiando las letras mayusculas por la minusculas y viseversa es el siguiente: {texto_cambiado}")