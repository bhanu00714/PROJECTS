students = {"Rohan":90,"Bhanu":100,"Fathima":80}

# Example Functions
def add_student(name, marks):
    students[name] = marks
def update_marks(name, new_marks):
    students[name] = new_marks
def delete_student(name):
    del students[name]
def display_all():
    print(students)
def show_topper_and_average():
    top_marks = max(students.values())
    top_students = []
    for name,marks in students.items():
        if top_marks == marks:
            top_students.append(name)
    print("Topper/Toppers:",top_students,"Marks =",top_marks)
    average = sum(students.values())/len(students.values())
    print("Average marks =",average)
# Then write a menu to call these functions based on user input
while True:
    print("WELCOME")
    print("type * to exit")
    choise = input(" 1.Add a student \n 2.update marks \n 3.delete a student \n 4.display the list \n 5.Display the topper and the average marks")
    if choise == "1":
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        add_student(name,marks)
    elif choise == "2":
        name = input("Enter name: ")
        new_marks = float(input("Enter marks: "))
        update_marks(name,new_marks)
    elif choise == "3":
        name = input("Enter name: ")
        delete_student(name)
    elif choise == "4":
        display_all()
    elif choise == "5":
        show_topper_and_average()
    elif choise == "*":
        print("Thank you")
        break
    else:
        print("Invalid choise")
