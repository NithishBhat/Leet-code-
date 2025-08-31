# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 22:20:01 2025

@author: Red
"""

strs=["flower","flow","flight"]

common=strs[0]
temp=""
for i in strs[1:]:
    for j,k in zip(i,common) :
        if j==k:
            temp=temp+j
        else:
            break
    common=temp
    temp=""
