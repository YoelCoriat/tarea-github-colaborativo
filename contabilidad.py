def run():
    print("\nMODULO DE CONTABILIDAD\n")

    ingresos = float(input("Ingrese el total de ingresos: "))
    gastos = float(input("Ingrese el total de gastos: "))

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
