#!/usr/bin/python
# -*- coding: UTF-8 -*-
from BmpFile import BmpFile 
from sys import argv
import trans

s = "test1.bmp"
st=s.split('.')
b = BmpFile(s)
N = b.getN()
Info = b.FileInfo()
num = b.getNumber()
biwidth = b.getWidth()
#trans.RGB2YIQ(num, N, Info, st[0])
#trans.RGB2HSI(num, N, Info, st[0])
#trans.RGB2YCbCr(num, N, Info, st[0])
trans.RGB2XYZ(num, N, Info, st[0] , biwidth)