deposit = int(input('Введите сумму вклада: '))
percent = int(input('Введите процентную ставку: '))
target = int(input('Введите желаемую сумму накопления: '))
year = 0
while deposit < target:
  deposit += deposit * percent // 100
  year += 1
print(year)