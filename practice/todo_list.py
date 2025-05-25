tasks = ["clean your room","study","a"]
def view():
    print(tasks)
def add(element):
    tasks.append(element)
    print("✅ added")
def remove(element):
    tasks.remove(element)
    print("✅ removed")
def done(element):
    tasks.remove(element)
    print("✅ marked as done")
def my_sort():
    tasks.sort()
    print(tasks)
def reverse():
    print(tasks[::-1])

while True:
    choise = input("choose: (view/add/remove/mark as done/sort/reverse/break)").lower()
    if choise == "view":
        view()
    elif choise == "add":
        element = input("type here: ").lower()
        add(element)
    elif choise == "remove":
        element = input("type here: ").lower()
        if element not in tasks:
            print("ENTER A VALID TASK")
        else:
            remove(element)
    elif choise == "mark as done":
        element = input("type here: ").lower()
        if element not in tasks:
            print("ENTER A VALID TASK")
        else:
            done(element)
    elif choise == "sort":
        my_sort()
    elif choise == "reverse":
        reverse()
    elif choise == "break":
        break
    else:
        print("❌ Invalid choise")