#!/usr/bin/python
import main 
import numpy
for i in range(1,11):
    cn , wlen , dn = main.DPCM_encode(i)
    main.Packet(cn, wlen,i)
    main.DPCM_decode(i)
    a = main.snr(i)
    print(a);
