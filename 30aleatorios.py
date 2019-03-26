#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Genera 30 números aleatorios del 1 al 30
#
import sys
from random import randint

#lista=[]
lista=[4,24,27,3,9,21,16]
for i in range(1,24):
    n=randint(1,30)
    while n in lista:
        n=randint(1,30)
    lista.append(n)
    print (n)
