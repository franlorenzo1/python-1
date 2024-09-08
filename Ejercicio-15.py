def div2(x):
    if x % 2 == 0:
        return True

def div3(x):
    num_sep = []
    num_sum = 0
    for i in x:
        num_sep.append(i)   
    for i in num_sep:
        num_sum += int(i)
    if num_sum % 3 == 0:
        return True

def div5(x):
    if (x[0-1]) in "05":
        return True
    else:
        return False

def div9(x):
    num_sep = []
    num_sum = 0
    for i in x:
        num_sep.append(i)   
    for i in num_sep:
        num_sum += int(i)
    if num_sum % 9 == 0:
        return True
    
def div10(x):
    if (x[0-1]) in "0":
        return True
    else:
        return False
    
divisibles = []

num = input("Ingrese un número y le diré por qué números es divisible: ")

if div2(int(num)) == True:
    divisibles.append(2)
if div3(num) == True:
    divisibles.append(3)
if div5(num) == True:
    divisibles.append(5)
if div2(int(num)) and div3(num) == True:
    divisibles.append(6)
if div9(num) == True:
    divisibles.append(9)
if div10(num) == True:
    divisibles.append(10)

print(f"{num} es divisible por {divisibles}")