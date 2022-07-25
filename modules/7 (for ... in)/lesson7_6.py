for number in 114, 12, 14, 10605, 4907, 450:
  if number % 2 == 0 and number % 3 != 0:
    print(number)
    print('Число подходит')
  else:
    print(number)
    print('Число не подходит')


####################

even_numb = 0
for numbers in range(10):
    numb = int(input('Введите число: '))
    if numb % 2 == 0 and numb > 0:
      even_numb += 1
print(even_numb, ' чисел являются одновременно чётными и положительными')


####################

month = 0
summ_salary = 0
average_annual_salary = 0
for salary in range(12):
  month += 1
  month_salary = int(input('Введите зарплату за месяц №' + str(month) + ': '))
  summ_salary += month_salary
average_annual_salary = summ_salary / 12
print('Средняя годовая зарплата = ', average_annual_salary)

####################

violations = 0
for sector in range(30, 36):
  number_of_people = int(input('Введите количество людей в секторе №' + str(sector) + ': '))
  if number_of_people > 10:
    violations += 1
    print('Нарушение! Слишком много людей в секторе!')
  else:
    print('Всё спокойно.')
print('Количество нарушений: ' + str(violations))

####################

n = int(input('Введите число: '))
summ = 1
for factorial in range(1, n + 1):
  summ *= factorial
print('Факториал числа ' + str(n) + ' равен ' + str(summ))

####################

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