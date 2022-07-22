x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y: '))
if x > y:
  print('Х больше Y')
if x == y:
  print('Х равен Y')
if x < y:
  print('Х меньше Y')

###################################

bank = int(input('Введите сумму на счете: '))
if bank >= 75000:
  bank -= 75000
  if bank < 5000:
    bank += 1000
    print('Сделана скидка')
  print('Курс успешно приобретён. На счету осталось', bank)
else:
  print('Не хватает денег на счёте')
print('Хорошего дня!')

###################################

money = int(input('Количество денег: '))
cheese = 60
icecream = 20
if money >= cheese:
  print('На сыр денег хватило')
  money -= cheese
  if money >= icecream:
    print('На мороженое тоже')
  else:
    print('Денег маловато')
else:
  print('Денег маловато')