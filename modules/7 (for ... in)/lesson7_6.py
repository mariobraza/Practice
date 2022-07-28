for number in 114, 12, 14, 10605, 4907, 450:
  if number % 2 == 0 and number % 3 != 0:
    print(number)
    print('Число подходит')
  else:
    print(number)
    print('Число не подходит')


#################### 2

even_numb = 0
for numbers in range(10):
    numb = int(input('Введите число: '))
    if numb % 2 == 0 and numb > 0:
      even_numb += 1
print(even_numb, ' чисел являются одновременно чётными и положительными')


#################### 3

summ_salary = 0
average_annual_salary = 0
for salary in range(1, 13):
  month_salary = int(input('Введите зарплату за месяц №' + str(salary) + ': '))
  summ_salary += month_salary
average_annual_salary = summ_salary / 12
print('Средняя годовая зарплата = ', average_annual_salary)

#################### 4

violations = 0
for sector in range(30, 36):
  number_of_people = int(input('Введите количество людей в секторе №' + str(sector) + ': '))
  if number_of_people > 10:
    violations += 1
    print('Нарушение! Слишком много людей в секторе!')
  else:
    print('Всё спокойно.')
print('Количество нарушений: ' + str(violations))

#################### 5

n = int(input('Введите число: '))
summ = 1
for factorial in range(1, n + 1):
  summ *= factorial
print('Факториал числа ' + str(n) + ' равен ' + str(summ))

#################### 6

excellent = 0
good = 0
satisfactory = 0
number_of_people = int(input('Введите количество человек в классе: '))
for evaluations in range(1, number_of_people + 1):
  score = int(input('Введите оценку ученика № ' + str(evaluations) + ' '))
  if score == 5:
    excellent += 1
  elif score == 4:
    good += 1
  else:
    satisfactory += 1
if excellent > good and excellent > satisfactory:
  print('Отличников больше')
elif good > excellent and good > satisfactory:
  print('Хорошистов больше')
else:
  print('Троечников больше')


#################### 7

start = int(input('Введите начало отрезка A: '))
stop = int(input('Введите конец отрезка B: '))
summ = 0
count = 0
for x in range(start, stop + 1):
  if x % 3 == 0:
    summ += x
    count += 1
average = int(summ / count)
print('среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.', average)

#################### 8

for x in range (100):
  if 0 < x // 10 < 10:
    y = x % 10
    z = x // 10
    w = y * z * 3
    if x == w:
      print('двузначные числа, которые равны утроенному произведению своих цифр', x)

#################### 9_1

prev_salary = 0
count_salary_increase = 0
summ_salary_increase = 0
count_salary_reduction = 0
summ_salary_reduction = 0
for month in range(1, 11):
  print(month)
  salary = int(input('Введите зарплату за этот месяц: '))
  if salary > prev_salary:
    count_salary_increase += 1
    summ_salary_increase += salary - prev_salary
    prev_salary = salary
  elif salary < prev_salary:
    count_salary_reduction += 1
    summ_salary_reduction += prev_salary - salary
    prev_salary = salary
salary_difference = summ_salary_increase - summ_salary_reduction
print('За 10 месяцев твоя зарплата: ')
print('Увеличивалась ',  count_salary_increase, 'раз')
print('На сумму ',  summ_salary_increase, 'рублей')
print('Уменьшилась ',  count_salary_reduction, 'раз')
print('На сумму ',  summ_salary_reduction, 'рублей')
print('Разница',  salary_difference, 'рублей')

#################### 9_2

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

#################### 10

n = int(input('Введите количество карточек: '))
summ_n = 0
for game in range(1, n + 1):
  summ_n += game
for numb in range(1, n):
  x = int(input('Введите номер оставшейся карточки: '))
  summ_n -= x
print ('Номер пропавшей карточки: ', summ_n)