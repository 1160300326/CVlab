#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 
import numpy as np

def Quick_Median(filename):
    img = cv2.imread(filename+'.bmp')
    rows,cols,channels=img.shape
    dst = img.copy()
    for i in range(1,rows-1): 
        b = np.zeros([9])
        g = np.zeros([9])
        r = np.zeros([9])
        hist_r = np.zeros([256])
        hist_g = np.zeros([256])
        hist_b = np.zeros([256])
        for k in range (3):
            for l in range(3):
                b[k*3+l] = img[i+k-1,l][0]
                g[k*3+l] = img[i+k-1,l][1]
                r[k*3+l] = img[i+k-1,l][2]
                hist_b[img[i+k-1,l][0]] = hist_b[img[i+k-1,l][0]] + 1
                hist_g[img[i+k-1,l][1]] = hist_g[img[i+k-1,l][1]] + 1
                hist_r[img[i+k-1,l][2]] = hist_r[img[i+k-1,l][2]] + 1
        img[i,1][0] = np.sort(b)[4]
        img[i,1][1] = np.sort(g)[4]
        img[i,1][2] = np.sort(r)[4]
        median_b = img[i,1][0]
        median_g = img[i,1][1]
        median_r = img[i,1][2]
        num_b = 4
        num_g = 4
        num_r = 4
        for j in range(2,cols-1): 
            for k in range (3):
                hist_b[img[i+k-1,j-2][0]] = hist_b[img[i+k-1,j-2][0]] - 1
                hist_g[img[i+k-1,j-2][1]] = hist_g[img[i+k-1,j-2][1]] - 1
                hist_r[img[i+k-1,j-2][2]] = hist_r[img[i+k-1,j-2][2]] - 1
                if (img[i+k-1,j-2][0] < median_b) : num_b = num_b - 1
                if (img[i+k-1,j-2][1] < median_g) : num_g = num_g - 1
                if (img[i+k-1,j-2][2] < median_r) : num_r = num_r - 1
                hist_b[img[i+k-1,j+1][0]] = hist_b[img[i+k-1,j+1][0]] + 1
                hist_g[img[i+k-1,j+1][1]] = hist_g[img[i+k-1,j+1][1]] + 1
                hist_r[img[i+k-1,j+1][2]] = hist_r[img[i+k-1,j+1][2]] + 1
                if (img[i+k-1,j+1][0] < median_b) : num_b = num_b + 1
                if (img[i+k-1,j+1][1] < median_g) : num_g = num_g + 1
                if (img[i+k-1,j+1][2] < median_r) : num_r = num_r + 1
                if(num_b > 4):
                    while(num_b > 4):
                        median_b = median_b - 1
                        num_b = num_b - hist_b[median_b]
                    img[i,j][0] = median_b

                else :
                    while(num_b + hist_b[median_b]<= 4):
                        
                        num_b = num_b + hist_b[median_b]
                        median_b = median_b + 1
                    img[i,j][0] = median_b

                
                if(num_g > 4):
                    while(num_g > 4):
                        median_g = median_g - 1
                        num_g = num_g - hist_g[median_g]
                    img[i,j][1] = median_g

                else :
                    while(num_g + hist_g[median_g]<= 4):
                        
                        num_g = num_g + hist_g[median_g]
                        median_g = median_g + 1
                    img[i,j][1] = median_g
                    continue
                
                if(num_r > 4):
                    while(num_r > 4):
                        median_r = median_r - 1
                        num_r = num_r - hist_r[median_r]
                    img[i,j][2] = median_r

                else :
                    while(num_r + hist_r[median_r]<= 4):
                        
                        num_r = num_r + hist_r[median_r]
                        median_r = median_r + 1
                    img[i,j][2] = median_r

    cv2.imwrite('Q_median.bmp',img)