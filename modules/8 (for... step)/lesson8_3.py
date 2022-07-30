n = int(input('Введите число: '))
for numb in range(1, n, 2):
  print(n ** 3)

#############

n = int(input('Введите количество мест: '))
sit_sum = 0
for numb in range(1, n + 1, 5):
  print('Номер стула:', numb)
  sit_sum += numb
print('Сумма:', sit_sum)

###############

wake_up = int(input('Во сколько встал? '))
water = 0
summ_calories = 0
for hour in range(wake_up, 23, 3):
  water += 1
  print(hour, 'часов')
  calories = int(input('Сколько калорий наел? '))
  summ_calories += calories
print('Выпито', water, 'литров воды')
print('Съедено', summ_calories, 'калорий') 