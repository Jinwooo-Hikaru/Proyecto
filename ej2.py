numeroDeIntentos = 3
valido = False

for i in range(numeroDeIntentos):
    contrasena1 = input("Ingresa la contraseña: ")
    contrasena2 = input("Repita su contraseña: ")

    if contrasena1 == contrasena2:
        print("Gracias, Bienvenido")
        valido = True
        break
    else:
        print("Las contraseñas no coinciden. %d intentos restantes" % (numeroDeIntentos - i - 1))

if not valido:
    print("Has agotado los intentos.")