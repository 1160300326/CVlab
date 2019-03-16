#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 
import numpy as np

def meanblur(filename):
    img = cv2.imread(filename+'.bmp')
    dst = np.array(img)
    rows,cols,channels=img.shape
    for i in range(1,rows-1): 
        for j in range(1,cols-1): 
            b = int(img[i,j][0])+ int(img[i-1,j-1][0])+ int(img[i-1,j][0])+ int(img[i-1,j+1][0])+ int(img[i,j-1][0])+ int(img[i,j+1][0])+ int(img[i+1,j-1][0])+ int(img[i+1,j][0])+ int(img[i+1,j+1][0])
            g = int(img[i,j][1])+ int(img[i-1,j-1][1])+ int(img[i-1,j][1])+ int(img[i-1,j+1][1])+ int(img[i,j-1][1])+ int(img[i,j+1][1])+ int(img[i+1,j-1][1])+ int(img[i+1,j][1])+ int(img[i+1,j+1][1])
            r = int(img[i,j][2])+ int(img[i-1,j-1][2])+ int(img[i-1,j][2])+ int(img[i-1,j+1][2])+ int(img[i,j-1][2])+ int(img[i,j+1][2])+ int(img[i+1,j-1][2])+ int(img[i+1,j][2])+ int(img[i+1,j+1][2])
            img[i,j][0] = int(b/9)
            img[i,j][1] = int(g/9)
            img[i,j][2] = int(r/9)
    cv2.imwrite(filename+'_mean.bmp' , img)
    
def medianblur(filename):
    img = cv2.imread(filename+'.bmp')
    dst = np.array(img)
    rows,cols,channels=img.shape
    for i in range(1,rows-1): 
        for j in range(1,cols-1): 
            b = np.zeros([9])
            g = np.zeros([9])
            r = np.zeros([9])
            b[0] = img[i-1,j-1][0]
            b[1] = img[i-1,j][0]
            b[2] = img[i-1,j+1][0]
            b[3] = img[i,j-1][0]
            b[4] = img[i,j][0]
            b[5] = img[i,j+1][0]
            b[6] = img[i+1,j-1][0]
            b[7] = img[i+1,j][0]
            b[8] = img[i+1,j+1][0]
            g[0] = img[i-1,j-1][1]
            g[1] = img[i-1,j][1]
            g[2] = img[i-1,j+1][1]
            g[3] = img[i,j-1][1]
            g[4] = img[i,j][1]
            g[5] = img[i,j+1][1]
            g[6] = img[i+1,j-1][1]
            g[7] = img[i+1,j][1]
            g[8] = img[i+1,j+1][1]
            r[0] = img[i-1,j-1][2]
            r[1] = img[i-1,j][2]
            r[2] = img[i-1,j+1][2]
            r[3] = img[i,j-1][2]
            r[4] = img[i,j][2]
            r[5] = img[i,j+1][2]
            r[6] = img[i+1,j-1][2]
            r[7] = img[i+1,j][2]
            r[8] = img[i+1,j+1][2]
            img[i,j][0] = np.sort(b)[4]
            img[i,j][1] = np.sort(g)[4]
            img[i,j][2] = np.sort(r)[4]
    cv2.imwrite(filename+'_median.bmp' , img)
    
    