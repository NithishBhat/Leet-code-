"""
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26
"""

import math

dimensions=[[25,60],[39,52],[16,63],[33,56]]

diag=0
new=0
area=0
for i in dimensions:
    new=math.sqrt(math.pow(i[0],2)+math.pow(i[1],2))
    print(i,new)
    if new>diag:
        diag=new
        area=i[0]*i[1]
        
        
print(area)


"""
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        import math
        diag=0
        new=0
    
        for i in dimensions:
            new=math.sqrt(math.pow(i[0],2)+math.pow(i[1],2))
            if new>diag:
                diag=new
                area=area=i[0]*i[1]
            elif new==diag and i[0]*i[1]>area:
                area=i[0]*i[1]
                diag=new
        return area
"""