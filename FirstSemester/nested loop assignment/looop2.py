count=0
for x in range(ord("!"),ord("~")+1):
    count+=1
    if count%10==0:
        print(x)
    else:
        print(x,end=" ")

