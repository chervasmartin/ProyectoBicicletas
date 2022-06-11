'''
Proyecto bicicletas de Los Angeles

Autor: Carlos Hervás Martín
Tutora: Belén Ramos Gutiérrez


'''

import csv
from collections import namedtuple
from matplotlib import pyplot as plt
import datetime as dt

Registro = namedtuple('Registro', 'trip_id,duration_in_seconds,start_time,end_time,starting_station_id,starting_station_latitude,starting_station_longitude,ending_station_id,ending_station_latitude,ending_station_longitude,bike_id,trip_route_category,passholder_type,kilometers_travelled,battery_level_at_start,battery_level_at_the_end,maximum_speed,minimum_speed,average_speed,new_user,damaged_bike,zip_codes,subscription_plan_duration')

def lectura_datos_csv(fichero):
    '''
    Lee el fichero csv y devuelve una lista de tuplas con nombre
    
    ENTRADA:
        @param fichero : ruta del fichero csv que contiene los datos en codificación utf-8
        @type fichero : str
    SALIDA:
        @return lista de datos
        @rtype [Registro(int, int, str, str, int, float, float, int, float, float, int, str, str, float, int, int, float, float, float, bool, bool, int, str)]
    
    '''
    datos = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for linea in f:
            trip_id, duration_in_seconds, start_time, end_time, starting_station_id, starting_station_latitude, starting_station_longitude, ending_station_id, ending_station_latitude, ending_station_longitude, bike_id, trip_route_category, passholder_type, kilometers_travelled, battery_level_at_start, battery_level_at_the_end, maximum_speed, minimum_speed, average_speed, new_user, damaged_bike, zip_codes, subscription_plan_duration = linea.split(';')
            trip_id = int(trip_id)
            duration_in_seconds = int(duration_in_seconds)
            start_time = dt.datetime.strptime(start_time
            , "%d/%m/%Y %H:%M")
            end_time = dt.datetime.strptime(end_time, "%d/%m/%Y %H:%M")
            starting_station_id = int(starting_station_id)
            starting_station_latitude = float(starting_station_latitude)
            starting_station_longitude = float(starting_station_longitude)
            ending_station_id = int(ending_station_id)
            ending_station_latitude = float(ending_station_latitude)
            ending_station_longitude = float(ending_station_longitude)
            bike_id = int(bike_id)
            kilometers_travelled = float(kilometers_travelled)/1000
            battery_level_at_start = int(battery_level_at_start)
            battery_level_at_the_end = int(battery_level_at_the_end)
            maximum_speed = float(maximum_speed)/100
            minimum_speed = float(minimum_speed)/100
            average_speed = float(average_speed)/100
            new_user = True if new_user == 'True' else False
            damaged_bike = True if damaged_bike == 'True' else False
            zip_codes = int(zip_codes)
            subscription_plan_duration = subscription_plan_duration.split('\n')
            subscription_plan_duration = subscription_plan_duration.pop(0)

            datos.append(Registro(trip_id, duration_in_seconds, start_time, end_time, starting_station_id, starting_station_latitude, starting_station_longitude, ending_station_id, ending_station_latitude, ending_station_longitude, bike_id, trip_route_category, passholder_type, kilometers_travelled, battery_level_at_start, battery_level_at_the_end, maximum_speed, minimum_speed, average_speed, new_user, damaged_bike, zip_codes, subscription_plan_duration))
    return datos


'''BLOQUE 2'''

    # 3. Obtener una lista de uno de los campos sin repetir.

def lista_starting_stations (datos):
    '''
        Recibe la lista de tuplas con nombre y devuelve una lista de todas las estaciones iniciales sin repetir.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
    SALIDA:
        @return lista de estaciones iniciales
        @rtype lista_starting_stations: [int,...]
    
    '''
    
    lista_starting_stations = [i.starting_station_id for i in datos]
    lista_starting_stations = set(lista_starting_stations)
    lista_starting_stations = list(lista_starting_stations)
    lista_starting_stations.sort()
    return lista_starting_stations

    # 4. Obtener una lista con dos o tres de los campos de cada registro en los que otro campo cumple determinada condición.

def lat_long (datos):
    '''
        Recibe la lista de tuplas con nombre y devuelve una lista de tuplas con langitudes y longitudes
        de los registros que tienen esa información.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
    SALIDA:
        @return lista de de tuplas con latitudes/longitudes iniciales y finales
        @rtype lista_Lat_long: [float, float, float, float]
    
    '''

    lista_lat_long = [(i.starting_station_latitude, i.starting_station_longitude, i.ending_station_latitude, i.ending_station_longitude) for i in datos if i.starting_station_latitude != 0.0 if  i.ending_station_latitude != 0.0]
    return lista_lat_long


'''BLOQUE 3'''

    # 1. Calcular la suma de alguna propiedad numérica de los registros que cumplan determinada condición.
def suma_bateria (datos,n='todos'):
    '''
        Recibe la lista de tuplas con nombre y devuelve una lista de longitud n con la suma
        de los porcentajes de batería al inicio y al final de cada trayecto, con latitud/longitud válidas.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
        @param n: string que indica cuántos datos quiero leer desde el inicio de la lista
        @type n: str
    SALIDA:
        @return lista de integers de longitud n con las sumas de los porcentajes de batería inicial y final.
        @rtype suma_nivel_bateria: [int,...]
    
    '''

    suma_nivel_bateria = [i.battery_level_at_start+i.battery_level_at_the_end for i in datos if i.starting_station_latitude != 0.0 if  i.ending_station_latitude != 0.0]
    if n != 'todos':
        n = int(n)
        suma_nivel_bateria = suma_nivel_bateria[0:n]
    return suma_nivel_bateria

    # 2. Calcular el promedio de alguna propiedad numérica de los registros que cumplan determinada condición.
def promedio_bateria (datos,n):
    '''
        Recibe la lista de tuplas con nombre y devuelve una lista de longitud n 
        con el nivel medio de batería de cada trayecto con latitud/longitud válidas.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
        @param n: string que indica cuántos datos quiero leer desde el inicio de la lista
        @type n: str
    SALIDA:
        @return lista de floats, de longitud n con el promedio de los porcentajes de batería inicial y final de cada trayecto.
        @rtype promedio_nivel_bateria: [float,...]
    
    '''

    promedio_nivel_bateria = [suma/2 for suma in suma_bateria(datos,n)]
    promedio_nivel_bateria = round((sum(promedio_nivel_bateria[:n]))/(len(promedio_nivel_bateria[:n])),2)
    return promedio_nivel_bateria

'''BLOQUE 4'''

    # 2. Obtener el registro (o algunos campos del registro) que contiene el valor máximo o mínimo de un campo determinado, de los registros que cumplen determinada condición.

def registro_maximos_kilometros_recorridos(datos):
    '''
        Recibe la lista de tuplas con nombre y devuelve el registro que tiene el máximo de kilómetros en el trayecto, siendo la bicicleta una dañada.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
    SALIDA:
        @return registro completo que contiene el trayecto con más kilómetros recorridos con una bicicleta dañada
        @rtype registro_km_max: Registro(int, int, str, str, int, float, float, int, float, float, int, str, str, float, int, int, float, float, float, bool, bool, int, str)
    
    '''

    registro_km_max = max([i for i in datos if i.damaged_bike == True], key = lambda x: x.kilometers_travelled, default='Error')
    return registro_km_max

'''BLOQUE 5'''

    # 1. Obtener una lista de registros (o algunos campos del registro) ordenada con los n registros con mayor (o menor) valor en un campo determinado. Donde 'n' es un parámetro que debe recibir la función.

def registros_mas_duracion_trayecto(datos,n):
    '''
        Recibe la lista de tuplas con nombre y devuelve una lista con los n registros con mayor duración del trayecto.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
        @param n: número entero que indica cuántos datos quiero leer desde el inicio de la lista
        @type n: int
    SALIDA:
        @return lista con los n registros de mayor duración de trayecto
        @rtype lista_registros_mas_largos: [Registro_1, Registro_2, ... , Registro_n]
    
    '''

    lista_registros_mas_largos = sorted([i for i in datos], key = lambda x: x.duration_in_seconds, reverse = True)
    return lista_registros_mas_largos[:n]

'''BLOQUE 6''' # Elegir 2 (1 entre el (1,2) y 2 entre el (3,4))

    # 1. Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún campo(clave). A cada clave se le hará corresponder
    # una lista con los registros que contienen esa clave.

def tipo_de_pase(datos,anyo):
    '''
        Recibe la lista de tuplas con nombre y el año de filtrado, y devuelve un diccionario cuyas claves son los tipos de 
        pases disponibles, y los valores son listas de registros que contienen esas claves.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
        @param anyo: número entero que indica el año para filtrar los datos
        @type anyo: int
    SALIDA:
        @return diccionario con tipos de pases como claves, y listas de registros que contienen las claves como valores
        @rtype dict_pases: {'Walk-up':[Registros], 'Monthly Pass':[Registros], 'Flex Pass':[Registros], 'Staff Annual':[Registros]}
    
    '''

    registros_anyo_i = [l for l in datos if l.start_time.year == anyo]
    lista_walk_up = []
    lista_monthly = []
    lista_flex = []
    lista_staff_annual = []

    tipos_passholder = []

    for linea in registros_anyo_i:
        if linea.passholder_type not in tipos_passholder:
            tipos_passholder.append(linea.passholder_type)

    j = len(tipos_passholder)

    #defaultdic --> mejor solución

    for linea in registros_anyo_i:
        if linea.passholder_type == "Walk-up":
            lista_walk_up.append(linea)
        elif linea.passholder_type == 'Monthly Pass':
            lista_monthly.append(linea)
        elif linea.passholder_type == 'Flex Pass':
            lista_flex.append(linea)
        elif linea.passholder_type == 'Staff Annual':
            lista_staff_annual.append(linea)

    dict_pases = {'Walk-up':lista_walk_up, 'Monthly Pass':lista_monthly, 'Flex Pass':lista_flex, 'Staff Annual':lista_staff_annual}

    return dict_pases
 
    # 4. Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún campo(clave) y que haga corresponder a cada clave
    # una lista, con los 'n' regitros, ordenados de mayor a menor o de menor a mayor por algún campo que no sea la clave.

def tipo_de_viaje(datos,anyo,n,mayor_a_menor_duracion):
    '''
        Recibe la lista de tuplas con nombre, el año de filtrado, los n primeros valores a mostrar y un booleano que indica el orden; 
        y devuelve un diccionario cuyas claves son los tipos de viaje, y los valores son listas de longitud de los registros que tienen
        esas claves, pero ordenados según el tiempo de duración del viaje.
    
    ENTRADA:
        @param datos : lista de tuplas con nombre obtenida de leer el csv
        @type datos : list
        @param anyo: número entero que indica el año para filtrar los datos
        @type anyo: int
        @param n: número entero que indica cuántos datos quiero leer desde el inicio de la lista
        @type n: int
        @param mayor_a_menor_duracion: booleano que marca si se ordena según el tiempo de duración del viaje de mayor a menor o al contrario
        @type mayor_a_menor_duracion: bool
    SALIDA:
        @return diccionario con tipos de viajes como claves, y listas de registros que contienen las claves como valores, ordenados según el tiempo de viaje
        @rtype dict_pases: {'One Way':[Registros], 'Round Trip':[Registros]}
    
    '''

    registros_anyo_i = [l for l in datos if l.start_time.year == anyo]
    lista_one_way = []
    lista_round_trip = []

    for linea in registros_anyo_i:
        if linea.trip_route_category == 'One Way':
            lista_one_way.append(linea)
        elif linea.trip_route_category == 'Round Trip':
            lista_round_trip.append(linea)

    lista_one_way_ordenada = sorted(lista_one_way,key = lambda x: x.duration_in_seconds, reverse = mayor_a_menor_duracion)
    lista_round_trip_ordenada = sorted(lista_round_trip,key = lambda y: y.duration_in_seconds, reverse = mayor_a_menor_duracion)

    dict_tipo_viaje = {'One Way': lista_one_way_ordenada[:n], 'Round Trip': lista_round_trip_ordenada[:n]}

    return dict_tipo_viaje