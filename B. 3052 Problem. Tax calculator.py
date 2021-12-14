# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 08:03:02 2021

@author: Administrator
"""
f_s, income = eval(input())

if income < 30000:
    tax = 0
elif income <= 30000 or income < 100000:
    if f_s < 3:
        tax = (10 / 100) * income
        
    elif f_s == 3 or f_s == 4:
        tax = (7 / 100) * income
    elif f_s >= 5:
        tax = (5 / 100) * income
elif income <= 100000 or income < 500000:
    if f_s == 0 or f_s ==1 or f_s ==2 or f_s == 3:
        tax = (20 / 100) * income
    elif f_s > 3:
        tax = (15 / 100) * income
elif income >= 500000:
    tax = (30 / 100) * income

print ("%.2f" %tax)
        