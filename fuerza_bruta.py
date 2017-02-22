#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from math import ceil
from math import floor

#It's Pizza Time

#Files
file_in = "data/big.in"
file_out = "data/out.txt"

#Global vars

# N x M (char, n slice), 0
global Matrix
# Lista con los tipos de trozos
global tipoTrozos
# Slice Array, index = n slice in Matrix
global Slices
global ROW
global COL
global MIN
global MAX

#Functions

def generaTrozos(min, max):
    global ROW, COL, tipoTrozos,Slices
    ntrozos = 0
    tipoTrozos = []
    for i in range(1, max + 1):
        for j in range(int(ceil(min / i)), int(floor(max / i)) + 1):
            if i <= ROW and j > 0 and j <= COL:
                Slices.append([])
                ntrozos+=1
                tipoTrozos.append((i, j))

    # Slices[1].append("hola")
    # Slices[1].append("adios")
    # print Slices

def read(file_name):
    f = open(file_name, 'r')
    global ROW, COL, MIN, MAX, Matrix
    ROW, COL, MIN, MAX = f.readline().strip().split()
    ROW, COL, MIN, MAX = int(ROW), int(COL), int(MIN), int(MAX)

    # Generamos la lista de formas posibles
    generaTrozos(MIN * 2, MAX)

    #Comprehension list, magia oscura
    # Matrix = [[(ch , []) for ch in line.strip()] for line in f]
    Matrix = [[(ch , 0) for ch in line.strip()] for line in f]

def write(file_name):
    global Slices
    f = open(file_name, 'w')
    for linea in Matrix:
        print linea

    print ""

    # for linea in Slices:
    #     print linea
    # print Slices
    # f.write(Slices)

def encajaTrozo(r1,c1,r2,c2,indice):
    global MIN,MAX
    setas, tomates = 0,0
    for x in range(r1,r2+1):
        for y in range(c1,c2+1):
            (food, _) = Matrix[x][y]
            if food == "T":
                tomates+=1
            else:
                setas+=1
    if (tomates >= MIN and setas >= MIN):
        Slices[indice].append((r1,c1,r2,c2))
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                (food, trozos) = Matrix[x][y]
                Matrix[x][y] = (food, trozos+1)
                # Matrix[x][y] = (food, trozos.append((indice,len(Slices[indice]))))

    #Si encaja se mete en slices

def run():
    global ROW, COL, Matrix, Slices, tipoTrozos
    r1, c1, r2, c2 = 0, 0, 0, 0
    trozoActual = 0
    Slices = []
    read(file_in)

    # Bloque
    indice = 0
    for tupla in tipoTrozos:
        (altura, anchura) = tupla
        for x in range(0,ROW-altura):
            for y in range(0, COL-anchura):
                encajaTrozo(x,y,x+altura, y+anchura,indice)

    # Volcamos la solución
    write(file_out)

if __name__ == '__main__':
    run()
