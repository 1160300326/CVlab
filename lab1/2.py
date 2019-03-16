#!/usr/bin/python
import math
import wave
import numpy

for k in range(1,11):
    fn='wav/'+str(k)+'.wav'
    fw = wave.open(fn,'rb')
    params = fw.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = fw.readframes(nframes)
    wave_data = numpy.fromstring(str_data, dtype=numpy.short)
    #print(wave_data)
    fw.close()
    frameSize = 256
    wlen = len(wave_data)
    step = frameSize
    frameNum = math.ceil(wlen/step)
    zcr = []
    en = []
    for i in range(frameNum):
        result1 = 0
        result2 = 0
        plen = min(frameSize,wlen-(frameSize*i))
        for j in range(1,plen):
            if wave_data[i*frameSize+j]>=0: a=1
            else : a= -1
            if wave_data[i*frameSize+j-1]>=0: b=1
            else : b=-1
            result1 =result1 +(wave_data[i*frameSize+j] * wave_data[i*frameSize+j-1]<0)
            result2 =result2+(wave_data[i*frameSize+j]/(2*frameSize))**2
        
        result1 =result1 /(frameSize-1)
        zcr.append(result1)
        en.append(result2)
    f1=open(str(k)+'_zero.txt','w+')
    f2=open(str(k)+'_en.txt','w+')
    for i in range(len(zcr)):
        f1.write(str(zcr[i]) + '\n')
        f2.write(str(en[i]) + '\n')
    f1.close()
    f2.close()