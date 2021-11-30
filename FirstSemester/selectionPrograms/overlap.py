#rectangle overlap program
x1,y1,w1,h1=eval(input("Enter r1's center x-cordinates,y-coordinates,width, and height: "))
x2,y2,w2,h2=eval(input("Enter r2's center x-cordinates,y-coordinates,width, and height: "))
if (x1+w1/2>=x2+w2/2>=x1-w1/2)and(x1+w1/2>=x2-w2/2>=x1-w1/2)and(y1+h1/2>=y2+h2/2>=y2+h2/2>=y1-h1/2)and(y1+h1/2>=y2+h2/2>=y1-h1/2):
    print("r2 is inside r1")
elif (x1+w1/2>=x2+w2/2>=x1-w1/2)or(x1+w1/2>=x2-w2/2>=x1-w1/2)or(y1+h1/2>=y2+h2/2>=y2+h2/2>=y1-h1/2)or(y1+h1/2>=y2+h2/2>=y1-h1/2):
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
