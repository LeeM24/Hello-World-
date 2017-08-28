#!/usr/bin/env python

import math

mevq = 1024

byte = "byte"

mbyte = "mbyte"

print("Convertitore BTMB (Byte-To-MegaByte)  V. 0.01")
menu = input("Premi 1 per: byte to mbyte -- 2 per: mbyte to byte:  ")

if menu == 1:
    print("(Byte-To-MegaByte)")
    byte = float(input("byte:  "))  #rimuovere 'float' per un numero arrotondato
    if byte == 0:
	    print("byte=0")
	    exit()

    risultato = byte / 1024
    print risultato, ("Mb")

if menu == 2:
	print("(MegaByte-To-Byte)")
	mbyte = float(input("mbyte:  "))  #rimuovere 'float' per un numero arrotondato
	if mbyte == 0:
		print("mbyte=0")
		exit()
	risultato_m = mbyte * 1024
	print risultato_m, ("Kb")	
