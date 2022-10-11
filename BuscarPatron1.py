# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:10:16 2022

@author: Montse García
"""

cadena ="1110010001101110100011001111000110001110001110001110100011010001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001101000111110101010100111100011000"
patron ="1010101"

def Patron_busq(cadena, patron):
   for a in range (len(cadena)- len(patron)+1):
    for b in range (len(patron)):
      if patron[b] == cadena[a + b]:
        pass
      else:
        break
    if (b + 1 == (len(patron))) and (cadena[a +b] == patron[b]):
      print(f"Se encuentra el patron en el caracter número {a}")   

      
Patron_busq(cadena, patron)



