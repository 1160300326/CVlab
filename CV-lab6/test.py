#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2 as cv 
import numpy as np 
sigma_d = 1
dis_space = np.zeros([3][3])
dis_space = np.array([[1, 2, 1], 
                        [2, 4, 2], 
                        [1, 2, 1]])
dis_similar = np.array([[1, 1, 1], 
                        [1, 1, 1], 
                        [1, 1, 1]])
print(dis_similar * dis_space)