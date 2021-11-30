n1=eval(input("Enter an integer: "))
n2=eval(input("Enter an integer: "))
d=min(n1,n2)
while d>=1:
    if n1%d==0 and n2%d==0:
        print("The Greatest Common Factor of",n1,"and",n2,"is",d)
        break
    d-=1
