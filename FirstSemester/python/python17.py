w=eval(input("Enter weight in pounds:"))
h=eval(input("Enter height in inches:"))
wk=0.45359237*w
hm=0.0254*h
BMI=wk/(hm**2)
print(BMI)
