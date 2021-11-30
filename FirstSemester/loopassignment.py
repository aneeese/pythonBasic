#1
#USING WHILE LOOP
num=int(input("Enter the number: "))
count=1
while count<11:
    multiply=num*count
    print(num,"*",count,"=",multiply)
    count=count+1
print("End")
#USING FOR LOOP
num=int(input("Enter the number: "))
for count in range(1,11):
    multiply=num*count
    print(num,"*",count,"=",multiply)
print("End")







#2
import math
degree=0
while degree<361:
    function1=(math.sin(math.radians(degree)))
    function2=(math.cos(math.radians(degree)))
    xy=round(function1,4)
    yz=round(function2,4)
    print("degree|Sin|Cos")
    print(degree,"|",xy,"|",yz)
    degree+=10
print("End")









#3
print("kilograms\tPounds\t | \tPounds\t\tKilograms")
K=1
p=20
while K<=199 and p<=515:
    print(K,"\t\t",round((K*2.2),2),"\t\t",p,"\t","\t",round((p*0.45),2))
    K=K+2
    p=p+5







#4
numStudents=eval(input("Enter the number of students:"))
score1=eval(input("Enter the score of student1:"))
score2=eval(input("Enter the score of studnt2:"))
if score1>score2:
    highest=score1
    next_highest=score2
else:
    highest=score2
    next_highest=score1
for x in range(2,numStudents):
    score=int(input("Enter scores of students:"))
    if score>highest:
        next_highest=highest
        highest=score
    elif score>next_highest:
        next_highest=score
print("The highest score is",highest)
print("The next highest score is",next_highest)









#5
import time
import random
start=time.time()
score=0#for count of correct answers
count=0#for repition
while count<=4:
    num1=random.randint(0,10)
    print("num1=",num1)
    num2=random.randint(1,10)
    print("num2=",num2)
    if num2>num1:
        num1,num2=num2,num1
    num3=random.randint(1,4)
    print("num3=",num3)
    if num3==1:
        print("What is",num1,"+",num2,"?")
    if num3==2:
        print("What is",num1,"-",num2,"?")
    if num3==3:
        print("What is",num1,"*",num2,"?")
    if num3==4:
        print("What is",num1,"/",num2,"?")
    ans=eval(input("Enter your answer:"))
    if num1+num2==ans or num1-num2==ans or num1*num2==ans or num1/num2==ans:
        print("Your Answer is Correct")
        score=score+1
    else:
        print("Your Answer is incorrect.Try Again")
        if num3==1:
            print(num1,"+",num2,"is",num1+num2)
        if num3==2:
            print(num1,"-",num2,"is",num1-num2)
        if num3==3:
            print(num1,"*",num2,"is",num1*num2)
        if num3==4:
            print(num1,"/",num2,"is",round(num1/num2,2))
    count=count+1
print("Correct count is",score,"out of",count)        
end=time.time()
runtime=end-start
t=round(runtime,1)
print("Runtime for the program is",t,"seconds")








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








