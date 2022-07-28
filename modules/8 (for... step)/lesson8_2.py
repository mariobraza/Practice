n = int(input('Введите число: '))
for x in range(1, n // 2 + 1):
  z = (x * 2) ** 3
  print(z)

#############################

cell = 1
total_hours = int(input('Введите количество часов: '))
for hour in range(1, total_hours // 3 + 1):
  cell *= 2
  print('Прошло ', hour * 3, 'часов')
  print('Клеток: ', cell)
  print('Часов до конца эксперемента: ', total_hours - hour * 3)
  print()
print('Эксперемент окончен!')


##############################

n = int(input('Введите число: '))
for x in range(1, n + 1):
  if x % 2 == 1: 
    print(x ** 2)

####
n = int(input('Введите число: '))
number = 1
while number <= n:
  print(number, '** 2 =', number ** 2)
  number += 2

####

n = int(input('Введите число: '))
for x in range(1, n // 2 + n % 2 + 1):
  z = (x * 2 - 1) ** 2
  print(z)
