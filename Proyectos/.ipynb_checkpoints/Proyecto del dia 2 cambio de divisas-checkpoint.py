# primer proyecto del curso de python

# elaborar variables de nombre, fecha y saludo
nombre = "Ismael"
fecha = "10/12/2025"
saludo = "Buenos dias"

#concatenar las variables
bienvenida = saludo + nombre + "hoy" + fecha + "en que te puedo ayudar"

#dolares a convertir a euros
dolares = 35.0

#convertir dolares a euros
euros_a_recibir = dolares * 0.88
#calcular billetes y monedas
#suponiendo que solo hay billetes de 10 y monedas de 1 euro
billetes_10 = euros_a_recibir // 10
nuevos_euros = euros_a_recibir - (billetes_10 * 10)

billetes_1 = nuevos_euros // 1
num_monedas = nuevos_euros - billetes_1

monedas = num_monedas * 100

#imprimir resultados
print("Bienvenido al programa de conversión de divisas")
print(bienvenida)
print("dolares a entregar")
print(dolares)
print("euros a recibir")
print(euros_a_recibir)
print("billetes de 10 euros:")
print(billetes_10)
print("billetes de 1 euro:")
print(billetes_1)
print("monedas:")
print(monedas)
