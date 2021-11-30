#Zeller's congruence
y=eval(input("Enter a year(e.g. 2008): "))
m=eval(input("Enter a month(1 to 12): "))
q=eval(input("Enter the day of month(1 to 31): "))
if m<3:
    m=m+12
    y=y-1
century=y//100
century_year=y%100
h=(q+((26*(m+1))//(10))+century_year+((century_year)//(4))+((century)//(4))+(5*(century)))%7
if h==0:
    print("Day of the week is Saturday")
elif h==1:
    print("Day of the week is Sunday")
elif h==2:
    print("Day of the week is Monday")
elif h==3:
    print("Day of the week is Tuesday")
elif h==4:
    print("Day of the week is Wednesday")
elif h==5:
    print("Day of the week is Thursday")
elif h==6:
    print("Day of the week is Friday")
