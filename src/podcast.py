# -*- coding:utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''

from collections import namedtuple
from parsers import *
import csv
import statistics
from collections import Counter

Podcast = namedtuple('Podcast', 'titulo, suscriptores, valoracion,numero_valoraciones, categoria, episodios, fecha_ultimo, gratuito, etiquetas')
def lee_fichero(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter = ";")
        next(lector)
        res=[]
        for titulo, suscriptores, valoracion, numero_valoraciones, categoria, episodios, fecha_ultimo, gratuito, etiquetas in lector:
            tupla = Podcast(titulo, int(suscriptores), float(valoracion), int(numero_valoraciones), categoria, int(episodios), parsea_fecha(fecha_ultimo), parsea_booleano(gratuito), etiquetas)
            res.append(tupla)
    return res

def etiquetas(registros,etiqueta,fecha):
    return [t for t in registros if t.etiqueta==etiqueta and t.fecha==fecha and t.gratuito =='gratuito']

def numero_de_podcast(registros,categoria):
    lista = [t for t in registros if t.categoria==categoria]
    media = sum(t.suscriptores for t in lista)/len(lista)
    return len([t for t in lista if t.suscriptores>media])

def podcas_mas_valorados(registros,m,n):
    res =[(t.tituo,t.valoracion) for t in registros if t.valoracion>m]
    lista_ordenada = sorted(res,key=lambda x:x[1],reverse =True)
    if len(lista_ordenada)>n:
        lista_ordenada=lista_ordenada[:n]
    return lista_ordenada
    

def lista_ordenada (registros):
    lista_ordenada = sorted(registros, key=lambda x:x.suscriptores, reverse=True)
    return [(p1.titulo,p1.suscriptores-p2.suscriptores)for p1,p2 in zip(lista_ordenada,lista_ordenada[1:])]

def diccionario(registros):
    dicc = Counter(t.etiquetas for t in registros if t.gratuito == True)       
    maximo = max(dicc.items(), key=lambda x:x[1])
    return maximo [0]

def ejercicio6(registros,n=3):
    dicc ={}
    for t in registros:
        clave = t.categoria
        if clave in dicc:
            dicc[clave].append(t)
        else:
            dicc[clave] = [t]
    for clave, valor in dicc.items:
        lista_ordenada = sorted(valor, key=lambda x:x.suscriptores, reverse= True)[:n]
        dicc[clave]= [t.titulo for t in lista_ordenada]
    return dicc   
    
    