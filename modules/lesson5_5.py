exp = int(input('Введите опыт: '))
if exp < 1000:
  print('Ваш уровень: 1')
elif exp < 2500:
  print('Ваш уровень: 2')
elif exp < 5000:
  print('Ваш уровень: 3')
else:
  print('Ваш уровень: 4')


a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if c < a > b:
    print(a)
elif c < b > a:
    print(b)
else:
    print(c)




x = int(input('Enter X: '))
if x > 0:
  y = x - 12
elif x == 0:
  y = 5
else:
  y = x ** 2
print('Y is:', y)







place = int(input('Введите место в списке поступающих:'))
if place <= 10:
  number_of_points = int(input('Введите количество баллов:'))
  print('Поздравляем, вы поступили!')
  if number_of_points >= 290:
    print('Бонусом вам будет начисляться стипендия.')
  else:
    print('Но вам не хватило баллов для стипендии.')
else:
    print('К сожалению, вы не поступили.')





rating = int(input('Что получил по математике? '))
if rating < 4:
 print('Плохо. Марш учиться!')
elif rating < 6:
 print('Молодец! Можешь отдохнуть.')



numb = int(input('Введите число: '))
answer = numb / 10
if (10 > answer >= 1) or (-1 >= answer > -10):
  print('Двухзначное')
else:
  print('Не двухначное')





x = int(input('1: '))
y = int(input('2: '))
z = int(input('3: '))
if x == y == z:
  print('3 совпадения')
elif x == y != z or x != y == z or x == z !=y:
  print('2 совпадения')
else:
  print ('Нет совпадений')




area = int(input('Введите площадь квартиры: '))
cost = int(input('Введите стоимость квартиры: '))
if area >= 100 and cost <= 10000000 or area >= 80 and cost <= 7000000:
  print('Квартира подходит!')
else:
  print('Квартира НЕ подходит!')




profit = int(input('Введите сумму прибыли: '))
if profit < 0:
  print('Ошибка: доход не может быть отрицательным')
else:
  if profit < 10000:
    tax13 = profit * 13 / 100
    print('Ставка налога (13%): ', tax13)
  elif profit < 50000:
    tax20 = ((profit-10000) * 20 / 100) + (10000 * 13 / 100) 
    print('Ставка налога (20%): ', tax20)
  else:
    tax30 = ((profit-50000) * 30 / 100) + (40000 * 20 / 100) + (10000 * 13 / 100) 
    print('Ставка налога (30%): ', tax30)    

time = int(input('Введите текущее время в формате ЧЧ: '))
if (time >= 8 and time < 10) or (time >= 12 and time < 14) or (time >= 15) and (time < 18) or (time >= 20 and time < 22):
  print('Можно получить посылку')
else:
  print('Посылку получить нельзя')