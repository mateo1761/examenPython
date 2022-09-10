frutas = []

for i in range(2):
    fruta = {}

    fruta['Nombre'] = input('Digite el nomre de la fruta: ')
    fruta['Color'] = input('Digite el color: ')
    fruta['Precio'] = int(input('Digite el precio: '))

    frutas.append(fruta)

frutas.reverse()
print(frutas)
