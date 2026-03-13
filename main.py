import contacuentos
import contabilidad
import trigonometria

# Yoel Coriat va a realizar el archivo de matematicas
# Maryane puede realizar el de contacuentos
# Y Jose puede realizar el ultimo de contabilidad, aunque puedes cambiar el modulo a que sea lo que quieras

while True:
    modulo = input("Cual modulo desea utilizar?\n\n"
                   "1 - Modulo de matematicas\n"
                   "2 - Modulo de cuentacuentos\n"
                   "3 - Modulo de contabilidad\n")

    # Debajo de cada condicional pueden ejecutar su modulo
    # Es decir, importan el archivo .py arriba al inicio del archivo y ejecutan una funcion como modulo1.run()
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
