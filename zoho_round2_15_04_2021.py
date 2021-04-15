# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:15:38 2021

@author: keerthana
"""
n = input("enter the string :")

l = len(n)

s1 = n[:l//2]

s2 = n[l//2 :]


result = s2 + s1
for i in range(0, l):
    for j in range(0, l - i):
        print(" ", end = ' ')
        
    for k in range(0, i + 1):
        print(result[k], end = ' ')
        
    print("\n")
        
