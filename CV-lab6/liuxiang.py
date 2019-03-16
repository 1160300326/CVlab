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
r=vstack((r,[5,nan,nan,nan]))##生成期望收益矩阵，具体数值根据商品售价，商品单价
p=np.mat([1,0,0,0])
p=vstack((p,mat([0.75,0.25,0,0])))
p=vstack((p,[0.25,0.5,0.25,0]))
p=vstack((p,[0,0.25,0.5,0.25]))
p=np.matrix([[1,0,0,0],[0.75,0.25,0,0],[0.25,0.5,0.25,0],[0,0.25,0.5,0.25]])##生成转移概率矩阵
ustar=zeros((4,20))#用于记录每一天仓库不同状态下累积最大收益
d=zeros((4,20))#用与记录每一步的最优解

for t in range(0,19):
    t=18-t#从倒数第二天一直遍历到第一天
    #u=zeros((1,4))
    for i in range(4):#遍历今天状态
        cmp=0#用于记录最大收益填入dstar
        dtmp=0#用于记录最大收益对应的a填入d
        for a in range(4):#遍历今天的购进策略
            sum=0
            for j in range(4):#遍历转移的概率
                if(i+a<4):
                    sum=sum+p[i+a,j]*ustar[j,t+1]#用户按照概率转移到第二天的期望最大收益
            if(math.isnan(r[i,a])==False):
                sum=sum+r[i,a]#根据r更新今天的收益
            if(sum>cmp):
                cmp=sum#如果最大则更新
                dtmp=a
                #print(dtmp)
        ustar[i,t]=cmp#赋值
        #print(cmp)
        d[i,t]=dtmp
        #print(dtmp)
print(ustar)#打印每一天每一状态最大累积期望收益
print(d)#打印每一天的最优策略


