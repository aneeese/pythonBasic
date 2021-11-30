#6
#a
num=eval(input("Enter a number:"))
fac=1
while num>=2:
    fac=fac*num
    num=num-1
print("Factorial of number is",fac)




#b
num=eval(input("Enter a number:"))
fac=1
for num in range(num,1,-1):
    fac=fac*num
print("Factorial of number is",fac) 
