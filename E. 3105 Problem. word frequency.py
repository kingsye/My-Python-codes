# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:24:53 2021

@author: Administrator
"""
line=input()
line1=line.split()
a=[]
b=[]
for i in line1:
    if i!=" ":
        a.append(i)
        


mx=0

for i in a:
    if a.count(i)>mx:
        c=i
        mx+=1
b.append(c)
b.append(mx)
for i in b:
    print(i, end=" ")
print()
