x = int(input("Введи количество мальчиков: "))
y = int(input("Введи количество девочек: "))
boys = "B"
girls = "G"
stop = 0
if x > y:
    stop = x
elif x < y:
    stop = y
elif x == y:
    stop = (x + y) // 2
b_and_g_common = ""
flag = True

#если разница девочек от парней больше чем на 4, то решение не верное
for i in range(1, stop + 1):
    if x - y >= 5 or y - x >= 5:
        print("Ответ: Нет решения")
        flag = False
        break

    # получается как исключение если мальчиков или девочек > 7 и разница между ними >= 4, то их рассадить нельзя.
    elif (x == 5 and y == 2) or (x == 2 and y == 5) or \
            (x == 7 and y == 3) or (x == 3 and y == 7) or \
            (x == 6 and y == 2) or (x == 2 and y == 6):
        print("Ответ: Нет решения")
        flag = False
        break

    # если количество девочек == мальчиков то сажает через 1
    if x == y:
        y -= 1
        x -= 1
        b_and_g_common += boys + girls
        flag = False
        continue
    break


# ================================================================================================================

if flag:
    for i in range(1, stop + 1):

        if 0 < y < x:
            b_and_g_common += boys
            x -= 1
            b_and_g_common += girls
            y -= 1
            b_and_g_common += boys
            x -= 1
            continue
        elif 0 < x < y:
            b_and_g_common += girls
            y -= 1
            b_and_g_common += boys
            x -= 1
            b_and_g_common += girls
            y -= 1
            continue
        if y == 0 and 1 == x:
            b_and_g_common += boys
            x -= 1
            break
        elif x == 0 and 1 == y:
            b_and_g_common += girls
            y -= 1
            break
        elif x == 0 and y == 0:
            break
        elif x == y:
            y -= 1
            x -= 1
            b_and_g_common += boys + girls



print(b_and_g_common)