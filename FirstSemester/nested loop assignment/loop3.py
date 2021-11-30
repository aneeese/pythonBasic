biggest_num_to_check=1000
num_of_primes_per_line=8
count=0
num=2
print("The prime numbers between 2 and 1000 are")
while num<=biggest_num_to_check:
    isPrime=True
    divisor=2
    while divisor<=num/2:
        if num%divisor==0:
            isPrime=False
            break
        divisor+=1
    if isPrime:
        count+=1
        print(format(num,"5d"), end = '')
        if count%num_of_primes_per_line==0:
            print()
    num+=1
