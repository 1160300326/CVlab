#!/usr/bin/python
# -*- coding: UTF-8 -*-
from matplotlib.mlab import normpdf
from numpy import *
import matplotlib.pyplot as plt
import random
import numpy as np
#import pandas as pd
from numpy.linalg import cholesky

pai=zeros((1,20))
r=np.mat([0,3,2,-1])
r=vstack((r,mat([5,4,1,nan])))
r=vstack((r,[6,3,nan,nan]))
r=vstack((r,[5,nan,nan,nan]))##��������������󣬾�����ֵ������Ʒ�ۼۣ���Ʒ����
p=np.mat([1,0,0,0])
p=vstack((p,mat([0.75,0.25,0,0])))
p=vstack((p,[0.25,0.5,0.25,0]))
p=vstack((p,[0,0.25,0.5,0.25]))
p=np.matrix([[1,0,0,0],[0.75,0.25,0,0],[0.25,0.5,0.25,0],[0,0.25,0.5,0.25]])##����ת�Ƹ��ʾ���
ustar=zeros((4,20))#���ڼ�¼ÿһ��ֿⲻͬ״̬���ۻ��������
d=zeros((4,20))#�����¼ÿһ�������Ž�

for t in range(0,19):
    t=18-t#�ӵ����ڶ���һֱ��������һ��
    #u=zeros((1,4))
    for i in range(4):#��������״̬
        cmp=0#���ڼ�¼�����������dstar
        dtmp=0#���ڼ�¼��������Ӧ��a����d
        for a in range(4):#��������Ĺ�������
            sum=0
            for j in range(4):#����ת�Ƶĸ���
                if(i+a<4):
                    sum=sum+p[i+a,j]*ustar[j,t+1]#�û����ո���ת�Ƶ��ڶ���������������
            if(math.isnan(r[i,a])==False):
                sum=sum+r[i,a]#����r���½��������
            if(sum>cmp):
                cmp=sum#�����������
                dtmp=a
                #print(dtmp)
        ustar[i,t]=cmp#��ֵ
        #print(cmp)
        d[i,t]=dtmp
        #print(dtmp)
print(ustar)#��ӡÿһ��ÿһ״̬����ۻ���������
print(d)#��ӡÿһ������Ų���


