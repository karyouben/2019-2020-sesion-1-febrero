# -*- coding:utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''
from _datetime import datetime

def parsea_fecha(cadena):
    return datetime.strptime(cadena, '%d/%m/%Y').date()

def parsea_booleano(cadena):
    res = True
    cadena = cadena.upper()
    if cadena== 'GRATUITO':
        res=True
    elif cadena =='PAGO':
        res=False
    return res