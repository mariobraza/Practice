numb = int(input('Введите число: '))
summ = 0
while numb != 0:
  last_numb = numb % 10
  if last_numb == 5:
    print('Обнаружен разрыв')
    break
  summ += last_numb
  numb //= 10
print(summ)