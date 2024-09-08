num = int(input("Siendo que 1 es lunes y 7 domingo ingrese un número y le diré si es un día laboral o no: "))
while num not in range(1,8):
    num = int(input("Porfavor, ingrese un número del 1 al 7: "))
if num in range(1,6):
    print("Es un día laboral")
elif num in range(6,8):
    print("No es un día laboral")