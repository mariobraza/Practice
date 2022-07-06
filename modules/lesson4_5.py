rain = int(input('На улице идет дождь?'))
if rain == 1:
  print('Пошёл дождь. Возьмите зонтик!')


exam_ruslang = int(input('Введите количество баллов по русскому языку: '))
exam_math = int(input('Введите количество баллов по математике: '))
exam_it = int(input('Введите количество баллов по математике: '))
enter = 270
summ = exam_ruslang + exam_math + exam_it
if summ >= enter:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошёл на бюджет.')


day = int(input('Какое сегодня число? '))
clear_day = day % 2
if clear_day == 0:
  print('Почисть зубы!')


chair1 = int(input('Введите стоимость стула №1: '))
chair2 = int(input('Введите стоимость стула №2: '))
chair3 = int(input('Введите стоимость стула №3: '))
summ = chair1 + chair2 + chair3
discount = summ / 100 * 90
if summ >= 10000:
  print('Сумма к оплате: ', discount)
else:
  print('Сумма к оплате: ', summ)


a = int(input())
if a < 0:
  a = -a
print(a)


casino = int(input('Число D6 первого игрока: '))
player = int(input('Число D6 второго игрока: '))
if casino <= player:
  print('Костя платит', player - casino, 'тысяч долларов!')
else:
  print('Владелец платит', player + casino, 'тысяч долларов!')


summ = int(input('Введите сумму, которую хотите снять: '))
acces = summ % 100
if acces == 0:
  print('Возьмите деньги!')
else:
  print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')


hours = int(input('Введите количество отработанных часов: '))
loan_balance = int(input('Введите остаток по кредиту: '))
food_money = int(input('Введите необходимое количество денег на еду: '))
expenses = loan_balance + food_money
salary = (200 * hours) / 2 ** 3 + hours
if salary >= expenses:
  print('Часов хватает. Можно отдохнуть!')
else:
  print('Часов не хватает. Придётся работать!')


probeg = int(input('трёхзначное число пробега: '))
day = int(input('число дня: '))
summ_day = probeg // 100 + probeg // 10 % 10 + probeg % 10
if summ_day > day:
  print('Сброс')
  probeg = 0
  print('Пробег:', probeg)
else:
  print('Сегодня не сломался')
  print('Пробег:', probeg)


a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if a > b > c:
  print(a)
if a > c > b:
  print(a)
if b > a > c:
  print(b)
if b > c > a:
  print(b)
if c > a > b:
  print(c)
if c > b > a:
  print(c)


a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if a > b:
  max_num = a
else:
  max_num = b
if c > max_num:
  print(c)
else:
  print(max_num)
