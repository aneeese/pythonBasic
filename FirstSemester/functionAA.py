#Q1
def Addition(search):
    student = ['Awais','Hanan','Ammar','Sohaib','Anees']
    student.append(search)
    return student
def checking(search):
    student = ['Awais','Hanan','Ammar','Sohaib','Anees']
    if search in student:
        return True
    else:
        return False
def deleting(search):
    student = ['Awais','Hanan','Ammar','Sohaib','Anees']
    student.remove(search)
    return student
def main():
    print("Enter 1 to check if student is in list or not")
    print("Enter 2 delete the student name from a list")
    print("Enter 3 to add name of student in the list")
    choice = eval(input("Enter your choice: "))
    search = input("Enter the name of student: ")
    if choice == 1:
        print("Entered name is", checking(search))
    if choice == 2:
        print(deleting(search))
    if choice == 3:
        print(Addition(search))
main()
    



#Q2
def Order(sorted_list):
    s1 = [34,23,64,76,12]
    for i in range(len(s1)):
        minimum = min(s1)
        sorted_list.append(minimum)
        s1.remove(minimum)
    return sorted_list
def main():
    sorted_list = []
    print(Order(sorted_list))
main()
