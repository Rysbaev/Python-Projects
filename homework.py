name = input("Введите ваше имя: ")
age = input("Введите свой возраст: ")
time = input("Сколько месяцев вы занимаетесь программмированием?: ")

if time.lower() >= "1" in time:
    print("Вы Junior курса Python!")

if time.lower() == "3" in time:
    print("Вы Middle Python Developer!")

if time.lower() <= "5" in time:
    print("Вы Senior Python Developer!")
    name = input()
    age = input()
    email = input()
    print(name.title(), age, email)




