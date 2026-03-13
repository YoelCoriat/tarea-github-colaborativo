def input_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            if numero >= 0:
                return numero
            else:
                print("Por favor ingresar un numero positivo")
        except ValueError:
            print("Por favor ingresar un numero valido")

def run():
    print("\nMODULO DE CONTABILIDAD\n")

    ingresos = input_float("Ingrese el total de ingresos: ")
    gastos = input_float("Ingrese el total de gastos: ")

    balance = ingresos - gastos

    print("\nRESULTADO")
    print(f"Ingresos: {ingresos}")
    print(f"Gastos: {gastos}")
    print(f"Balance final: {balance}")

    if balance > 0:
        print("La empresa obtuvo ganancia.")
    elif balance < 0:
        print("La empresa tuvo pérdidas.")
    else:
        print("La empresa quedó en equilibrio.")
