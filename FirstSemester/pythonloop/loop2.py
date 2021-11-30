#2
import math
print("degree|Sin|Cos")
degree=0
while degree<361:
    function1=(math.sin(math.radians(degree)))
    function2=(math.cos(math.radians(degree)))
    xy=round(function1,4)
    yz=round(function2,4)
    print(degree,"|",xy,"|",yz,)
    degree+=10
print("End")
