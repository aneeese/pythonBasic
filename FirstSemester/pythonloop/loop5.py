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
