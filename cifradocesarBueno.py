# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:15:14 2022

@author: Montse García
"""

abc = "abcdefghijklmnñopqrstuvwxyz"

def cifrado_cesar(mensaje):
    cifrado=""
    for i in range(len(mensaje)):
        if(mensaje[i] == 'z' ):
            cifrado = cifrado + 'a'
        else: 
            cifrado = cifrado + (abc[abc.index(mensaje[i]) + 19])
            if (mensaje[i] == '.'):
                cifrado = cifrado + '.'
        
    return cifrado 

mensaje = "Si Cupdmzaplil Uikpwuis Icbwuwti lm Tmfpkw oi lmamtxmvilw cu xixms xzwbiñwupkw mu si opabwzpi g mu si nwztikpwu lm ucmabzw xipa. Sia bizmia acabiubpdia lm mabi puabpbckpwu xcjspki, icbwuwti g sipki awu si lwkmukpi, si pudmabpñikpwu g si lpncapwu lm si kcsbczi. Mu ms tculw ikilmtpkw ma zmkwuwkpli kwtw cui cupdmzaplil lm mfkmsmukpi. Si CUIT zmaxwulm is xzmamubm g tpzi ms ncbczw kwtw ms xzwgmkbw kcsbczis tia ptxwzbiubm lm Tmfpkw. Si CUIT ma cu maxikpw lm spjmzbilma. Mu mssi am xzikbpki kwbplpiuitmubm ms zmaxmbw, si bwsmziukpi g ms lpiswñw. Si xsczisplil lm plmia g lm xmuaitpmubw ma ixzmkpili kwtw apñuw lm ac zpycmhi g ucuki kwtw nikbwz lm lmjpsplil."
mensaje = mensaje.lower()
frase_cif = cifrado_cesar(mensaje)
print(frase_cif)

                              
                                            
            
           