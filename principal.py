from funciones import *

regiones = ["NOA", "NEA", "Pampeana", "Cuyo", "Patagonia", "GBA"]

ejecutando = True
while ejecutando:
    print("---MENU---")
    print("1- Cargar ventas")
    print("2- Mostrar Ventas")
    print("3- Regiones con menos del 5%")
    print("4- Regiones con menos del 25%")
    print("5- Regiones con mas de 500 ventas ")
    print("6- Regiones con mas de 3000 ventas")
    print("7- Regiones por encima del promedio")

    opcion = input("Ingrese una opcion: ")
    while not validar_entero(opcion):
        opcion = input("Error. Ingrese una opcion: ")

    opcion = int(opcion)

    match opcion:
        case 1:
            ventas_ingresadas = cargar_ventas(regiones)
        case 2:
            print(mostrar_ventas(regiones, ventas_ingresadas))
        case 3:
            print(regiones_porcentaje(regiones, 5, ventas_ingresadas))
        case 4:
            print(regiones_porcentaje(regiones, 25, ventas_ingresadas))
        case 5:
            print(regiones_mayor_valor(regiones, 500, ventas_ingresadas))
        case 6:
            print(regiones_mayor_valor(regiones, 3000, ventas_ingresadas))
        case 7:
            print(regiones_encima_promedio(regiones, ventas_ingresadas))
        case 8:
            print(regiones_mas_compradoras(regiones, ventas_ingresadas))
        case _:
            ejecutando = False