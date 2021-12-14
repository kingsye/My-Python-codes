# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 19:32:24 2021

@author: Administrator
"""


n = []
c=int(input())

grac=0
grbc=0
grcc=0
grdc=0
grec=0

#list to hold the grade values for evrty grade
gra = []
grb = []
grc = []
grd = []
gre = []

for i in range(c):
    i=int(input())
    n.append(i)
print(n)

for d in n:
    if d >=90:
        gra.append(d)
        grac = len(gra)
    elif d >=80:
        grb.append(d)
        grbc = len(grb)
    elif d>=70:
        grc.append(d)
        grcc = len(grc)
    elif d>= 60:
        grd.append(d)
        grdc = len(grd)
    else:
        gre.append(d)
        grec = len(gre)
print("A = ",gra)
print("B = ",grb)
print("C = ", grc)
print("D = ", grd)
print("E =", gre)
print("A=",grac,sep="", end=",")
print("B=",grbc,sep="", end=",")
print("C=",grcc,sep="",end=",")
print("D=",grdc,sep="",end=",",)
print("E=",grec,sep="")
