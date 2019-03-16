#!/usr/bin/python
import wave
import numpy

class ReadWavfile():
    
    
    def __init__(self,filename):
        fn = filename
        fw = wave.open(fn,'rb')
        params = fw.getparams()
        self.nchannels, self.sampwidth, self.framerate, self.nframes = params[:4]
        self.str_data = fw.readframes(self.nframes)
        self.wave_data = numpy.fromstring(self.str_data, dtype=numpy.short)
        self.wlen = len(self.wave_data)
        
    def getData(self):
        return self.str_data
    
    def getShortData(self):
        return  self.wave_data
    
    def getLen(self):
        return self.wlen
    