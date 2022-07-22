year_of_release = int(input('Введите год выпуска: '))
gears_count = int(input('Введите количество скоростей: '))
if year_of_release >= 2018 and gears_count >= 24:
  print('Велосипед подходит')
else:
  print('Велосипед не подходит')

###################################

score = int(input('Введите количество баллов: '))
medal = int(input('Ведите наличие медали: '))
if score >= 280 and medal == 1:
  print('Поздравляем! Ты поступил!')
else:
  print('К сожалению, ты не прошёл в наш университет.')

###################################

temp = int(input('Введите температуру: '))
if temp < 0 or temp > 100:
  print('Опасность!')