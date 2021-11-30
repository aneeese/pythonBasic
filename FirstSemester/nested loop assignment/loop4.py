decimalValue=eval(input("Enter decimal Value: "))
hex = " "
while decimalValue != 0:
    hexValue = decimalValue % 16
    if 0<=hexValue<=9:
        hex=chr(hexValue+ ord('0'))+hex
    else:
        hex=chr(hexValue-10+ord('A'))+hex
    decimalValue = decimalValue // 16
print("\nHexadecimal value: ",hex)
