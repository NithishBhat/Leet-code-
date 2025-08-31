"""
https://leetcode.com/problems/roman-to-integer/submissions/1754159829/
"""



x="MCMXCIV"
prev=""
res=0
roman={
       "I":1,
       "V":5,
       "X":10,
       "L":50,
       "C":100,
       "D":500,
       "M":1000
       }

res=res+roman[x[0]]
prev=x[0]
for i in x[1:] :
    res=res+roman[i]
    if roman[prev]<roman[i] :
        res=res-2*roman[prev]
    prev=i
    