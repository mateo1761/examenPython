print("***MENU***")
print("1. Agregar")
print("2. Mostrar")
print("3. Buscar y editar")
print("4. Buscar y eliminar")
print("0. Salir")
opcion = 100
#DATOS EMPANADA
#SABOR
#Ingredientes (x3)
#Precio de fabricación
#Precio de venta

productos = []
ingredientes = []

while(opcion != 0):
    producto = {}
    menu = int(input('Ingrese un numero: '))
    if(menu == 1):
        producto['codigo'] = int(input('Digite el codigo del producto: ' ))
        producto['nombre'] = input('Digite el nombre del producto: ' )
        producto['precio'] = int(input('Digite el precio del producto: ' ))

        productos.append(producto)
        print("Agregando producto")
    elif(menu == 2):
        print(productos)
    elif(menu == 3):
        for i in range(len(productos)):
            if productos[i] == 55:
                productos[i] = 60
    elif(menu == 4):
        print(productos)

        productos.clear()

        print(productos)
    elif(menu == 0):
        opcion = 0
        print('Saliste del programa')

else:
    print('Digite una opcion valida')
