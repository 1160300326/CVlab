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
    sgn = [0 for i in range(frameNum)]
    opdata = []
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
        
    enavg=numpy.mean(en[1:10])
    zcravg=numpy.mean(zcr[1:10])
    ensig=numpy.std(en[1:10])
    zcrsig=numpy.std(zcr[1:10])
    
    IEN = enavg+3*ensig
    IZCR = zcravg+3*zcrsig
    
    for i in range(frameNum):
        if en[i]>=IEN : sgn[i] = 1
        if zcr[i]>=IZCR : sgn[i] = 1
      
    for i in range(frameNum):
        plen = min(frameSize,wlen-(frameSize*i))
        if sgn[i] == 1:
            for j in range(1,plen):
                opdata.append(wave_data[i*frameSize+j]) 
    
    f1=open(str(k)+'.pcm','wb')
    for i in range(len(opdata)):
        #print(str(opdata[i]))
        f1.write(opdata[i])
    f1.close();
        