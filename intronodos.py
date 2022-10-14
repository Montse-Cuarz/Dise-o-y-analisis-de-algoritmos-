# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:13:31 2022

@author: Montse García
"""

class Nodo:
    def _init_(self, value, arriba = None, centro = None, abajo = None):
        self.data = value
        self.arriba = arriba
        self.centro = centro
        self.abajo = abajo



Objhead = Nodo(20, Nodo(23, ' ', Nodo(57), ' '),
          Nodo(19, ' ', ' ', Nodo(67, ' ', Nodo(99), ' ')))

print(Objhead.centro.abajo.centro.data)
print(Objhead.arriba.centro.data)