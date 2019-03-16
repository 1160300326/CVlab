# -*- coding: UTF-8 -*-
import numpy as np
import cv2
import math

def BilateralFilter(img , sigma_r , sigma_d) : 
    B = img * 1
    dis_space = np.zeros((sigma_d * 2 + 1,sigma_d * 2 + 1))
    dis_similar = np.zeros((sigma_d * 2 + 1,sigma_d * 2 + 1))
    for row in range(sigma_d, len(B) - sigma_d) :
        for col in range(sigma_d, len(B[row]) - sigma_d) :
            arr = img[row-sigma_d:row+sigma_d+1, col-sigma_d:col+sigma_d+1] 
            for i in range(2 * sigma_d + 1) :
                for j in range(2 * sigma_d + 1) :
                    a = float(-int(arr[i][j] - arr[sigma_d][sigma_d])*int(arr[i][j] - arr[sigma_d][sigma_d]) / (2 * sigma_r * sigma_r))
                    dis_similar[i][j] = math.exp(a)
                    b = float(((i-sigma_d)*(i-sigma_d) + (j-sigma_d)*(j-sigma_d))/(-2 * sigma_d * sigma_d))
                    dis_space[i][j] = math.exp(b)
            weight = dis_similar * dis_space
            sum = np.sum(weight)
            value = 0.0
            for i in range(2 * sigma_d + 1) :
                for j in range(2 * sigma_d + 1) :
                    value = value + weight[i][j] * arr[i][j]
            B[row][col] = int(value/sum)
    return B

img = cv2.imread("test1.bmp")

img_out = img * 1
img_out[:, :, 0] = BilateralFilter(img[:, :, 0] , 100 , 1)
img_out[:, :, 1] = BilateralFilter(img[:, :, 1] , 100 , 1)
img_out[:, :, 2] = BilateralFilter(img[:, :, 2] , 100 , 1)
cv2.imshow('result',img_out)
cv2.waitKey(0)

