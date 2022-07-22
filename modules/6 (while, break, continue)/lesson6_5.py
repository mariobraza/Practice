str_counts = int(input('Введите необходимое количество раз: '))
exit_str_counts = 0
while exit_str_counts < str_counts:
  print('Я — программист!')
  exit_str_counts += 1


###################################

timer = int(input('Cколько раз Вам напомнить?: '))
timer2 = 0
while timer2 < timer:
  print('Вы хотели не забыть о чём-то')
  timer2 += 1


###################################

bags = int(input('Введите количество мешков: '))
bags_count = 0
total_weight = 0
while bags_count < bags:
  bags_count += 1
  weight = int(input('Введите вес мешка: '))
  total_weight += weight
print('Сумарный вес мешков', total_weight, 'килограмм.')