num = int(input("Ingrese un número y le diré si es primo o no: "))
contador = 0
for x in range(1, (num + 1)):
    if num % x == 0:
        contador = contador + 1
if num == 0:
    print("El cero no es primo porque no se puede dividir entre sí mismo. El cero es un numero aparte de todos.")
elif contador < 3:
    print(num, "si es un número primo")
else:
    print(num, "no es un número primo")