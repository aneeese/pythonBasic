#4
numStudents=eval(input("Enter the number of students:"))
score1=eval(input("Enter the score of student1:"))
score2=eval(input("Enter the score of studnt2:"))
if score1>score2:
    highest=score1
    next_highest=score2
else:
    highest=score2
    next_highest=score1
for x in range(2,numStudents):
    score=int(input("Enter scores of students:"))
    if score>highest:
        next_highest=highest
        highest=score
    elif score>next_highest:
        next_highest=score
print("The highest score is",highest)
print("The next highest score is",next_highest)
