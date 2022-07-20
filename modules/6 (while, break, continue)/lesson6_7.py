n = int(input('Введите число: '))
count = 0
while count < n:
  count += 1
  print(count ** 3)



debtors_name = input('Введите имя должника: ')
debt_amount = int(input('Введите сумму долга: '))
deposited_money = 0
print(debtors_name + ', ваша задолженность составляет', debt_amount, 'рублей.')
while deposited_money < debt_amount:
  deposited_money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
  if deposited_money < debt_amount:
    print('Маловато,', debtors_name + '. Давайте ещё раз.')
print('Отлично,', debtors_name + '. Вы погасили долг. Спасибо!')




number = int(input('Введите число: '))
count = 0
if number == 0:
  print(1)
else:
  while number != 0:
    count += 1
    number //= 10
  print(count)


even_months = 0
while True:
  number_of_days = int(input('Введите количество дней: '))
  if number_of_days == 0:
    print('Количество месяцев с четным количеством дней: ', even_months)
    break
  even_check = number_of_days % 2
  if even_check == 0:
    even_months += 1