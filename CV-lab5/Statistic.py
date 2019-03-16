#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 
import numpy as np
from matplotlib import pyplot as plt

    
def Grayscale_Histogram(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    r = np.zeros([32])
    g = np.zeros([32])
    b = np.zeros([32])
    for i in range(rows): 
        for j in range(cols): 
            b[int(img[i,j][0]/8)] = b[int(img[i,j][0]/8)] + 1
            g[int(img[i,j][1]/8)] = b[int(img[i,j][1]/8)] + 1
            r[int(img[i,j][2]/8)] = b[int(img[i,j][2]/8)] + 1
    plt.bar(range(32),b)
    plt.show()
    plt.bar(range(32),g)
    plt.show()
    plt.bar(range(32),r)
    plt.show()