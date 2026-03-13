import contacuentos
import contabilidad
import trigonometria

while True:
    modulo = input("Cual modulo desea utilizar?\n\n"
                   "1 - Modulo de matematicas\n"
                   "2 - Modulo de cuentacuentos\n"
                   "3 - Modulo de contabilidad\n")

    if modulo == "1":
        trigonometria.run()
        break

    elif modulo == "2":
        contacuentos.run()
        break

    elif modulo == "3":
        contabilidad.run()
        break

    else:
        print("El modulo ingresado no existe. Por favor ingresar un modulo del 1-3: ")
