import warnings
warnings.filterwarnings("ignore")
from folium.map import FeatureGroup, LayerControl
import osmnx as ox
import networkx as nx
import webbrowser
import folium
from osmnx.io import load_graphml, save_graphml
from folium.plugins import MeasureControl
from folium.plugins import MousePosition
import sys
import os
import time
import selenium
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver
import csv

get_driver = GetGeckoDriver()
get_driver.install()

lista_codigos = []
with open('codigos_panorama.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for linea in f:
        lista_codigos.append(linea)
lista_codigos = [x.replace("\n","") for x in lista_codigos]

def plot_rutas(rutastotales):

    ox.config(log_console=False, use_cache=False)

    #G_bike = ox.graph_from_place('Los Angeles, California, USA', network_type='bike')
    #save_graphml(G_bike, 'src\mapabaserutas.graphml')
    G_bike = load_graphml('src\mapabaserutas.graphml')
    Mapa = 'https://api.mapbox.com/styles/v1/chervasmartin/ckvvl0wxq42bc14o2xqzgiqy1/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiY2hlcnZhc21hcnRpbiIsImEiOiJjajZwc3BqNHIwMmswMnBwbWRtczV0ODN2In0.K18WhQI1yGtHP7xl1HVtzA'

    m = folium.Map(location=[34.04652, -118.237411],
        zoom_start=14,
        tiles=None,
        attr='Mapbox de Carlos Hervás Martín')

    tile_layer = folium.TileLayer(
        tiles = Mapa,
        attr = 'Mapbox de Carlos Hervás Martín',
        name = 'Mapa',
        control = False)

    tile_layer.add_to(m)


    import random
    def color_aleatorio():
        hexcolor = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        return hexcolor[0]

    d = {}
    iter = 0
    ntrayecto = 1
    n_estacion = 0
    feature_group_estaciones = FeatureGroup(name='Estaciones')
    feature_group_rutas = FeatureGroup(name='Trayectos')
    fg = folium.FeatureGroup(name='Mapa', show=False)
    m.add_child(fg)

    iter_codigos = 0

    for i in rutastotales:

        orig_node = ox.get_nearest_node(G_bike, (i[0], i[1]))

        dest_node = ox.get_nearest_node(G_bike,(i[2], i[3]))

        d["route{0}".format(iter)] = nx.shortest_path(G_bike, orig_node, dest_node, weight='length')
        print(d.values())

        n_estacion = n_estacion+1
        n_estacion_aux = n_estacion

        html_e1="""
            <center>
            <h2 style="font-family: Helvetica;">Estación %s &#128204</h2>
            <iframe src="https://www.google.com/maps/embed?pb=!!6m8!1m7!%s!!!!!!" width="700" height="500" style="border:0;" allowfullscreen="" loading="lazy" scrolling="no"></iframe>
            """ % (n_estacion,lista_codigos[iter_codigos])
        iframe_e1 = folium.IFrame(html=html_e1, width=800, height=600)
        popup_e1 = folium.Popup(iframe_e1, max_width=2650)
        iter_codigos = iter_codigos + 1

        #<iframe src="https://maps.google.com/maps?q=&layer=c&cbll=%f,%f&cbp=11,0,0,0,0" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>

        folium.Marker([i[0],i[1]], popup=popup_e1, icon=folium.Icon(color="green", icon="bicycle", prefix='fa')).add_to(feature_group_estaciones)

        n_estacion = n_estacion+1

        html_e2="""
            <center>
            <h2 style="font-family: Helvetica;">Estación %s &#128204</h2>
            <iframe src="https://www.google.com/maps/embed?pb=!!6m8!1m7!%s!!!!!!" width="700" height="500" style="border:0;" allowfullscreen="" loading="lazy" scrolling="no"></iframe>
            """ % (n_estacion,lista_codigos[iter_codigos])
        iframe_e2 = folium.IFrame(html=html_e2, width=800, height=600)
        popup_e2 = folium.Popup(iframe_e2, max_width=2650)
        iter_codigos = iter_codigos + 1
        
        folium.Marker([i[2],i[3]], popup=popup_e2, icon=folium.Icon(color="green", icon="bicycle", prefix='fa')).add_to(feature_group_estaciones)

        html="""
            <center>
            <h2 style="font-family: Helvetica;">Trayecto %i &#128690</h2>
            <p style="font-family: Helvetica;">
            Estaci&oacute;n inicial: %s <br />
            Estaci&oacute;n final: %s </center>
            </p>
            <center></center><center></center>
            <center><a href="https://www.google.com/maps/dir/%f,%f/%f,%f/@34.04652,-118.237411,14z/data=!3m1!4b1!4m2!4m1!3e1" target="_blank"><img class="n3VNCb" style="width: 123px; height: 82px; margin: 0px;" src="https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2021/03/31/16172001711936.png" alt="Google Maps trae cambios y mejoras a Espa&ntilde;a: esto es lo que necesitas saber  | Tecnolog&iacute;a" data-noaft="1" /></a></center>
            """ % (ntrayecto,n_estacion_aux,n_estacion, i[0], i[1], i[2], i[3])
        iframe = folium.IFrame(html=html, width=250, height=220)
        popup = folium.Popup(iframe, max_width=2650)

        for key, value in d.items():
            lista_nodos = list(value)
            print(lista_nodos)
            lista_nodos_lat_lon = []
            for nodo in lista_nodos:
                lat = G_bike.nodes[nodo]['y'] #latitud
                lon = G_bike.nodes[nodo]['x'] #longitud
                lista_nodos_lat_lon.append((lat,lon))
            
            folium.PolyLine(lista_nodos_lat_lon, color = color_aleatorio(), weight = 5, popup=popup).add_to(feature_group_rutas)
        ntrayecto += 1
            
    feature_group_estaciones.add_to(m)
    feature_group_rutas.add_to(m)
    LayerControl(collapsed=False,).add_to(m)
    MousePosition().add_to(m)
    m.add_child(MeasureControl())
    m.save('src\mapa.html')
    url = 'src\mapa.html'
    webbrowser.open(url, new=2)