#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Genera 30 números aleatorios del 1 al 30 en una lista.
# Escribe los nombres de los ficheros que contienen los nombres de alumnos en un fichero (lista.txt) y le cambia el nombre original por uno aleatorio para ocultar la identidad
#
import sys
from random import randint
import os

#Genera una lista de números aleatorios del 1-30
lista=[]
for i in range(1,30):
    n=randint(1,30)
    while n in lista:
        n=randint(1,30)
    lista.append(n)

file = open("asociacion.txt","w")
#Crea una lista con los nombres de los ficheros del directorio actual
files = [f for f in os.listdir('.') if os.path.isfile(f)]
#recorre los ficheros del directorio actual
i = 0
for f in files:
    if extension != ".py" and extension != ".txt" :
        #parsea el filename y recoge unicamente el nombre del alumno
        nombreAlumno = f.split('_')[0]
        #parsea el filename y recoge la extensión del archivo
        extension = os.path.splitext(f)[1]
        #cambia el nombre del fichero por un número aleatorio de la lista creada anteriormente excepto este script .py y asociacion.txt
        os.rename(f, str(lista[i])+extension)
        print("Cambiado" + nombreAlumno+ " por " + str(lista[i])+extension)
        #Escribe el nombre del alumnos y su fichero correspondiente en un fihero de texto para poder sociarlos posteriormente
        file.write(str(lista[i]) + ', ' + nombreAlumno + '\n')
        i += 1
file.close()
