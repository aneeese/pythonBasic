#conversion of dollar and RMB
import random
rate=eval(input("Enter the exchange rate from dollar to RMB: "))
choice=eval(input("Enter 0 to convert dollars to RMB and 1 for vice versa: "))
if choice==0:
    amountD=eval(input("Enter the Dollars amount: "))
    exchange=(amountD*rate)
    amou=str(amountD)
    exe=str(exchange)
    print("$"+amou+" is "+exe+"Yuan")
else:
    amountR=eval(input("Enter amount in RMB: "))
    rateR=1/rate
    exchange=amountR*rateR
    r=round(exchange,2)
    amou=str(amountR)
    exe=str(r)
    print(amou+"Yuan is $"+exe)
