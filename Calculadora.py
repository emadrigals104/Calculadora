#Calculadora Esteban Madrigal

def salir():
    print("*****************Saliendo de la Calculadora**************")
    return exit()

print('**************Bienvenidos Usuarios****************')
print('************Esta calculadora realiza operaciones basicas************\n')

print('Que operacion desea hacer?')
print('a) Sumar')
print('b) Restar')
print('c) Multiplicar')
print('d) Dividir\n')

repetir= True
while True:
    while True:
        numero1 = input('Introduce un numero ---> ')
        numero2 = input('Introduce otro numero ---> ')
        if numero1.isdigit() == True and numero2.isdigit() == True:
            numero1 = float(numero1)
            numero2 = float(numero2)
            break

        else:
            print("Error, ingrese numeros")
            print('Que operacion desea hacer?')
            print('a) Sumar')
            print('b) Restar')
            print('c) Multiplicar')
            print('d) Dividir')
            print("e) Salir \n")

    opcion = input('Elija una opcion ---> ')
    if opcion == 'a':
        suma = numero1 + numero2
        print('Calculando...')
        print('El resultado es ', suma, "\n")

    elif opcion == 'b':
        resta = numero1 - numero2
        print('Calculando...')
        print('El resultado es ', resta, "\n")

    elif opcion == 'c':
        multi = numero1 * numero2
        print('Calculando...')
        print('El resultado es ', multi, "\n")

    elif opcion == 'd':
        if numero2 != 0:
            divi = numero1 / numero2
            print('Calculando...')
            print('El resultado es ', divi, "\n")
        else:
            print("Error, no se puede dividir por 0\n")


    else:
        print("Ingrese una opcion valida\n")

    repetir = input("Operación realizada con exito.Desea realizar otra operacion (si/no):   ")
    if repetir == "no":
        repetir= salir()

    else:
        print('\nQue operacion desea hacer?')
        print('a) Sumar')
        print('b) Restar')
        print('c) Multiplicar')
        print('d) Dividir\n')
