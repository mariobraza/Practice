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