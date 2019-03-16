#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 

def BrightnessAdjust(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    for i in range(rows): 
        for j in range(cols): 
            if(img[i,j][0]<200) : img[i,j][0] = img[i,j][0] + 40
            if(img[i,j][1]<200) : img[i,j][1] = img[i,j][1] + 40
            if(img[i,j][2]<200) : img[i,j][2] = img[i,j][2] + 40
    cv2.imwrite("Bright.bmp",img)
    
def HueAdjust(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    dst = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    for i in range(rows): 
        for j in range(cols): 
            dst[i,j][0] = dst[i,j][0]+20
    img2 = cv2.cvtColor(dst,cv2.COLOR_HLS2BGR)
    cv2.imwrite("Hue.bmp",img2)
    
def SaturationAdjust(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    dst = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    for i in range(rows): 
        for j in range(cols): 
            dst[i,j][2] = dst[i,j][2]+40
    img2 = cv2.cvtColor(dst,cv2.COLOR_HLS2BGR)
    cv2.imwrite("Saturation.bmp",img2)
    
def ContrastAdujust(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    for i in range(rows): 
        for j in range(cols): 
            for c in range(3):
                if (img[i,j][c] < 150 and img[i,j][c] > 50) :
                    img[i,j][c] = img[i,j][c] * 1.2 + 20
                if (img[i,j][c]>255): img[i,j] = 255
    cv2.imwrite("Contrast.bmp",img)