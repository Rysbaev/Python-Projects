class Study:


    def __init__(self,name , age, month):
        self.name = name
        self.age = age
        self.month = month

    def how_many_month_you_study(self):
        return f"{self.name} {self.age} {self.month}"

while True:
    print("1) Your Name ")
    print("2) Your age")
    print("3) Month you've been studying Python")
    option = int(input("Choose your option: "))

    if option == 1:
        name = input("What is your name ? ")
        age = input("How old are you? ")
        month = input("How many month you complete Python lessons? ")


    if option == 2:
        age = input("How old are you? ")

    if option == 3:
        month = input("How many month you complete Python lessons? ")

    if  month >= "1" in month:
            print("You are Junior Python developer!")

    if  month == "3" in month:
            print("You are Middle Python developer!")

    if  month <= "5" in month:
            print("You are Senior Python developer!")