for n in range(1,10001):
    sum1 = 0
    for i in range(1, n):
       if(n % i == 0):
           sum1 = sum1 + i
    if (sum1 == n):
        print("\nThe Perfect number :",n)
