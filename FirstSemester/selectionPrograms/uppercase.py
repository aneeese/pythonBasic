#random uppercase letter
import random
uppercase=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
letter=(random.choice(uppercase))
print(letter)
#OR
import random
num=random.randint(65,90)
print("The letter is",chr(num))
