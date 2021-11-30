#flipped coin display
guess=str(input("Guess whether its Heads or Tail:"))
import random
coin=("Heads","Tail")
Toss=(random.choice(coin))
if guess==Toss:
    print("Your guess is Correct")
elif guess!=Toss:
    print("Your guess is incorrect. Please Try Again")
else:
    print("Invalid Input")
