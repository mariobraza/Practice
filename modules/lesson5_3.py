x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y: '))
if x > y:
  print('Х больше Y')
elif x == y:
  print('Х равен Y')
else:
  print('Х меньше Y')



profit = int(input('Введите сумму прибыли: '))
if profit < 0:
  print('Ошибка: доход не может быть отрицательным')
else:
  if profit < 10000:
    tax = profit * 13 / 100
    print('Ставка налога (13%): ', tax)
  elif profit < 50000:
    tax = profit * 20 / 100
    print('Ставка налога (20%): ', tax)
  else:
    tax = profit * 30 / 100
    print('Ставка налога (30%): ', tax)      