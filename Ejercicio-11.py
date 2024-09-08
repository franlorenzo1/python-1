contraseña = "ricardito"
for x in reversed(range(1,4)):
    inicio = input(f"Usted tiene {x} intentos, ingrese la contraseña: ")
    if inicio == contraseña:
        print("Acceso Correcto")
        break
    elif x == 1:
        print("El acceso se ha bloqueado después de los 3 intentos")