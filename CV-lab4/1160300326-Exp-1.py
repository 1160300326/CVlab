#!/usr/bin/python
# -*- coding: UTF-8 -*-

from BmpFile import BmpFile 
from sys import argv
import trans

s = argv[1]
#s = "test.bmp"
st=s.split('.')
b = BmpFile(s)
N = b.getN()
Info = b.FileInfo()
num = b.getNumber()
biwidth = b.getWidth()
#trans.RGB2YIQ(num, N, Info, st[0], biwidth)
trans.RGB2HSI(num, N, Info, st[0], biwidth)
#trans.RGB2YCbCr(num, N, Info, st[0], biwidth)
#trans.RGB2XYZ(num, N, Info, st[0], biwidth)