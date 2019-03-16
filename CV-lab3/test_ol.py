#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
import struct
import dtw
from ReadFile import ReadFile
from record import recoder
from python_speech_features import mfcc
import scipy.io.wavfile as wav

fs, audio = wav.read("mfcc/wav/1.wav")
N1 = mfcc(audio, samplerate=fs)
fs, audio = wav.read("mfcc/wav/2.wav")
N2 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/3.wav")
N3 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/4.wav")
N4 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/5.wav")
N5 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/6.wav")
N6 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/7.wav")
N7 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/8.wav")
N8 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/9.wav")
N9 = mfcc(audio, samplerate=fs )
fs, audio = wav.read("mfcc/wav/10.wav")
N10 = mfcc(audio, samplerate=fs )
inp =input("begin?(Y/N):")
while (inp == 'Y' or inp == 'y'):
    r = recoder()
    r.recoder()
    r.savewav("test.wav") 

    fs, audio = wav.read("test.wav")
    feature_mfcc = mfcc(audio, samplerate=fs )

    A = numpy.zeros([10])

    A[0] = dtw.dtw(feature_mfcc, N1)
    A[1] = dtw.dtw(feature_mfcc, N2)
    A[2] = dtw.dtw(feature_mfcc, N3)
    A[3] = dtw.dtw(feature_mfcc, N4)
    A[4] = dtw.dtw(feature_mfcc, N5)
    A[5] = dtw.dtw(feature_mfcc, N6)
    A[6] = dtw.dtw(feature_mfcc, N7)
    A[7] = dtw.dtw(feature_mfcc, N8)
    A[8] = dtw.dtw(feature_mfcc, N9)
    A[9] = dtw.dtw(feature_mfcc, N10)

    m , w = dtw.Min10(A)
    print(m)
    print(w)
    inp =input("continue?(Y/N):")