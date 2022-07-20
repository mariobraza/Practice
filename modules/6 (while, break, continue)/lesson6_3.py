temp = int(input('Сколько на улице градусов?: '))
meters = 0
while temp > 15:
  meters += 20
  temp -= 2
  if temp <= 15:
    break
  meters +=10
print(meters)


numb = int(input('Введите число: '))
summ = 0
while numb != 0:
  last_numb = numb % 10
  if last_numb == 5:
    print('Обнаружен разрыв')
    break
  summ += last_numb
  numb //=10
print(summ)


money = int(input('Введите количество денег: '))
while money < 10000:
  cube_numb = int(input('Введите число на кубике от 1 до 6: '))
  if cube_numb == 3:
    print('Вы проиграли всё!')
    money = 0
    break
    print('Вы всё проиграли!')
    print('Игра закончилась')
    print('Итого осталось: ', money, 'рублей.')
  money += 500
  print('Выйграли 500 рублей!')
print('Игра закончилась')
print('Итого осталось: ', money, 'рублей.')