# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:41:47 2022

@author: Montse García
"""


print("Bienvenido, ingreso el numero de habitantes dependiendo de la puerta que se pide")

print("Ingrese los habitantes de la puerta 1A")
A1 = input()
print("Ingrese los habitantes de la puerta 1B")
B1 = input()
print("Ingrese los habitantes de la puerta 1C")
C1 = input()
print("Ingrese los habitantes de la puerta 1D")
D1 = input()

print("Ingrese los habitantes de la puerta 2A")
A2 = input()
print("Ingrese los habitantes de la puerta 2B")
B2 = input()
print("Ingrese los habitantes de la puerta 2C")
C2 = input()
print("Ingrese los habitantes de la puerta 2D")
D2 = input()

print("Ingrese los habitantes de la puerta 3A")
A3 = input()
print("Ingrese los habitantes de la puerta 3B")
B3 = input()
print("Ingrese los habitantes de la puerta 3C")
C3 = input()
print("Ingrese los habitantes de la puerta 3D")
D3 = input()

print("Ingrese los habitantes de la puerta 4A")
A4 = input()
print("Ingrese los habitantes de la puerta 4B")
B4 = input()
print("Ingrese los habitantes de la puerta 4C")
C4 = input()
print("Ingrese los habitantes de la puerta 4D")
D4 = input()

print("Ingrese los habitantes de la puerta 5A")
A5 = input()
print("Ingrese los habitantes de la puerta 5B")
B5 = input()
print("Ingrese los habitantes de la puerta 5C")
C5 = input()
print("Ingrese los habitantes de la puerta 5D")
D5 = input()

print("Ingrese los habitantes de la puerta 6A")
A6 = input()
print("Ingrese los habitantes de la puerta 6B")
B6 = input()
print("Ingrese los habitantes de la puerta 6C")
C6 = input()
print("Ingrese los habitantes de la puerta 6D")
D6 = input()


if (A1 > B1) and (A1>C1) and (A1>D1):
    print("El departamento A es el que tiene más habitantes en el piso 1")
    piso1 = A1
    nombre1 = "1A"
else:
    if (B1 > A1) and (B1>C1) and (B1>D1):
        print("El departamento 1B es el que tiene más habitantes en el piso 1")
        piso1 = B1
        nombre1 = "1B"
    else:
        if (C1 > A1) and (C1>B1) and (C1>D1):
            print("El departamento 1C es el que tiene más habitantes en el piso 1")
            piso1 = C1
            nombre1 = "1C"
        else:
            if (D1 > A1) and (D1>B1) and (D1>C1):
                print("El departamento 1D es el que tiene más habitantes en el piso 1")
                piso1 = D1
                nombre1 = "D1"
                
                
                
if (A2 > B2) and (A2>C2) and (A2>D2):
    print("El departamento 2A es el que tiene más habitantes en el piso 2")
    piso2 = A2
    nombre2 = "2A"
else:
    if (B2 > A2) and (B2>C2) and (B2>D2):
        print("El departamento 2B es el que tiene más habitantes en el piso 2")
        piso2 = B2
        nombre2 = "2B"
    else:
        if (C2 > A2) and (C2>B2) and (C2>D2):
            print("El departamento 2C es el que tiene más habitantes en el piso 2")
            piso2 = C2
            nombre2 = "2C"
        else:
            if (D2 > A2) and (D2>B2) and (D2>C2):
                print("El departamento 2D es el que tiene más habitantes en el piso 2")
                piso2 = D2
                nombre2 = "2D"
                
                
                
if (A3 > B3) and (A3>C3) and (A3>D3):
    print("El departamento 3A es el que tiene más habitantes en el piso 3")
    piso3 = A3
    nombre3 = "3A"
else:
    if (B3 > A3) and (B3>C3) and (B3>D3):
        print("El departamento 3B es el que tiene más habitantes en el piso 3")
        piso3 = B3
        nombre3 = "3B"
    else:
        if (C3 > A3) and (C3>B3) and (C3>D3):
            print("El departamento 3C es el que tiene más habitantes en el piso 3")
            piso3 = C3
            nombre3 = "3C"
        else:
            if (D3 > A3) and (D3>B3) and (D3>C3):
                print("El departamento 3D es el que tiene más habitantes en el piso 3")
                piso3 = D3
                nombre3 = "3D"
                
                
                
if (A4 > B4) and (A4>C4) and (A4>D4):
    print("El departamento 4A es el que tiene más habitantes en el piso 4")
    piso4 = A4
    nombre4 = "4A"
else:
    if (B4 > A4) and (B4>C4) and (B4>D4):
        print("El departamento 3B es el que tiene más habitantes en el piso 4")
        piso4 = B4
        nombre4 = "4B"
    else:
        if (C4 > A4) and (C4>B4) and (C4>D4):
            print("El departamento 3C es el que tiene más habitantes en el piso 4")
            piso4 = C4
            nombre4 = "4C"
        else:
            if (D4 > A4) and (D4>B4) and (D4>C4):
                print("El departamento 4D es el que tiene más habitantes en el piso 4")
                piso4 = D4
                nombre4 = "4D"
                
                
                
if (A5 > B5) and (A5>C5) and (A5>D5):
    print("El departamento 5A es el que tiene más habitantes en el piso 5")
    piso5 = A5
    nombre5 = "5A"
else:
    if (B5 > A5) and (B5>C5) and (B5>D5):
        print("El departamento 5B es el que tiene más habitantes en el piso 5")
        piso5 = B5
        nombre5 = "5B"
    else:
        if (C5 > A5) and (C5>B5) and (C5>D5):
            print("El departamento 5C es el que tiene más habitantes en el piso 5")
            piso5 = C5
            nombre5 = "5C"
        else:
            if (D5 > A5) and (D5>B5) and (D5>C5):
                print("El departamento 5D es el que tiene más habitantes en el piso 5")
                piso5 = D5
                nombre5 = "5D"
                
                
                
if (A6 > B6) and (A6>C6) and (A6>D6):
    print("El departamento 6A es el que tiene más habitantes en el piso 6")
    piso6 = A6
    nombre6 = "6A"
else:
    if (B6 > A6) and (B6>C6) and (B6>D6):
        print("El departamento 6B es el que tiene más habitantes en el piso 6")
        piso6 = B6
        nombre6 = "6B"
    else:
        if (C6 > A6) and (C6>B6) and (C6>D6):
            print("El departamento 6C es el que tiene más habitantes en el piso 6")
            piso6 = C6
            nombre6 = "6C"
        else:
            if (D6 > A6) and (D6>B6) and (D6>C6):
                print("El departamento 6D es el que tiene más habitantes en el piso 6")
                piso6 = D6
                nombre6 = "6D"
                
                
if (piso1 > piso2) and (piso1 > piso3) and (piso1 > piso4) and (piso1 > piso5) and (piso1 > piso6):
    print("El departamento con mayor número de habitantes en el edificio es el ", nombre1)
else:
    if (piso2 > piso1) and (piso2 > piso3) and (piso2 > piso4) and (piso2 > piso5) and (piso2 > piso6):
        print("El departamento con mayor número de habitantes en el edificio es el ", nombre2)
    else:
        if (piso3 > piso1) and (piso3 > piso2) and (piso3 > piso4) and (piso3 > piso5) and (piso3 > piso6):
            print("El departamento con mayor número de habitantes en el edificio es el ", nombre3)
        else: 
            if (piso4 > piso2) and (piso4 > piso3) and (piso4 > piso3) and (piso4 > piso5) and (piso4 > piso6):
                print("El departamento con mayor número de habitantes en el edificio es el ", nombre4)
            else:
                if (piso5 > piso2) and (piso5 > piso3) and (piso5 > piso3) and (piso5 > piso4) and (piso5 > piso6):
                    print("El departamento con mayor número de habitantes en el edificio es el ", nombre5)
                else:
                    if (piso6 > piso2) and (piso6 > piso3) and (piso6 > piso3) and (piso6 > piso4) and (piso6 > piso5):
                        print("El departamento con mayor número de habitantes en el edificio es el ", nombre6)