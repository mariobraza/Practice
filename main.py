a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if a > b:
  max_num = a
else:
  max_num = b
if c > max_num:
  print(c)
else:
  print(max_num)