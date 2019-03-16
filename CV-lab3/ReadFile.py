#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
import struct
class ReadFile():
    
    def __init__(self,filename):
        f = open(filename , 'rb')
        self.nframes = int.from_bytes(f.read(4) , byteorder = 'big')
        self.frate   = int.from_bytes(f.read(4) , byteorder = 'big')
        self.nbytes = int.from_bytes(f.read(2) , byteorder = 'big')
        self.feakind = int.from_bytes(f.read(2) , byteorder = 'big')
        self.ndim = int(self.nbytes/4)
        self.N = numpy.zeros([self.nframes,self.ndim])
        for i in range(self.nframes):
            for j in range(self.ndim):
                flo = struct.unpack('>f', f.read(4))[0]
                self.N[i][j] = flo
        f.close()
    
    def getN(self):
        return self.N