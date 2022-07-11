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