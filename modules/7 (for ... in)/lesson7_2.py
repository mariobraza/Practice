for meters in 100, 90, 95, 87, 102:
 if meters % 3 == 0:
   print(meters, 'Подходит')
 else:
   print(meters, 'Не подходит')

###################################

for numbers in 3, 7, 5, 6, 4:
  print(numbers ** 2, numbers ** 3, numbers ** 4)

###################################

winners = 0
for tickets in 345, 19, 87, 1020, 421:
  if tickets % 5 == 0 and 0 < tickets // 100 < 10:
    print(tickets, 'Выйгрышный билет')
    winners += 1
print('Всего победителей: ', winners)