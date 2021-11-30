#1.	What is the output of the following code?
list1 = list(range(1, 10, 2))
list2 = list1
list1[0] = 111
print(list1)
print(list2)
#The answer is [111,3,5,7,9] for both lists










#2.	What is the output of the following code?
list1 = list(range(1, 10, 2))
list2 = [] + list1
list1[0] = 111
print(list1)
print(list2)
#The answer is [111,3,5,7,9] and [1,3,5,7,9]











#4
m=[]
print("Enter Scores:")
for i in range(5):
    num=eval(input())
    m.append(num)
max=max(m)
for i in range(len(m)):
    grade=''
    if m[i]>=max-10:
        grade='A'
    elif m[i]>=max-20:
        grade='B'
    elif m[i]>=max-30:
        grade='C'
    elif m[i]>=max-40:
        grade='D'
    else:
        grade='F'
    print('Student',i ,  'score is ', m[i], 'and grade is' ,grade)












#5
m=[]
print("Enter number:")
for i in range(5):
    num=eval(input())
    m.append(num)
m.reverse()
print(m)










#6
list1=[]
n=eval(input('Enter total number of integers you want to: '))
for i in range(0,n):
    x=eval(input('Enter integer between 1 and 100: '))
    list1.append(x)
print('List is:',list1)
for i in range(0,len(list1)):
    a=list1.count(list1[i])
    print(list1[i], 'occurs',a,'times in list')











#7
list1=[int(i) for i in input("Enter numbers: ").split(' ')]
list2=[]
for i in list1:
    if i not in (list2):
        list2.append(i)
print("The distinct numbers are: ",list2)












#8
import random
count=[0]*10
randomInts=[random.randint(0,9) for i in range(1000)]
for num in randomInts:
    count[num]+=1
print('Number Data')
for i in range(10):
    print(str(i) + "s:", count[i])

















#9
list1=eval(input('Enter a list: '))
count=0
list2=[]+list1
list2.sort()
if (list2==list1):
    count=1
if (count):
    print("The list is Sorted")
else:
    print('The list is not sorted')



