number = int(input('Введите число: '))
summ = 0
while number != 0:
 summ += number
 number = int(input('Введите число: '))
print(summ)



password = int(input('Введите пароль: '))
while password != 235:
  print('Неверный пароль!')
  password = int(input('Попробуйте ещё раз: '))
print('Пароль верный! Добро пожаловать.')



donate = int(input('How much?: '))
summ = 0
summ += donate
while summ <= 500000:
  donate = int(input('How much?: '))
  summ += donate
print('Yeah boy, well done')