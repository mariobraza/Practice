x = 0
a = 1
b = 100
all_count_Dinar = 0
summ_count = 0
count = 0
while x <= 100:
  x += 1
  all_count_Dinar += summ_count
  while a != b:
      count += 1
      if x == a + (b - a) // 2:
        summ_count += count
        break
      elif x > a + (b - a) // 2:
        a = (b + a) // 2 + 1
      else:
        b = (b + a) // 2 - 1
x = 0
a = 1
b = 100
all_count_Marat = 0
summ_count = 0
count = 0
while x <= 100:
  x += 1
  all_count_Marat += summ_count
  while a != b:
      count += 1
      if x == a + (b - a) // 2:
        summ_count += count
        break
      elif x > a + (b - a) // 2:
        a = (b + a) // 2 + 1
      else:
        b = a + (b - a) // 2
if all_count_Dinar < all_count_Marat:
  print('У Сеньора Динара сумма всех итераций меньше, чем у Джуна Марата на', all_count_Marat - all_count_Dinar)
elif all_count_Dinar > all_count_Marat:
  print('У Джуна Марата сумма всех итераций меньше на', all_count_Dinar - all_count_Marat)
else:
  print('Количество итераций равно, идите оба спать')