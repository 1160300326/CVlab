#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
import struct
import dtw
from ReadFile import ReadFile
from record import recoder
from python_speech_features import mfcc
import scipy.io.wavfile as wav

f1 = ReadFile("mfcc/mfc/1.mfc")
f2 = ReadFile("mfcc/mfc/2.mfc")
f3 = ReadFile("mfcc/mfc/3.mfc")
f4 = ReadFile("mfcc/mfc/4.mfc")
f5 = ReadFile("mfcc/mfc/5.mfc")
f6 = ReadFile("mfcc/mfc/6.mfc")
f7 = ReadFile("mfcc/mfc/7.mfc")
f8 = ReadFile("mfcc/mfc/8.mfc")
f9 = ReadFile("mfcc/mfc/9.mfc")
f10 = ReadFile("mfcc/mfc/10.mfc")

N1 = f1.getN()
N2 = f2.getN()
N3 = f3.getN()
N4 = f4.getN()
N5 = f5.getN()
N6 = f6.getN()
N7 = f7.getN()
N8 = f8.getN()
N9 = f9.getN()
N10 = f10.getN()

for i in range (11,11):
    for j in range(4):
        f = ReadFile("mfcc/mfc/"+str(i+1)+"-"+str(j+1)+".mfc")
        N = f.getN()
        A = numpy.zeros([10])

        A[0] = dtw.dtw(N, N1)
        A[1] = dtw.dtw(N, N2)
        A[2] = dtw.dtw(N, N3)
        A[3] = dtw.dtw(N, N4)
        A[4] = dtw.dtw(N, N5)
        A[5] = dtw.dtw(N, N6)
        A[6] = dtw.dtw(N, N7)
        A[7] = dtw.dtw(N, N8)
        A[8] = dtw.dtw(N, N9)
        A[9] = dtw.dtw(N, N10)

        m , w = dtw.Min10(A)
        if (m>13):print("error!")
        else : print(w)


