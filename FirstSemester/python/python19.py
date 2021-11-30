invest_value=eval(input("Enter investment amount:"))
interest_rate=eval(input("Enter annual interest rate:"))
num_years=eval(input("Enter number of years:"))
monthlyInterestRate=interest_rate/1200
numofMonths=num_years*12
futureInvestmentValue=(invest_value*(1+monthlyInterestRate)**(numofMonths))
print("Future Investment Value is",futureInvestmentValue)
