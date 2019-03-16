#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 
import numpy
def Roberts(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    for i in range(rows-1): 
        for j in range(cols-1):
            robert = 0
            r = numpy.zeros([3])
            for k in range(3):
                a = abs(int(img[i,j][k]) - int(img[i+1,j+1][k]))
                b = abs(int(img[i+1,j][k]) - int(img[i,j+1][k]))
                robert = robert + a + b
            if (robert < 400):
                img[i,j] = [0,0,0]
    cv2.imwrite(filename+'_Roberts.bmp' , img)
    
def Sobel(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    for i in range(rows-1): 
        for j in range(cols-1):
            sobel = 0
            for k in range(3):
                a = abs(int(img[i-1,j-1][k]) + 2 * int(img[i,j-1][k]) + int(img[i+1,j-1][k]) - int(img[i-1,j+1][k]) - 2 * int(img[i,j+1][k]) - int(img[i+1,j+1][k]))
                b = abs(int(img[i-1,j-1][k]) + 2 * int(img[i-1,j][k]) + int(img[i-1,j+1][k]) - int(img[i+1,j-1][k]) - 2 * int(img[i+1,j][k]) - int(img[i+1,j+1][k]))
                sobel = sobel + a + b
            if (sobel < 2600) :
                img[i,j] = [0,0,0]
    cv2.imwrite(filename+'_Sobel.bmp' , img)