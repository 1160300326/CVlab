#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
import struct
from math import acos
from cmath import nan, pi

def min(r , b , g):
    if (r < b) : m = r
    else : m = b
    if (m > g) : m = g
    return m

def RGB2YIQ(num , N , Info , st, biwidth):
    filename = st +"-1160300326-YIQ.bmp"
    f = open(filename , "wb")
    for j in range(len(Info)):
        f.write(Info[j])
    height = int(num/biwidth)
    k = 4 - (3*biwidth % 4)
    for j in range(height):
        for l in range(biwidth):
            b = N[j * biwidth + l][0]
            g = N[j * biwidth + l][1]
            r = N[j * biwidth + l][2]
            y = int(0.299 * r + 0.587 * g + 0.114 * b)
            i = int(0.596 * r - 0.274 * g - 0.322 * b + 128)
            q = int(0.211 * r - 0.523 * g + 0.312 * b + 128)           
            if (y > 255) : y = 255
            if (i < 0) : i = 0
            if (i > 255) : i =255
            if (q > 255) : q = 255
            if (q < 0) : q = 0
            f.write(struct.pack("B", y))
            f.write(struct.pack("B", i))
            f.write(struct.pack("B", q))
        for l in range(k):
            f.write(struct.pack("B", 0))
    f.close()
    
def RGB2HSI(num , N , Info , st, biwidth):
    filename = st +"-1160300326-HSI.bmp"
    f = open(filename , "wb")
    for j in range(len(Info)):
        f.write(Info[j])
    height = int(num/biwidth)
    k = 4 - (3*biwidth % 4)
    for j in range(height):
        for l in range(biwidth):
            b = N[j * biwidth + l][0]
            g = N[j * biwidth + l][1]
            r = N[j * biwidth + l][2]
            su = r + g + b
            if (su < 1e-10) : 
                r = 1
                g = 1
                b = 1
            else : 
                r = r / su
                g = g / su
                b = b / su
            i = int((r + b + g) * su/3)
            s = int((1-3*min(r, b, g))*100)
            a = (2 * r - g - b)/2
            c = pow(r-g,2)+(r-b)*(g-b)
            d = pow(c,0.5)
            if (abs(a-0)<0.001 and abs(c-0)<0.001) : th = 1
            elif (c != c) :th = 1
            elif (d<1e-10) : th = 1
            else : 
                th = a/d
                if (th > 1) : th = 1
                elif (th < -1) : th = -1
            if (b > g) : h = int((2*pi - acos(th))*180/pi)
            else :h = int(acos(th)*180/pi)
            if (i > 255) : i = 255
            if (i < 0) : i = 0
            if (s > 255) : s = 255
            if (s < 0) : s = 0
            if (h > 255) : h = 255
            if (h < 0) : h = 0      
            f.write(struct.pack("B", h))
            f.write(struct.pack("B", s))
            f.write(struct.pack("B", i))
        for l in range(k):
            f.write(struct.pack("B", 0))
    f.close()
    
def RGB2YCbCr(num , N , Info , st, biwidth):
    filename = st +"-1160300326-YCbCr.bmp"
    f = open(filename , "wb")
    for j in range(len(Info)):
        f.write(Info[j])
    height = int(num/biwidth)
    k = 4 - (3*biwidth % 4)
    for j in range(height):
        for l in range(biwidth):
            b = N[j * biwidth + l][0]
            g = N[j * biwidth + l][1]
            r = N[j * biwidth + l][2]
            y = int(0.299 * r + 0.587 * g + 0.114 * b)
            cb = int(-0.169 * r - 0.331 * g + 0.5* b + 128)
            cr = int(0.5 * r - 0.419 * g - 0.081 * b + 128)           
            if (y > 255) : y = 255
            if (cb > 255) : cb = 255
            if (cb < 0) : cb = 0
            if (cr > 255) : cr = 255
            if (cr < 0) : cr = 0
            f.write(struct.pack("B", y))
            f.write(struct.pack("B", cb))
            f.write(struct.pack("B", cr))
        for l in range(k):
            f.write(struct.pack("B", 0))
    f.close()
        
def RGB2XYZ(num , N , Info , st , biwidth):
    filename = st +"-1160300326-XYZ.bmp"
    f = open(filename , "wb")
    for j in range(len(Info)):
        f.write(Info[j])
    height = int(num/biwidth)
    k = 4 - (3*biwidth % 4)
    for j in range(height):
        for l in range(biwidth):
            b = N[j * biwidth + l][0]
            g = N[j * biwidth + l][1]
            r = N[j * biwidth + l][2]
            x = int(0.412 * r + 0.358 * g + 0.18 * b)
            y = int(0.213 * r + 0.715 * g + 0.072* b)
            z = int(0.019 * r + 0.119 * g + 0.95 * b)           
            if (x > 255) : x = 255
            if (y > 255) : y = 255
            if (z > 255) : z = 255
            f.write(struct.pack("B", x))
            f.write(struct.pack("B", y))
            f.write(struct.pack("B", z))
        for l in range(k):
            f.write(struct.pack("B", 0))
    f.close()
    