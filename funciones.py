def validar_entero(ingreso: str):
    valido = True
    if ingreso == "":
        valido = False

    for i in ingreso:
        if i < "0" or i > "9":
            valido = False

    if valido and int(ingreso) <= 0:
        valido = False

    return valido

def cargar_ventas(lista_regiones):
    ventas_regiones = []
    for i in range(len(lista_regiones)):
        ingreso_ventas = input(f"Ingrese las ventas de {lista_regiones[i]}: ")
        while not validar_entero(ingreso_ventas):
            ingreso_ventas = input(f"Error. Ingrese las ventas de {lista_regiones[i]} : ")            

        ingreso_ventas = int(ingreso_ventas)

        ventas_regiones += [ingreso_ventas]
    
    return ventas_regiones


def ventas_totales(ventas):
    total_ventas = 0
    for i in range(len(ventas)):
        total_ventas += ventas[i]
    
    return total_ventas



def mostrar_ventas(lista_regiones, ventas):
    total = ventas_totales(ventas)
    mensaje = ""
    for i in range(len(lista_regiones)):
        porcentaje = calcular_porcentaje(ventas[i], total)
        mensaje += f"{lista_regiones[i]}: {ventas[i]} - Porcentaje: {porcentaje} \n"

    mensaje += f"Total de ventas: {total}\n"
    return mensaje


def calcular_porcentaje(ventas, totales):
    porcentaje = (ventas * 100) / totales
    return porcentaje

def regiones_porcentaje(lista_regiones, valor, ventas):
    total = ventas_totales(ventas)
    mensaje = ""
    encontro = False
    for i in range(len(ventas)):
        porcentaje = calcular_porcentaje(ventas[i], total)

        if porcentaje < valor:
            mensaje += F"{lista_regiones[i]}: {ventas[i]} - Porcentaje: {porcentaje}% \n"
            encontro = True

    if not encontro:
        mensaje = f"No hay regiones con menos del {valor}%"

    return  mensaje


def regiones_mayor_valor(lista_regiones, valor, ventas):
    mensaje = ""
    suma = 0
    cantidad = 0

    for i in range(len(ventas)):
        if ventas[i] > valor:
            mensaje += f"{lista_regiones[i]}: {ventas[i]} \n"
            suma += ventas[i]
            cantidad += 1

    if cantidad == 0:
        mensaje = f"No hay regiones con mas de {valor} ventas \n"

    else:
        promedio = suma / cantidad

        mensaje += f"Suma: {suma} \n -Cantidad = {cantidad} \n -Promedio: {promedio}\n"
        return mensaje


def regiones_encima_promedio(lista_regiones, ventas):
    total = ventas_totales(ventas)
    promedio = total / len(ventas)

    mensaje = f"Promedio: {promedio}\n"
    for i in range(len(ventas)):
        if ventas[i] > promedio:
            mensaje += f"{lista_regiones[i]}: {ventas[i]} \n"

    return mensaje

def regiones_mas_compradoras(lista_regiones, ventas):
    mas_compradora = 0
    mensaje = ""
    for i in range(len(ventas)):
        if ventas[i] >= mas_compradora:
            mas_compradora = ventas[i]
            mensaje += f"Pais mas comprador: {lista_regiones[i]}: {ventas[i]} \n"

    return mensaje