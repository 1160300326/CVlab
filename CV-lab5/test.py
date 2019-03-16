#!/usr/bin/python
# -*- coding: UTF-8 -*-

import NoiseRemove
import cv2
import PictureAdjust
import Statistic
import PictureSharpen
import quick_median
n = 'noise2'
s = 'test'
#NoiseRemove.meanblur(n)
#NoiseRemove.medianblur(n)
#PictureAdjust.BrightnessAdjust(s)
#PictureAdjust.ContrastAdujust(s)
#PictureAdjust.HueAdjust(s)
#PictureAdjust.SaturationAdjust(s)
#Statistic.Grayscale_Histogram(s)
#PictureSharpen.Roberts(s)
PictureSharpen.Sobel(s)
#quick_median.Quick_Median(n)

