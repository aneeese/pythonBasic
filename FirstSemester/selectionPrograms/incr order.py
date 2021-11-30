# increasing order.
x,y,z=eval(input("Enter three numbers separated by commas: "))
if x>y>z:
    print("Increasing Order is",z,y,x)
elif y>x>z:
    print("Increasing order is",z,x,y)
elif y>z>x:
    print("Increasing order is",x,z,y)
elif z>x>y:
    print("Increasing order is",y,x,z)
elif z>y>x:
    print("Increasing order is",x,y,z)
elif x>z>y:
    print("Increasing order is",y,z,x)
else:
    print("Invalid Number")
