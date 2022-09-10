contador2 = 0
contador3 = 0

cantidadNumeros = int(input('Ingrese la cantidad de numeros: '))

for i in range(cantidadNumeros):

    numerosIngresados = int(input('Ingrese un numero: '))

    if (numerosIngresados % 3 == 0):
        contador3 += 1
    elif (numerosIngresados % 2 == 0):
        contador2 +=1


print(f'Cantidad de numeros multiplo de 3 fueron ingresados: {contador3}')
print(f'Cantidad de numeros multiplo de 2 fueron ingresados: {contador2}')
