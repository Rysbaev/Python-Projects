print("Hello Dear Guest,This is Your Task Manager! ")
tasks = []
while True:
    print("1) Enter Your Task! ")
    print("2) Show All Your Tasks! ")
    print("3) End Your Task! ")
    option = int(input("Choose your option: "))

    if option == 1:
        task = input("Add Your task: ")
        name = input("Name of your task: ")
        date = input("Date of your task: ")
        tasks.append(task)

    if option == 2:
        for i in tasks:
         print(f"{i}")

    if option == 3:
        idx = int(input("Enter index of your task: "))
        del tasks[idx]
