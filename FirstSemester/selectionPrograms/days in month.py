#enter month and year and display the number of days in the month
month=eval(input("Enter the month: "))
year=eval(input("Enter the year: "))
if month==1:
    print("January",year,"has 31 days")
elif month==2:
    leap=year%4
    if leap==0:
        print("Feburary",year,"has 29 days")
    else:
        print("Feburary",year,"has 28 days")
elif month==3:
    print("March",year,"has 31 days")
elif month==4:
    print("April",year,"has 30 days")
elif month==5:
    print("May",year,"has 31 days")
elif month==6:
    print("June",year,"has 30 days")
elif month==7:
    print("July",year,"has 31 days")
elif month==8:
    print("August",year,"has 31 days")
elif month==9:
    print("September",year,"has 30 days")
elif month==10:
    print("October",year,"has 31 days")
elif month==11:
    print("November",year,"has 30 days")
elif month==12:
    print("December",year,"has 31 days")
else:
    print("The number you entered doesn't represent any Month")
