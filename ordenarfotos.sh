#!/bin/bash

#Ordena fotos por fecha creando carpetas para cada año y subcarpetas para cada  mese
exiftool "-Directory<CreateDate" -d ./%Y/%m -r ./
