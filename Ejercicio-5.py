num = int(input("Escribe un número y te diré si es divisible por dos: "))
if num == 0:
    print("Cero no es un número divisible")
elif num % 2 != 0:
    print(f"{num} no es divisible por 2")
elif num % 2 == 0:
    print(f"{num} si es divisible por 2")