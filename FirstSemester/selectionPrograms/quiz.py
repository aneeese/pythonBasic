#create a quiz
import random
num1=random.randint(0,100)
print("num1=",num1)
num2=random.randint(0,100)
print("num2=",num2)
num3=random.randint(1,4)
print("num3=",num3)
if num3==1:
    print(num1,"+",num2,"=")
if num3==2:
    print(num1,"-",num2,"=")
if num3==3:
    print(num1,"*",num2,"=")
if num3==4:
    print(num1,"/",num2,"=")
ans=eval(input("Enter your answer:"))
if num1+num2==ans or num1-num2==ans or num1*num2==ans or num1/num2==ans:
    print("Your Answer is Correct")
else:
    print("Your Answer is incorrect.Try Again")
