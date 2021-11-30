import time
t = eval(input("Enter the time in seconds: "))
for i in range(1,t+1):
    print(t," seconds remaining ")
    time.sleep(1)
    t-=1
print('\nSTOPPED')
