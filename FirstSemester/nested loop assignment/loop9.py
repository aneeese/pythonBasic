salary=5000
sales_amount=0
while salary<30000:
    sales_amount+=0.01
    if sales_amount<=5000:
        salary+=0.08*0.01
    elif sales_amount<=10000:
        salary+=0.10*0.01
    else:
        salary+=0.12*0.01
print("To earn $30,000, you need to generate $" + format(sales_amount, "0,.2f")
