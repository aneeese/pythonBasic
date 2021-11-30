#4.1 six comparison operators are:
#greater than (>)
#less than (<)
#greater than equal to (>=)
#less than equal to (<=)
#equals to (==)
#not equal to (!=)






#4.2
#a
i=eval(input("Enter a number:"))
i=int(True)
print(i)
##ANSWER IS "1"
#b
i=eval(input("Enter a number:"))
i=int(False)
print(i)
##ANSWER IS "0"
#c
b1=eval(input("Enter a number:"))
b1=bool(4)
print(b1)
##ANSWER IS "TRUE"
#d
b2=eval(input("Enter a number:"))
b2=bool(0)
print(b2)
##ANSWER IS "FALSE"
#Yes, the above Conversions are allowed.






#4.3
#random integer 0<=i<20
import random
rand=random.randint(0,19)
print(rand)






#4.4
#random integer 10<=i<20
import random
rand=random.randint(10,19)
print(rand)






#4.5
#random integer 10<=i<50
import random
rand=random.randint(10,49)
print(rand)






#4.6
#random integer o or 1
import random
rand=random.randint(0,1)
print(rand)






#4.7 if statement that assigns 1 to x if y is greater than 0.

num=eval(input("enter a number:"))
y=num//2
if y>0:
    print("x=1")






#4.8 Write an if statement that increases pay by 3% if score is greater than 90.

score=eval(input("enter your score:"))
if score>90:
    pay=eval(input("enter the pay:"))
    final_pay=pay*1.03
    print("Increase in pay is",final_pay)






#4.9 Write an if statement that increases pay by 3% if score is greater than 90, otherwise it increases pay by 1%

score=eval(input("Enter your score:"))
pay=eval(input("enter the pay:"))
if score>90:
    final_pay=pay*1.03
    print("Pay is",final_pay)
else:
    final_pay=pay*1.01
    print("Pay is",final_pay)






#4.10 what is printout of these codes if number iss 30 and 35 respectively?

#A
num=eval(input("Enter a number:"))
count=num%2
if num%2==0:
    print(num,"ïs even")
print(num,"is odd")
#ANSWER: IF WE ENTER 30 it gives output that 30 is even.

#B
num=eval(input("Enter a number:"))
count=num%2
if num%2==0:
    print(num,"is even.")
else:
    print(num,"is odd.")
#ANSWER: IF WE ENTER 35 it gives output that 35 is odd.





    
#4.13 What is wrong in the following code?

if score >= 60.0:
   grade = 'D'
elif score >= 70.0:
   grade = 'C'
elif score >= 80.0:
   grade = 'B'
elif score >= 90.0:
   grade = 'A'
else:
   grade = 'F'
#Answer: Conditions for this program are in incorrect order. Let we enter score is 100, then for the given code, value of grade will be "D" but actually it should have grade "A".






#4.14 Which of following statement are equivalent and are correctly indented?

#(A)
if i>0:
    x=0
    y=0
else:
    y=0
    z=0


#(B)
if i>0:
    x=0
    y=1
else:
    y=0
    z=0

#(C)
if i>0:
  x=0
  y=1
else:
    y=0
    z=0

#(D)
if i>0:
  x=0
  y=1
else:
    y=0
    z=0

#Answer: (A) and (C) both are alike and both are correctly intended.






#4.15 Rewritten statement in  boolean form:

count=eval(input("Enter value:"))
newLine=count%10
if newLine==0:
    newLine=bool(True)
    print(newLine)
else:
    newLine=bool(False)
    print(newLine)






#4.16 Are these statements correct?Which is better?

#A
if age<16:
    print("Cannot get a driver's license")
if age >=16:
    print("Can get a driver's license")


#B
if age<16:
    print("Cannot get a driver's license")
else:
    print("Can get a driver's license")
#ANSWER: Both are correct but "B" is better becausse it uses (if,else) rather than 2 ifs as the condition in 2 ifs are complement to each other.






#4.17 Write input if num is 14,15 and 30.

    #A
num=eval(input("Enter a number:"))
if num%2==0:
    print(num,"is even")
if num%5==0:
    print(num,"is multiple of 5")
    #B
num=eval(input("Enter a number:"))
if num%2==0:
    print(num,"is even")
elif num%5==0:
    print(num,"is multiple of 5")
#ANSWER: For 14 both A and B gives answer that 14 is even.
#For 15 and 30 both A and B gives output that they are multiple of 5.   






#4.18 Are the following statements equivalent?

income=eval(input("enter your income:"))
if income<=10000:
    tax=income*0.1
    print(tax)
elif income<=20000:
    tax=1000+(income-10000)*0.15
    print(tax)

    #B
income=eval(input("enter your income:"))
if income<=10000:
    tax=income*0.1
    print(tax)
elif income>10000 and income<=20000:
    tax=1000+(income-10000)*0.15
    print(tax)
#ANSWER: Yes both are equivalent.






#4.19 What is wrong in this code?

income=eval(input("enter your income:"))
if income<=10000:
    tax=income*0.1
    print(tax)
elif income>10000 and income<=20000:
    tax=1000+(income-10000)*0.15
    print(tax)
#ANSWER: since income is greater than 20000, it will never meet both given conditions so programm will give error.






#4.20 Give results of these boolean expressions
x=eval(input("Enter value:"))
b1=True and (3>4)
print(b1)#ANSWER:FALSE
b2=not(x>0)and(x>0)
print(b2)#ANSWER:FALSE
b3=(x>0)or(x<0)
print(b3)#ANSWER:TRUE)
b4=(x!=0)or(x==0)
print(b4)#ANSWER:TRUE
b5=(x>=0)or(x<0)
print(b5)#ANSWER:TRUE
b6=(x!=1)==(not(x==1))
print(b6)#ANSWER:TRUE






#4.21 Write a Boolean expression that evaluates to True if variable num is between 1 and 100

num=eval(input("Enter value:"))
if num>=1 and num<=100:
   print(True)
else:
   print(False)






#4.26 when you run the following program, you enter input 2, 3, 6 from the console. What is the output?

x, y, z = eval(input("Enter three numbers: "))
b1=x<y and y<z
print("(x < y and y < z) is",b1)#ANSWER:TRUE
b2=x<y or y<z
print("(x < y or y < z) is",b2)#ANSWER:TRUE
b3=not(x<y)
print("not (x < y) is",b3)#ANSWER:FALSE
b4=x<y<z
print("(x < y < z) is",b4)#ANSWER:TRUE
b5=not(x<y<z)
print("not(x < y < z) is",b5)#ANSWER:FALSE






#4.27 Boolean expression that evaluates true if age is greater than 13 and less than 18.

age=eval(input("enter age:"))
if age>13 and age<18:
    print(True)






#4.31 you enter the input 2, 3, 6 from the console. What is the output?

x, y, z = eval(input("Enter three numbers: "))
print("sorted" if x < y and y < z else "not sorted")
#ANSWER: SORTED






#4.33 Rewritten programs

#A
scale=eval(input("Enter number:"))
if scale>10:
    score=3*scale
    print(score)
else:
    score=4*scale


#B
income=eval(input("Enter number:"))
if income>10000:
    tax=income*0.2
    print(tax)
else:
    tax=income*0.17+1000
    print(tax)


#C
num=eval(input("Enter number:"))
if num%3==0:
    print("i")
else:
    print("j")





    
#4.37 Are they all same?

#A
x=eval(input("Enter number:"))
b1=(x>0 and x<10)
print(b1)
b2=((x>0)and(x<10))
print(b2)


#B
x=eval(input("Enter number:"))
b3=(x>0 or x<10)
print(b3)
b4=((x>0)or(x<10))
print(b4)


#C
x=eval(input("Enter number:"))
b5=(x>0 or x<10 and y<0)
print(b5)
b6=(x>0 or(x<10 and y<0))
print(b6)

#ANSWER: Yes they all are same


    
