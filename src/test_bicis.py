from bicis import *
from modulo_navegacion import *

### TEST BLOQUE 7.1: Lectura del fichero y carga y devolución de una lista con todos los registros leídos.

def mostrar_numero_registros_leidos(coleccion):
    i = 0
    for p in coleccion:
        i += 1

    print(f'\nSe han leido un total de {i} registros \n')
    print(f'Los tres primeros elementos del registro son: \n')
    for j in range(0,3):
        print(f'{coleccion[j]} \n')
    print(f'Los tres últimos elementos del registro son: \n')
    for k in range(-3,0):
        print(f'{coleccion[k]} \n')

### TEST BLOQUE 2: 3. Obtener una lista de uno de los campos sin repetir

def test_bloque2_3 (datos):
    print(f'Test Bloque 2, apartado 3: \n')
    print(f'Hay {len(lista_starting_stations(datos))} estaciones de inicio de trayecto diferentes. \n')
    print(lista_starting_stations(datos),'\n' )

### TEST BLOQUE 2: 4. Obtener una lista con dos o tres de los campos de cada registro en los que otro campo cumple determinada condición.

def test_bloque2_4 (datos, n = 5):
    print(f'Test Bloque 2, apartado 4: \n')
    print(f'Hay {len(lat_long(datos))} rutas de trayectos trazables. \nSe muestran los {n} primeros elementos de la lista: \n')
    lista_lat_lon = lat_long(datos)
    print(lista_lat_lon[:n],'\n')
    lista_lat_long_limpia = list(dict.fromkeys(lista_lat_lon))
    print(f'Espera unos segundos a que cargue el mapa de representación de rutas y estaciones... \n')
    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")
    plot_rutas(lista_lat_long_limpia[:n])
    sys.stdout = old_stdout
    

### TEST BLOQUE 3: 1. Calcular la suma de alguna propiedad numérica de los registros que cumplan determinada condición.

def test_bloque_3_1 (datos, n = 3):
    print(f'Test Bloque 3, apartado 1: \n')
    print(suma_bateria(datos,n),'\n')

### TEST BLOQUE 3: 2. Calcular el promedio de alguna propiedad numérica de los registros que cumplan determinada condición.

def test_bloque_3_2 (datos, n = 3):
    print(f'Test Bloque 3, apartado 2: \n')
    print(f'El nivel de bateria promedio es de: {promedio_bateria(datos,n)} % \n')

### TEST BLOQUE 4: 2. Obtener el registro (o algunos campos del registro) que contiene el valor máximo o mínimo de un campo determinado, de los registros que cumplen determinada condición.

def test_bloque_4_2 (datos):
    print(f'Test Bloque 4, apartado 2: \n')
    print(f'El registro con más kilómetros recorridos, estando la bicicleta dañada:\n')
    print(registro_maximos_kilometros_recorridos(datos),'\n')

### TEST BLOQUE 5: 1. Obtener una lista de registros (o algunos campos del registro) ordenada con los n registros con mayor (o menor) valor en un campo determinado. Donde 'n' es un parámetro que debe recibir la función.

def test_bloque_5_1 (datos, n = 3):
    print(f'Test Bloque 5, apartado 1: \n')
    print(f'Los {n} registros con mayor duración del tiempo de trayecto son:\n')
    print(registros_mas_duracion_trayecto(datos,n),'\n')

### TEST BLOQUE 6: 1. Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún campo(clave). A cada clave se le hará corresponder una lista con los registros que contienen esa clave.

def test_bloque_6_1 (datos, anyo = 2016):
    print(f'Test Bloque 6, apartado 1: \n')
    print(f'Diccionario con tipos de pase, mostrando los registros y filtrado por año ({anyo}):\n')
    print(tipo_de_pase(datos,anyo),'\n')

### TEST BLOQUE 6: 4. Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún campo(clave) y que haga corresponder a cada clave una lista, con los 'n' regitros, ordenados de mayor a menor o de menor a mayor por algún campo que no sea la clave.

def test_bloque_6_4 (datos, n = 2, anyo = 2017, mayor_a_menor_duracion = True):
    print(f'Test Bloque 6, apartado 4: \n')
    print(f'Diccionario con tipos de viajes, para el año {anyo}, mostrando los {n} primeros registros de trayectos ordenados', end=' ')
    if mayor_a_menor_duracion == True:
        print(f'de mayor a menor duración: \n')
    else:
        print(f'de menor a mayor duración: \n')
    print(tipo_de_viaje(datos,anyo,n,mayor_a_menor_duracion),'\n')

################################################################
#  Programa principal
################################################################
if __name__ == '__main__':

    datos = lectura_datos_csv('./data/dataset_bicis.csv')
    mostrar_numero_registros_leidos(datos) #Test Bloque 7_1

    test_bloque2_3(datos) #Test Bloque 2_3
    #test_bloque2_4(datos) #Test Bloque 2_4

    test_bloque_3_1(datos) #Test Bloque 3_1
    test_bloque_3_2(datos) #Test Bloque 3_2

    test_bloque_4_2(datos) #Test Bloque 4_2

    test_bloque_5_1(datos) #Test Bloque 5_1

    test_bloque_6_1(datos) #Test Bloque 6_1
    test_bloque_6_4(datos) #Test Bloque 6_4