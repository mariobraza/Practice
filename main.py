check = 0
flag = False
for i in range(1, 11):

    money = int(input("Введи зарплату за " + str(i) + " месяц "))
    if check < money:
        check = money
    else:
        flag = True

if flag == False:
    print("Ваша зарплата упорядочена по возрастанию.")
else:
    print("Ваша зарплата НЕ упорядочена по возрастанию.")