n = int(input('Введите число: '))
count = 0
while count < n:
  count += 1
  print(count ** 3)

###################################

debtors_name = input('Введите имя должника: ')
debt_amount = int(input('Введите сумму долга: '))
deposited_money = 0
print(debtors_name + ', ваша задолженность составляет', debt_amount, 'рублей.')
while deposited_money < debt_amount:
  deposited_money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
  if deposited_money < debt_amount:
    print('Маловато,', debtors_name + '. Давайте ещё раз.')
print('Отлично,', debtors_name + '. Вы погасили долг. Спасибо!')

###################################


number = int(input('Введите число: '))
count = 0
if number == 0:
  print(1)
else:
  while number != 0:
    count += 1
    number //= 10
  print(count)

###################################

number_of_days = int(input('Введите количество дней: '))
even_months = 0
while number_of_days != 0:
  if number_of_days % 2 == 0:
    even_months += 1
  number_of_days = int(input('Введите количество дней: '))
print('Количество месяцев с четным количеством дней: ', even_months)


###################################

ticket_numb = int(input('Введите номер билета: '))
numb_1 = ticket_numb // 100000
numb_2 = ticket_numb // 10000 % 10
numb_3 = ticket_numb // 1000 % 10
numb_4 = ticket_numb // 100 % 10
numb_5 = ticket_numb // 10 % 10
numb_6 = ticket_numb % 10
if numb_1 + numb_2 + numb_3 == numb_4 + numb_5 + numb_6:
  print('У Вас счастливый билет!')
else:
  print('У Вас обычный билет!')


###################################

numb = int(input('Введите число: '))
positive_numb = 0
negative_numb = 0
while numb != 0:
  if numb > 0:
    positive_numb += 1
  else:
    negative_numb += 1
  numb = int(input('Введите число: '))
print('Кол-во положительных чисел: ', positive_numb)
print('Кол-во отрицательных чисел: ', negative_numb)


###################################

working_hours = 0
sum_tasks = 0
sum_call = 0
while working_hours < 8:
  working_hours += 1
  print(working_hours, '- й час')
  numb_tasks = int(input('Сколько задач решит Максим? '))
  sum_tasks += numb_tasks
  wife_call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
  if wife_call == 1:
    sum_call += 1
print('Рабочий день закончился. Всего выполнено задач:', sum_tasks)
if sum_call > 0:
  print('Нужно зайти в магазин.')


###################################

#без капитализации
deposit = int(input('Введите сумму вклада: '))
percent = int(input('Введите процентную ставку: '))
target = int(input('Введите желаемую сумму накопления: '))
summ = (target - deposit) // (deposit * percent // 100)
print(summ)

#с капитализацией
deposit = int(input('Введите сумму вклада: '))
percent = int(input('Введите процентную ставку: '))
target = int(input('Введите желаемую сумму накопления: '))
year = 0
while deposit <= target:
  deposit += deposit * percent // 100
  year += 1
if 10 <= year % 100 <= 20:
  pr_year = "лет"
elif year % 10 == 1:
  pr_year = "год"
elif 1 < year % 10 <= 4:
  pr_year = "года"
elif (5 <= year % 10) or (year % 10 <= 9) or (year % 10 == 0):
  pr_year = "лет"
print(year, pr_year, "пройдет прежде, чем ты сможеш забрать сумму в размере", target, "рублей")

###################################


son = 0
count = 0
while son != 7:
  son = int(input('Какое чиcло я загадал? от 1 до 10: '))
  count += 1
  if son < 7:
    print('Число меньше, чем нужно. Попробуйте ещё раз!')
  elif son > 7:
    print('Число больше, чем нужно. Попробуйте ещё раз!')
  else:
    print('Вы угадали! Число попыток: ', count)


###################################

x = 0
a = 1
b = 100
while x != 1:
  y = a + (b - a) // 2
  print(y)
  x = int(input('Твоё число равно(1), больше(2) или меньше(3), чем число?'))
  if x == 1:
    break
  elif x == 2:
    a = (b + a) // 2 + 1
  else:
    b = (b + a) // 2 - 1
print('Загадал число: ', y)