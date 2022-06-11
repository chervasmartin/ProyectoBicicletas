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


def panoramacodegen(lat,lon):

    url_0 = f'https://maps.google.com/maps?q=&layer=c&cbll={lat},{lon}&cbp=11,0,0,0,0'
    driver = webdriver.Firefox()
    driver.get(url_0)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span').click()
    driver.get(url_0)
    driver.implicitly_wait(1)
    time.sleep(7)
    new_url = driver.current_url
    new_url = str(new_url)
    pancode = new_url[new_url.find('3m4!')+len('3m4!'):new_url.rfind('!2e0')]
    driver.close()
    return pancode

def generador_codigos(rutastotales):
    with open('codigos_panorama.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        iter = 1
        total = len(rutastotales)
        for i in rutastotales:
            writer.writerow([panoramacodegen(i[0],i[1])])
            print(f'Van {iter} estaciones de {total}')
            iter = iter+1