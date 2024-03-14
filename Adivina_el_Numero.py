from random import randint

Eleccion = int(input("Por favor ingrese un número del 1 al 30: "))

X = randint(1, 30)

# Bucle para volver a intentar
while Eleccion != X:
    if X > Eleccion:
        print("El número ingresado es menor.")
    else:   
        print("El número ingresado es mayor.")
    Eleccion = int(input("Por favor ingrese un número del 1 al 30: "))
    if X == Eleccion:
        print("¡Has acertado el número!", X)
