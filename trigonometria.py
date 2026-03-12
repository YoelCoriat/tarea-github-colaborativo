import math
# Este programa funciona a traves de varias funciones que se ejecutan en un loop en run()
# input_float es el unico que puede ser un poco confuso, se usa como alternativa a input() donde realiza un loop hasta que el usuario ingrese un numero valido


def input_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            if numero >= 0:
                return numero
            else:
                print("Ingresar un numero positivo")
        except ValueError:
            print("Ingresar un numero valido")

def hallar_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

def hallar_cateto(hipotenusa, cateto):
    if cateto >= hipotenusa:
        return None
    return math.sqrt(hipotenusa**2 - cateto**2)

def calcular_area_triangulo(cateto_a, cateto_b):
    return (cateto_a * cateto_b) / 2

def run():
    primer_loop = True
    while True:
        if primer_loop:
            print("Que calculo desea realizar?\n\n")
        else:
            print("Que otro calculo desea realizar?\n\n")

        print("1 - Hallar hipotenusa de triangulo rectangulo\n"
        "2 - Hallar cateto faltante de triangulo rectangulo\n"
        "3 - Hallar area de triangulo rectangulo\n"
        "4 - Salir\n")
        calculo = input()

        # Hallar hipotenusa
        if calculo == "1":
            cateto_a_temp = input_float("Cateto A: ")
            cateto_b_temp = input_float("Cateto B: ")

            print(f"La hipotenusa de un triangulo rectangulo con los catetos {cateto_a_temp} y {cateto_b_temp} es: {round(hallar_hipotenusa(cateto_a_temp, cateto_b_temp), 2)}\n")
            primer_loop = False


        # Hallar cateto faltante
        elif calculo == "2":
            hipotenusa_temp = input_float("Hipotenusa: ")
            cateto_a_temp = input_float("Cateto A: ")

            cateto_b_temp = hallar_cateto(hipotenusa_temp, cateto_a_temp)
            if cateto_b_temp is None:
                print(f"Este triangulo no existe!")
            else:
                print(f"El cateto faltante de un triangulo rectangulo con hipotenusa {hipotenusa_temp} y cateto {cateto_a_temp} es: {round(cateto_b_temp, 2)}\n")
                primer_loop = False


        # Hallar area de un triangulo
        elif calculo == "3":
            cateto_a_temp = input_float("Cateto A: ")
            cateto_b_temp = input_float("Cateto B: ")
            print(f"El area de un triangulo rectangulo con los catetos {cateto_a_temp} y {cateto_b_temp} es de {round(calcular_area_triangulo(cateto_a_temp, cateto_b_temp), 2)}\n")
            primer_loop = False

        elif calculo == "4":
            break

        else:
            print("La opcion ingresada no existe. Por favor ingresar un numero de 1-4: ")