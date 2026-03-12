# modulo de contabilidad es placeholder, lo pueden cambiar cuando quieran
run = True

while run:
    modulo = input("Cual modulo desea utilizar?\n\n"
                   "1 - Modulo de matematicas\n"
                   "2 - Modulo de cuentacuentos\n"
                   "3 - Modulo de contabilidad\n")

    if modulo == "1":
        run = False
        # funcion para ejecutar el modulo 1 importado

    elif modulo == "2":
        run = False
        # funcion para ejecutar el modulo 2 importado

    elif modulo == "3":
        run = False
        # funcion para ejecutar el modulo 3 importado

    else:
        print("El modulo ingresado no existe. Por favor ingresar un modulo del 1-3: ")
