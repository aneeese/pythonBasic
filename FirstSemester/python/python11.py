f=eval(input("final account value:"))
ai=eval(input("annual interest rate in percent:"))
y=eval(input("enter number of years:"))
mit=ai/1200
nom=y*12
initialDepositAmmount=f/(1+mit)**nom
print("Initial Deposit Value is",initialDepositAmmount)
