from random import randint
randnum = randint(0,100)
respuesta = int(input("Adivina un número del uno al cien: "))
contador = 1
while respuesta != randnum:
    if respuesta > randnum:
        print("Más bajo...")
    elif respuesta < randnum:
        print("Más alto...")
    respuesta = int(input("Vuelve a intentar: "))
    contador = contador + 1

print("Correcto, número encontrado, cantidad de intentos", contador)