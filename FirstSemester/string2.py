#displays valid password if the rules are followed or invalid password otherwise.
pas=input("Enter atleast 8 characters password which shuold be mixup of characters and numbers: ")
p=len(pas)
x=pas.isalpha()
y=pas.isdigit()
if p>=8 and x==False and y==False:
    print("Valid Password")
else:
    print("Invalid Password")










#number of letters in a string. 
num=str(input("Enter a string: "))
count=len(num)
print(count)








#whether the first string is a substring of the second string.
s1=input("Enter string: ")
s2=input("Enter string: ")
s3=s2.find(s1)
print(s3)








#enter a string and then prints the reverse of it.
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("Enter a string: ")
print('The original string is: ',end='')
print(s)
print('The reversed string is: ',end='')
print(reverse(s))








#Binary to decimal

def reverseString(str1):
    return str1[::-1]
def binaryToDecimal(binaryString):
    reversed_bin_num = reverseString(binaryString)
    dec_num=0
    digit=0
    for num in reversed_bin_num:
        dec_num+=int(num)*2**digit
        digit+=1
    return dec_num
def main():
    bin_string=input("Enter a binary number: ")
    print("Decimal representation: ", binaryToDecimal(bin_string))
main()









#binary to hexadecimal
def binaryToHex(binaryString):
    bin_nums=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    hex_nums=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while len(binaryString)%4!=0:
        binaryString='0'+binaryString
    hex_value=''
    for i in range(0,len(binaryString),4):
        seq=binaryString[i:i+4]
        for bins in bin_nums:
            if seq==bins:
                ind=bin_nums.index(bins)
                hex_value+=hex_nums[ind]
    return hex_value
def main():
    bin_string=input("Enter a binary number: ")
    print('Hexadecimal represenation: ',binaryToHex(bin_string))
