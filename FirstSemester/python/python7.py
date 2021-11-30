minutes=eval(input("enter the minutes:"))
years=minutes/525600
r=round(years)
remaining_minutes=minutes%525600
days=remaining_minutes/1440
d=round(days)
print(minutes,"minutes is approximately",r,"and",d,"days")           
