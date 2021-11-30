#three edges for a triangle to print perimeter
side1=eval(input("Ënter side of a triangle: "))
side2=eval(input("Ënter side of a triangle: "))
side3=eval(input("Ënter side of a triangle: "))
if ((side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2)):
    Peri=side1+side2+side3
    print("The perimeter of triangle is",Peri)
else:
    print("Invalid Input")
