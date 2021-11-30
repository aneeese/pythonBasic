# three-digit lottery number.
import random
lot=random.randint(100,999)
print(lot)
num=eval(input("Enter three digit number:"))
a=lot//100
lot=lot%100
b=lot//10
c=lot%10
d=num//100
num=num%100
e=num//10
f=num%10
if d==a and e==b and f==c:
    award=10000
    print("Congratulations! You won $",award)
elif (d==a or d==b or d==c) and (e==a or e==b or e==c) and (f==a or f==b or f==c):
    award=3000
    print("Congratulations! You won $",award)
elif d==a or d==b or d==c or e==a or e==b or e==c  or f==a or f==b or f==c:
    award=1000
    print("Congratulations! You won $",award)
