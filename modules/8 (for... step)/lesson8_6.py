buckwheat = 100
month = 0
for remains in range(buckwheat, 0, -4):
  month += 1
  print('Месяц:', month)
  buckwheat -= 4
  print('Осталось', buckwheat, 'килограмм гречки')

######################## 2

number_of_debtors = int(input('Введите количество должников: '))
amount_of_debts = 0
for score in range(0, number_of_debtors, 5):
  print('Должник с номером', score)
  question_of_debt = int(input('Сколько должны? '))
  amount_of_debts += question_of_debt
print('Общая сумма долга:', amount_of_debts)

######################## 3

reverse_timer = int(input('Введите количество секунд: '))
question = 0
for time in range(reverse_timer, -1, -1):
  if time == 0:
    print('Ваша еда готова, осторожно горячo!')
    break
  print('Осталось:', time, 'секунд')
  question = int(input('Готовы забрать еду? (1)ДА  (0)НЕТ: '))
  if question == 1:
    print('Ваша еда готова, можете забрать, прошло', time, 'секунд')
    break

######################## 4

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
summ_arith = 0
count_arith = 0
for arithmetic_mean in range(a, b + 1, c):
  summ_arith += arithmetic_mean
  count_arith += 1
print('Cреднее арифметическое всех чисел из отрезка от', a, 'до', b, 'кратных числу', c)
print(int(summ_arith / count_arith))

######################## 5

a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
c = int(input('Введите шаг: '))
for x in range(b, a - 1, c):
  y = x ** 3 + 2 * x ** 2 - 4 * x + 1
  print('В точке', x, 'функция равна', y)

######################## 6

envelope_square_side = 12
count = 0
letter = int(input('Введите размер письма: '))
while letter > envelope_square_side:
  letter /= 2
  count += 1
print(count, 'раз нужно сложить письмо пополам, чтобы оно поместилось в конверт.')

######################## 7


educational_grant = int(input('Введите ежемесячную стипендию: '))
living_expenses = int(input('Введите расходы на проживание: '))
summ_expenses = 0
for month in range(1, 11):
  print(living_expenses)
  if month != 1:
    living_expenses = living_expenses * 3 / 100 + living_expenses
  summ_expenses += living_expenses
print('У родителей необходимо попросить', summ_expenses - educational_grant * 10)

######################## 8

n = int(input('Введите число: '))
summ = 0
for x in range(0, n + 1):
  summ += (-1) ** n * 1 / 2 ** n
print(summ)

######################## 9

x = int(input("Введите число x: "))
numerator_summ = 1
denominator_summ = 1

for i in range(1, 7):
    numb_top = (x - (2 ** i - 1))
    numerator_summ *= numb_top
    numb_bottom = (x - (2 ** i))
    denominator_summ *= numb_bottom
total = numerator_summ / denominator_summ
print(total)

######################## 10

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