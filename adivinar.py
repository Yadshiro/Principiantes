# juego adivinar numero

import random

MINIMO = 1
MAXIMO = 10

numero_azar = random.randint(MINIMO, MAXIMO)
intentos = 0

while True:
    intento_usuario = int(input("Introduce el numero deseado"))
    intentos += 1
    if intento_usuario > numero_azar:
        print("Te has pasado el numero es mas pequeño que" + str(intento_usuario))
    elif intento_usuario < numero_azar:
        print("Te has quedado corto! El numero es ,mas grande que" + str(intento_usuario))
    else:
         break
    
    print("Has aceptado El numero era" + str(numero_azar))
    print(f"Has tardado ( La cantidad de intentos)numeros de intentos.")    

    
