x=1
total=0
while x<=100000:
   total=total+ ((-1)**(x+1))/((2*x)-1)
   x+=1
   for i in range(10000,100001,10000):
       if(x==i):
           print("Value of pi for i= "+str(x)+ " is "+ str(4*total))
