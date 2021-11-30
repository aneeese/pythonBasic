#Deck Cards
import random
suit=random.randint(1,4)
if suit==1:
    suit="Clubs"
elif suit==2:
    suit="Diamonds"
elif suit==3:
    suit="Hearts"
elif suit==4:
    suit="Spades"
rank=random.randint(1,13)
if rank==1:
    rank="Ace"
elif rank==2:
    rank="2"
elif rank==3:
    rank="3"
elif rank==4:
    rank="4"
elif rank==5:
    rank="5"
elif rank==6:
    rank="6"
elif rank==7:
    rank="7"
elif rank==8:
    rank="8"
elif rank==9:
    rank="9"
elif rank==10:
    rank="10"
elif rank==11:
    rank="Jack"
elif rank==12:
    rank="Queen"
elif rank==13:
    rank="King"
print("The card you picked is "+rank+" of "+suit)
