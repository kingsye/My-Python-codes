# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 03:37:41 2021

@author: Administrator
"""
n=int(input())

inc = 1
nume=1
de=1
sign = 1
listsign=[]
listnume=[]
listde=[]
listdivision=[]
listdivsign=[]
pi=0
summ=0
while inc<= n:
    inc+=1
    
    print("numerator ",nume)
    print("denominator ", de)
    print("sign ", sign)
    
#assigning the numerators, denominators and signs in lists
    listsign.append(sign)
    listnume.append(nume)
    listde.append(de)
#increasing the numerators, denominators and signs
    nume=1
    de+=2
    sign = -1*sign
    
#printing the numerators, denominators and signs
print("numerators are ",listnume)
print("denomitors are ",listde)
print("sign are ",listsign)

#dividing the sign element by denominators and assigning 
#them in a new list, since the numerator is already 1 and sign is also 1
listdivision= [int(b) / int(m) for b,m in zip(listsign, listde)]
print("division are ", listdivision)

"""
NOT IMPORTANT!!!
#changing the sign of the division and assigning them in a new list
#listdivsign= [int(up) * int(dw) for up,dw in zip(listsign, listdivision)]
#print("sign changed are ", listdivsign)
"""
# 
for at in range(0,len(listdivision)):
    
    summ=summ+listdivision[at]
print(summ)

pi=summ*4
print("%.5f" %pi)
    
    
    
    