count = 11
while count <= 11:
  count -= 1
  if count == -1:
    print('Время вышло!')
    break
  else:
    print(count)




while True:
  question = int(input('продолжаем работу приложения? 1-ДА / 0-НЕТ: '))
  if question == 0:
    print('Приложение закрывается...')
    break


while True:
  print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
  password = input('Введите код: ')
  if password == '0550':
    print('Код верный, завершаю работу...')
    break