for x in range(1, 11):
  print(x ** 3)

#######################

start = int(input('Введите первое число: '))
stop = int(input('Введите второе число: '))
summ = 0

for numb in range(start, stop + 1):
  summ += numb

print('Сумма чисел от', start, 'до ', stop, 'равна ', summ)

#######################

wake_hour = int(input('Во сколько встал?: '))
summ_calories = 0
cheerful_hours = 0

for hour in range(wake_hour, 23):
  print('Сейчас', hour, 'часов')
  cheerful_hours += 1
  calories = int(input('Сколько съел калорий в этом часу?: '))
  summ_calories += calories
  if summ_calories >= 2000:
    break
  
print('Всего съедено калорий', summ_calories, 'и', cheerful_hours, 'часов был бодрым.')