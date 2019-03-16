#!/usr/bin/python
# -*- coding: UTF-8 -*-

import struct
import numpy

class BmpFile:


    def __init__(self,filename):
        f = open(filename , 'rb')
        self.Info = []
        self.Info.append(f.read(2))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(2))
        self.Info.append(f.read(2))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.Info.append(f.read(4))
        self.bfType = struct.unpack('<cc' ,self.Info[0])        
        self.bfSize = struct.unpack('<i' ,self.Info[1] )[0]
        self.bfReserved = struct.unpack('<i' ,self.Info[2] )[0]
        self.bfOffBits = struct.unpack('<i' ,self.Info[3] )[0]
        self.biSize = struct.unpack('<i' ,self.Info[4] )[0]
        self.biWidth = struct.unpack('<i' ,self.Info[5] )[0]
        self.biHeight = struct.unpack('<i' ,self.Info[6] )[0]
        self.biPlanes = struct.unpack('<h' ,self.Info[7])[0]
        self.biBitCount = struct.unpack('<h' ,self.Info[8] )[0]
        self.biCompression = struct.unpack('<i' ,self.Info[9])[0]
        self.biSizeImage = struct.unpack('<i' ,self.Info[10])[0]
        self.biXPelsPerMeter = struct.unpack('<i' ,self.Info[11])[0]
        self.biYPelsPerMeter = struct.unpack('<i' ,self.Info[12])[0]
        self.biClrUsed = struct.unpack('<i' , self.Info[13])[0]
        self.biClrImportant = struct.unpack('<i' , self.Info[14])[0]
        self.n = self.biWidth*abs(self.biHeight)
        self.N = numpy.zeros([self.n,3])
        k = 4 - (3 * self.biWidth % 4)
        for i in range (self.biHeight):
            for j in range (self.biWidth):
                self.N[i * self.biWidth + j ][0] = struct.unpack("<B" , f.read(1))[0]
                self.N[i * self.biWidth + j ][1] = struct.unpack("<B" , f.read(1))[0]
                self.N[i * self.biWidth + j ][2] = struct.unpack("<B" , f.read(1))[0]
            for l in range(k):
                f.read(1)
        f.close()
        
    def getN(self):
        return self.N
    
    def FileInfo(self):
        return self.Info
    
    def getNumber(self):
        return self.n
    
    def getWidth(self):
        return self.biWidth