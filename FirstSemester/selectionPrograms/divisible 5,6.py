#number is divisible by 5,6
num=int(input("Enter an integer: "))
count=num%5
count1=num%6
if count==0 and count1==0:
    print("Is",num,"divisible by 5 and 6?",True)
else:
    print("Is",num,"divisible by 5 and 6?",False)
if count==0 or count1==0:
    print("Is",num,"divisible by 5 or 6?",True)
else:
    print("Is",num,"divisible by 5 or 6?",False)
if count==0 or count1==0:
    print("Is",num,"divisible by 5 or 6, but not both?",True)
else:
    print("Is",num,"divisible by 5 or 6, but not both?",False)
