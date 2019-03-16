#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

def dtw(X,Y):
    M=[[distance(X[i],Y[j]) for i in range(len(X))] for j in range(len(Y))]
    l1=len(X)
    l2=len(Y) 
    w = 0
    D=[[0 for i in range(l1+1)] for i in range(l2+1)]
    D[0][0]=0 
    for i in range(1,l1+1):
        D[0][i]=sys.maxsize
    for j in range(1,l2+1):
        D[j][0]=sys.maxsize
    for j in range(1,l2+1):
        for i in range(1,l1+1):
            minnum , a = Min(D[j-1][i],D[j][i-1],D[j-1][i-1]+M[j-1][i-1])
            D[j][i]=M[j-1][i-1]+minnum
            w = w + a
    return D[l2][l1]/w
            
def distance(a,b):
    dis = 0
    for i in range(len(a)):
        dis = dis + (a[i]-b[i])*(a[i]-b[i])
    return dis
    
def Min(a,b,c):
    w = 1
    if a>b : m = b
    else : m = a
    if m>c :
        m = c 
        w = 2
    return m , w

def Min10(N):
    w = 1
    m = N[0]
    for i in range(10):
        if m > N[i] :
            m = N[i]
            w = i+1
            
    return m , w