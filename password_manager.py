master_password = "stilljk"
input_password = input("Enter your password: ")
#adding
def add():
    website = input("Enter your website: ")
    user_name = input("Enter user name: ")
    password = input("Enter password: ")
    with open("pass_store.txt","a") as file :
        details = file.write(f"{website}     {user_name}     {password}")
        file.write("\n")
    return details     
#viewing
def view():
    with open("pass_store.txt","r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            print(f"{i} {lines[i]}")
#removing
def remove():
    view()
    select = int(input("Enter the index to remove: "))
    with open("pass_store.txt","r") as file:
        lines = file.readlines()
        if select in range(len(lines)):
            del lines[select]
            with open("pass_store.txt","w") as file:
                file.writelines(lines)
            print("successful ✅")    
        else:
            print("invalid index")       
while True:
    if input_password != master_password:
        print("Invalid password,Who are you 😠")
        break
    else:
        print("Welcome to the password manager 😊\n")
        change = input("Do you want to make any changes (y/n): ").lower()
        if change != 'y':
            print("Thanks for visiting 😊")
            break
        else:
            choose = input("(a/r/v): ")
            if choose == 'a':
                add()
                continue
            elif choose == 'v':
                view()
                continue
            elif choose == 'r':
                remove()
            else:
                print("Invalid choise!!")