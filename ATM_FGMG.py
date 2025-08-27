pin_correcto = "1234"
saldo = 1000
intentos = 3

while intentos > 0:
    pin = input("Ingrese su PIN: ")
    if pin == pin_correcto:
        print("Bienvenido al cajero automático\n")
        break
    else:
        intentos = intentos - 1
        print("PIN incorrecto. Intentos restantes:", intentos)
        if intentos == 0:
            print("Cuenta bloqueada")
            quit()

opcion = 0
while opcion != 4:
    print("\n1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Tu saldo es:", saldo)
    elif opcion == 2:
        retiro = float(input("Cantidad a retirar: "))
        if retiro <= saldo:
            saldo = saldo - retiro
            print("Retiro exitoso. Nuevo saldo:", saldo)
        else:
            print("No tienes suficiente dinero")
    elif opcion == 3:
        deposito = float(input("Cantidad a depositar: "))
        saldo = saldo + deposito
        print("Depósito exitoso. Nuevo saldo:", saldo)
    elif opcion == 4:
        print("Gracias por usar el cajero.")
    else:
        print("Opción no válida.")
