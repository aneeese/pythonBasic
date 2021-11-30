#a
s1="Welcome"
s2="welcome"
isEqual=(s1==s2)
print(isEqual)
#b
s1="Welcome"
s2="welcome"
isEqual=(s1.lower()==s2.lower())
print(isEqual)
#c
s1="Welcome"
s2="welcome"
b=(s1.startswith('AAA'))
print(b)
#d
s1="Welcome"
s2="welcome"
b=(s1.endswith('AAA'))
print(b)
#f
s1="Welcome"
s2="welcome"
x=len(s1)
print(x)
#g
s1="Welcome"
s2="welcome"
x=s1[0]
print(x)
#h
s1="Welcome"
s2="welcome"
s3=s1 + s2
print(s3)
#i
s1="Welcome"
s2="welcome"
substring=s1[1:7]
print(substring)
#j
s1="Welcome"
s2="welcome"
substring=s1[1:5]
print(substring)
#k
s1="Welcome"
s2="welcome"
s3=s1.lower()
print(s3)
#l
s1="Welcome"
s2="welcome"
s3=s1.upper()
print(s3)
#m
s1="Welcome"
s2="welcome"
s3=s1.strip()
print(s3)
#n
s1="Welcome"
s2="welcome"
x=s1.replace('e','E')
print(x)
#o
s1="Welcome"
s2="welcome"
x=s1.find('e')
print(x)
#p
s1="Welcome"
s2="welcome"
x=s1.find('abc')
print(x)






#############3
s=()
x=len(s)
print(x)
#It will have zero length












#############3
CNIC=eval(input("Enter your CNIC number in format ddddd-ddddddd-d: "))
y=str(CNIC)
x=len(y)
i=len('ddddd-ddddddd-d')
if x==8 and i==15:
    print("Valid CNIC")
else:
    print("Invalid CNIC")




    

