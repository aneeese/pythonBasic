#1
num_lines=eval(input("Enter the number of lines: "))
for i in range(1,num_lines+1):
    for j in range(num_lines,1, -1):
        if j<=i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    for j in range(1,num_lines+1):
        if j<=i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()







#2
num_lines=8
for i in range(num_lines):
    for j in range(7-i):
        if j==0:
            print(' ',end='')
        else:
            print('    ',end='')
    for j in range(7-i,8):
        if j==0:
            print(1, end='')
        else:
            print('{0:4d}'.format(2**(j-7+i)),end='')
    for j in range(8,8+i):
        print('{0:4d}'.format(2**(i-j+7)),end='')
    print()
