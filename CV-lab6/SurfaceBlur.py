#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv 
import numpy as np 
import numpy.matlib
import math

def g(x , sigma):
    return math.exp(- (x*x)/(2*sigma*sigma))

def bi_demo(image):
    dst=cv.bilateralFilter(image,0,100,5) 
    return dst

def BilateralFilter(img , sigma_d , sigma_c , size):
    img_out = img * 1.0
    
    return img_out
    
def SurfaceBlur ( img, y, half_size): 
    I_out = img * 1.0 
    row, col  = img.shape 
    w_size = half_size * 2 + 1 
    for i in range (half_size, row-1-half_size): 
        for j in range (half_size, col-1-half_size): 
            a = img [i-half_size:i+half_size+1, j-half_size : j+half_size+1] 
            p0 = img [i, j] 
            m1 = numpy.matlib.repmat(p0, w_size, w_size) 
            m2 = 1-abs(a-m1)/(2.5*y)
            m3 = m2 * (m2 > 0) 
            t1 = a * m3 
            I_out[i, j] = t1.sum()/m3.sum() 
    return I_out

img = cv.imread('test1.bmp') 
img_out = img * 1.0
thre = 15
half_size = 20
rows,cols,channels=img.shape
img_out[:, :, 0] = SurfaceBlur (img[:, :, 0], thre, half_size) 
img_out[:, :, 1] = SurfaceBlur (img[:, :, 1], thre, half_size) 
img_out[:, :, 2] = SurfaceBlur (img[:, :, 2], thre, half_size)
while(abs((img-img_out).sum()/(3*rows*cols))>=5):
    img = img_out * 1.0
    img_out[:, :, 0] = SurfaceBlur (img[:, :, 0], thre, half_size) 
    img_out[:, :, 1] = SurfaceBlur (img[:, :, 1], thre, half_size) 
    img_out[:, :, 2] = SurfaceBlur (img[:, :, 2], thre, half_size)
img_out[:, :, 0] = SurfaceBlur (img[:, :, 0], thre, half_size) 
img_out[:, :, 1] = SurfaceBlur (img[:, :, 1], thre, half_size) 
img_out[:, :, 2] = SurfaceBlur (img[:, :, 2], thre, half_size)
cv.imwrite("Remove.bmp",img_out)