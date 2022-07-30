n = int(input('Количество секунд: '))
for go in range(n, 0, -1):
  print(go)
print('Я иду искать!')

#####################

sum_soldiers = int(input('Количество солдат: '))
sum_rules = int(input('Количество правил  в уставе: '))
sum_pushups = 0
for check in range(sum_soldiers - 3, 0, -4):
  print(check)
  answer_rules = int(input('Солдат, сколько правил в уставе?'))
  if answer_rules != sum_rules:
    print('Неверный ответ', check * 10, 'отжиманий!')
    sum_pushups += check * 10
print('Сумма отжиманий:', sum_pushups)

#####################

n = int(input('Количество секунд: '))
for go in range(n, 0, -2):
  print(go)
print('Я иду искать!')