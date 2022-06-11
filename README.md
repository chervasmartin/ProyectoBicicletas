# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  2021/2022) :snake: :computer:

![version](https://img.shields.io/badge/version-v1.0.0-green)

Autor: Carlos Hervás Martín  
> uvus:  carhermar3 

El dataset escogido para este proyecto es el que contiene los [datos del servicio de bicicletas compartidas de la ciudad de Los Ángeles](https://www.kaggle.com/cityofLA/los-angeles-metro-bike-share-trip-data).
<!-- Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto. -->



<p float="left" align="center">
<img src="https://momentummag.com/wp-content/uploads/2016/07/Screen-Shot-2016-07-07-at-11.48.17-AM.png" width="450" height="auto"/>
<img src="https://i.ibb.co/g4Xbth5/bike-share-hero.png" width="450" height="auto"/>
<img src="https://media.giphy.com/media/aiibBXnliiyChNOd1a/giphy-downsized-large.gif" width="450" height="auto" style = "float:right"/>
</p>


## Estructura de las carpetas del proyecto :file_folder:

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **bicis.py**: Módulo principal del proyecto. Aquí se implementan las funciones principales usadas.
  * **test_bicis.py**: Módulo de pruebas.
  * **modulo_navegacion.py**: Módulo para la representación de rutas y/o estaciones.
* **/data**: Contiene el dataset del proyecto.
    * **dataset_bicis.csv**: Dataset con información del servicio de bicletas compartidas de la ciudad de Los Angeles.
* **/doc**: Contiene el enunciado del proyecto.
    * **enunciado_bicis.md**: Enunciado del proyecto realizado.
    
## Estructura del *dataset* :page_facing_up:

El dataset con el que se trabaja tiene información relativa al servicio de préstamo de bicicletas de Los Angeles. 

El dataset está compuesto por 23 columnas, con la siguiente descripción:

* **trip_id**: de tipo `int`, representa el identificador único de cada viaje.
* **duration_in_minutes**: de tipo `int`, representa la duración de cada viaje en minutos.
* **start_time**: es un objeto `datetime`, representa la fecha y hora de inicio del viaje.
* **end_time**: objeto datetime `datetime`, representa la fecha y hora de finalización del viaje.
* **starting_station_id**: de tipo `int`, representa el identificador de la estación desde la que se inicia el viaje.
* **starting_station_latitude**: de tipo `float`, representa la latitud de la estación de inicio en grados decimales.
* **starting_station_longitude**: de tipo `float`, representa la longitud de la estación de inicio en grados decimales.
* **ending_station_id**: de tipo `int`, representa el identificador de la estación en la que se termina el viaje.
* **ending_station_latitude**: de tipo `float`, representa la latitud de la estación de finalización en grados decimales.
* **ending_station_longitude**: de tipo `float`, representa la longitud de la estación de finalización en grados decimales.
* **bike_id**: de tipo `int`, representa el identificador único de cada bicicleta.
* **trip_route_category**: de tipo `str`, representa el tipo de viaje que se ha realizado (*One Way* o *Round Trip*).
* **passholder_type**: de tipo `str`, representa el tipo de abono de cada viajero (*Walk-up*, *Monthly Pass*, *Flex Pass* o *Staff Annual*).
* **kilometers_travelled**: de tipo `float`, representa los kilómetros de viaje acumulados de esa bicicleta.
* **battery_level_at_start**: de tipo `int`, representa el nivel de batería de la bicicleta al comienzo del viaje.
* **battery_level_at_the_end**: de tipo `int`, representa el nivel de batería de la bicileta al finalizar el viaje.
* **maximum_speed**: de tipo `float`, representa la velocidad máxima alcanzada [dam/h] (*Pd*: debo dividir entre 100 para tener km/h).
* **minimum_speed**: de tipo `float`, representa la velocidad mínima alcanzada [dam/h] (*Pd*: debo dividir entre 100 para tener km/h).
* **average_speed**: de tipo `float`, representa la velocidad media de viaje [dam/h].
* **new_user**: de tipo `bool`, nos dice si se trata de un usuario nuevo o no.
* **damaged_bike**: de tipo `bool`, nos indica si la bicicleta está dañada o no.
* **zip_codes**: de tipo `int`, representa los códigos postales en los que se inician los viajes.
* **subscription_plan_duration**: de tipo `str`, representa la duración del tipo de suscripción del usuario (*0*, *30* o *365* días).

## Tipos implementados `str`, `int`, `float`,`bool`

Para manejar los datos del dataset se define la siguiente `namedtuple`:

`Registro = namedtuple('Registro', 'trip_id,duration_in_minutes,start_time,end_time,starting_station_id,starting_station_latitude,starting_station_longitude,ending_station_id,ending_station_latitude,ending_station_longitude,bike_id,trip_route_category,passholder_type,kilometers_travelled,battery_level_at_start,battery_level_at_the_end,maximum_speed,minimum_speed,average_speed,new_user,damaged_bike,zip_codes,subscription_plan_duration')`

que tiene los siguientes tipos:

`Registro(int, int, str, str, int, float, float, int, float, float, int, str, str, float, int, int, float, float, float, bool, bool, int, str)`

De cara a facilitar el trabajo con el dataset se toman algunas decisiones:

- Se rellenan de ceros (0) los datos incompletos de las columnas: `starting_station_latitude`,`starting_station_longitude`,`ending_station_latitude`,`ending_station_longitude` y `zip_codes`; esto se hace para evitar errores en la lectura al convertir `str` con espacios en `float` o `int`. 


## Funciones implementadas :heavy_multiplication_x: :heavy_plus_sign: :heavy_minus_sign: :heavy_division_sign:
En el proyecto creado se utilizan un gran número de funciones que se clasifican a continuación según las entregas, los ficheros y los bloques a los que pertenezcan.

### bicis.py

- **Entrega 1**
        
    - Bloque 1

      -  `lectura_datos_csv(fichero)`: lee los datos del fichero csv, tomando como input la ruta del fichero, y devuelve una lista de tuplas de tipo Registro con todas las filas del fichero. Además realiza una conversión de los tipos de datos, pasando de `str` al tipo pertinente según la columna.
        
- **Entrega 2**:

    - Bloque 2

      -  `lista_starting_stations(datos)`: recibe como input la lista de tuplas con nombre de la lectura del csv y devuelve una lista de todos los IDs de estaciones iniciales sin repetir y ordenada de menor a mayor.
      -  `lat_long(datos)`: recibe como input la lista de tuplas con nombre de la lectura del csv y devuelve una lista de tuplas, cada una con los datos de latitud/longitud de las estaciones de inicio y fin. Sólo almacena los registros en los que hay datos de latitud y longitud distintos de 0.

    - Bloque 3

      -  `suma_bateria(datos,n)`: recibe la lista de tuplas con nombre de la lectura del csv y la cantidad de datos a obtener (n), y devuelve una lista de longitud n de enteros que representan la suma de los porcentajes de batería inicial y final del trayecto.
      -  `promedio_bateria`: recibe la lista de tuplas con nombre de la lectura del csv y la cantidad de datos a obtener (n), y devuelve una lista de longitud n de floats que representan el nivel de batería promedio de cada trayecto.
        
- **Entrega 3**:

    - Bloque 4

      -  `registro_maximos_kilometros_recorridos(datos)`: recibe la lista de tuplas con nombre y devuelve el registro que tiene el máximo de kilómetros en el trayecto, siendo la bicicleta una dañada.

    - Bloque 5

      -  `registros_mas_duracion_trayecto(datos,n)`: recibe la lista de tuplas con nombre y devuelve una lista con los n registros con mayor duración del trayecto.

    - Bloque 6

      -  `tipo_de_pase(datos,anyo)`: recibe la lista de tuplas con nombre y el año de filtrado, y devuelve un diccionario cuyas claves son los tipos de pases disponibles, y los valores son listas de registros que contienen esas claves.
      -  `tipo_de_viaje(datos,anyo,n,mayor_a_menor_duracion)`: recibe la lista de tuplas con nombre, el año de filtrado, los n primeros valores a mostrar y un booleano que indica el orden; y devuelve un diccionario cuyas claves son los tipos de viaje, y los valores son listas de longitud de los registros que tienen esas claves, pero ordenados según el tiempo de duración del viaje.


### test_bicis.py

En el modulo de tests se implementan funciones que servirán para hacer pruebas sobre las funciones definidas en el módulo principal `bicis.py`.

- **Entrega 1**
        
    - Bloque 1

      -  `mostrar_numero_registros_leidos(coleccion)`: recibe la lista de tuplas de datos e imprime por pantalla el número total de registros leídos, y muestra los tres primeros y últimos registros leidos.

- **Entrega 2**

    - Bloque 2

      -  `test_bloque2_3(datos)`: recibe la lista de tuplas de datos e imprime por pantalla el número de estaciones de inicio diferentes, y la lista con todas estas estaciones.
      -  `test_bloque2_4(datos,n)`: recibe la lista de tuplas de datos e imprime por pantalla la lista de tuplas de latitudes y longitudes de los registros con datos de ubicación completos.

    - Bloque 3

      -  `test_bloque3_1(datos,n)`: recibe la lista de tuplas de datos y un parámetro n que indica la cantidad de datos a obtener desde el inicio (por defecto n = 'todos'). Devuelve una lista de longitud n con la suma de los niveles de bateria inicial y final de cada registro.
      -  `test_bloque3_2(datos,n)`: recibe la lista de tuplas de datos y un parámetro n que indica la cantidad de datos a obtener desde el inicio (por defecto n = 'todos'). Devuelve una lista de longitud n con el nivel de bateria promedio de cada registro, así como el promedio global según la lista obtenida.

- **Entrega 3**

    - Bloque 4

      -  `test_bloque4_2(datos)`: recibe la lista de tuplas de datos y devuelve el registro perteneciente al trayecto con más kilómetros recorridos con una bicicleta dañada.
 
    - Bloque 5

      -  `test_bloque5_1(datos,n)`: recibe la lista de tuplas de datos y devuelve los n primeros registros con mayor duración de trayecto.

    - Bloque 6

      -  `test_bloque6_1(datos,anyo)`: recibe la lista de tuplas de datos y el año de filtrado, y devuelve un diccionario cuyas claves son los tipos de pases disponibles, y los valores son listas de registros que contienen esas claves.
      -  `test_bloque6_4(datos,n,anyo,mayor_a_menor_duracion)`: recibe la lista de tuplas con nombre, el año de filtrado, los n primeros valores a mostrar y un booleano que indica el orden; y devuelve un diccionario cuyas claves son los tipos de viaje, y los valores son listas de longitud de los registros que tienen esas claves, pero ordenados según el tiempo de duración del viaje.

### modulo_navegacion.py 🗺️📍

- **Entrega 3**

    - Bloque Extra

      -  `plot_rutas(rutastotales)`: recibe una lista de tuplas con latitudes y longitudes de los puntos de inicio y fin de cada trayecto. Con esto, se representan en un mapa las estaciones pertenecientes a los n primeros registros y los trayectos entre esas estaciones siguiendo el criterio de mínima distancia.

## Roadmap 🎯

- [x] Bloque 1
- [x] Bloque 2
- [x] Bloque 3
- [x] Bloque 4
- [x] Bloque 5
- [x] Bloque 6
- [x] Bloque 7
- [x] Funciones extra
	- [x] Mapa de navegación de rutas y estaciones

[//]: # (- **<funcion 1>**: Descripción de la función 1.)
[//]: # (- **<funcion 2>**: Descripción de la función 2.)
