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
    print('У Сеньора Динара сумма всех итераций меньше, чем у Джуна Марата на',
          all_count_Marat - all_count_Dinar)
elif all_count_Dinar > all_count_Marat:
    print('У Джуна Марата сумма всех итераций меньше на',
          all_count_Dinar - all_count_Marat)
else:
    print('Количество итераций равно, идите оба спать')

#################################


x = 0
a = 1
b = 100
all_count_Dinar = 0
summ_count = 0
count = 0
while x <= 100:
  x += 1
  all_count_Dinar += summ_count
  a = 1
  b = 100
  count = 0
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
  a = 1
  b = 100
  count = 0
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

#############################


def bin_search_Dinar(search_num):
    left_num = 1
    right_num = 100
    count = 0
    while True:
        formula = (left_num + right_num) // 2
        if formula == search_num:
            return count
        elif search_num < formula:
            right_num = formula - 1
        else:
            left_num = formula + 1
        count += 1


#######################


LEFT_NUM = 1
RIGHT_NUM = 100


def bin_search_Dinar(search_num):
    left_num = LEFT_NUM
    right_num = RIGHT_NUM
    count = 0
    while True:
        formula = (left_num + right_num) // 2
        if formula == search_num:
            return count
        elif search_num < formula:
            right_num = formula - 1
        else:
            left_num = formula + 1
        count += 1


def bin_search_Marat(search_num):
    left_num = LEFT_NUM
    right_num = RIGHT_NUM
    count = 0
    while True:
        formula = (left_num + right_num) // 2
        if formula == search_num:
            return count
        elif search_num < formula:
            right_num = formula
        else:
            left_num = formula + 1
        count += 1


all_count_Marat = 0
all_count_Dinar = 0
for i in list(range(LEFT_NUM, RIGHT_NUM + 1)):
    all_count_Dinar += bin_search_Dinar(i)
    all_count_Marat += bin_search_Marat(i)

if all_count_Dinar < all_count_Marat:
    print('У Сеньора Динара сумма всех итераций меньше, чем у Джуна Марата на',
          all_count_Marat - all_count_Dinar)
elif all_count_Dinar > all_count_Marat:
    print('У Джуна Марата сумма всех итераций меньше на',
          all_count_Dinar - all_count_Marat)
else:
    print('Количество итераций равно, идите оба спать')