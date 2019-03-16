#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ReadWavfile import ReadWavfile
import struct
import numpy
def DPCM_encode(f):
    filename = 'wav/'+str(f)+'.wav'
    file = ReadWavfile(filename)
    wave_data = file.getShortData()
    dn = []
    cn = []
    xn_predict = []
    a = 400
    wlen = file.getLen()
    dn.append(wave_data[0])
    xn_predict.append((wave_data[0]))
    cn.append(wave_data[0])
    for i in range(len(wave_data)-1):
        dn.append(wave_data[i+1] - xn_predict[i])
        if dn[i+1] > 7*a:
            cn.append(7)
        elif dn[i+1] < -8*a:
            cn.append(-8)
        else:
            cn.append(int(dn[i+1]/a))
        cn[i+1] = cn[i+1] + 8
        xn_predict.append(xn_predict[i] + (cn[i+1] - 8)*a)
    return cn , wlen , wave_data
        
def Packet(cn , wlen , f):
    f1 = open(str(f)+'.dpc',"wb")
    num = wlen
    wn = []
    wn.append(cn[0])
    f1.write(struct.pack("i", cn[0]))
    for i in range(1,num-1,2):
        a="{:04b}".format(cn[i])
        b="{:04b}".format(cn[i+1])
        st = a + b
        w = 0
        for j in range(len(st)):
            if st[j]=="1" :
                w = w|0b1;
            else:
                w=w|0b0
            w=w<<1
        w=w>>1

        f1.write(struct.pack("B", w))

def snr(f):
    cn , wlen , sc = DPCM_encode(f)
    dc = DPCM_decode(f)
    s = 0
    n = 0
    for a in range(len(sc)):
        af = numpy.longlong(dc[a])
        bef = numpy.longlong(sc[a])
        p = af * af
        q = (af - bef) * (af - bef)
        s = s + p
        n = n + q
    return numpy.log10(s / n) * 10

def read_bit(f):
    f = open(str(f)+".dpc", "rb")
    cn = []
    i=1;
    cn.append(struct.unpack('h', f.read(2))[0])
    while True:
        chunk = f.read(1)
        
        if not chunk:
            break
        r = struct.unpack('B', chunk)
        p = r[0] >> 4
        q = r[0] & int('00001111', 2)
        if i < 3:
            p = p/2
            q = q/2
        cn.append(p)
        cn.append(q)
        i = i + 1

    return cn

def DPCM_decode(f):
    cn = read_bit(f)
    a = 400
    for i in range(1,len(cn)):
        cn[i] = cn[i] - 8
        cn[i] = cn[i] * a
    d = []
    d.append(cn[0])
    for i in range(1, len(cn)):
        a = cn[i] + d[i - 1]
        d.append(a)
    f1=open(str(f)+'.pcm','wb')
    d = numpy.array(d, dtype=numpy.short)
    for i in range(len(d)):
        f1.write(d[i])
    f1.close()
    return d
    