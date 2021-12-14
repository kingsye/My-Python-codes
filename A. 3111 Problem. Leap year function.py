# -*- coding: utf-8 -*-
"""
Created on Thu May 27 04:15:32 2021

@author: Administrator
"""
def leapcheck(styear,enyear,coun):
    
    while styear < enyear:
        styear+=1
        if (styear % 4==0) and (styear % 100==0):
            if styear % 400==0:
                leap=True
            else:
                leap=False
        elif(styear % 4==0) and (styear % 100 !=0):
             leap=True
        else:
            leap=False
        if leap==True:
            coun+=1
    print(coun)
st,en=eval(input())
coun=0

leapcheck(st,en,coun)

