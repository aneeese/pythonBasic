x1,y1=eval(input("Enter the coordinates:"))
x2,y2=eval(input("Enter the coordinates:"))
x3,y3=eval(input("Enter the coordinates:"))
s1=((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))**(1/2)
s2=((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))**(1/2)
s3=((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**(1/2)
s=(s1+s2+s3)/2
area=((s*(s-s1)*(s-s2)*(s-s3))**(1/2))
print("The area of triangle is",area)
