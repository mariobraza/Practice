a = 8
b = 10
c = 12
d = 18
res = ((-3 + a ** 2) * b - 2 ** 3)/(c - 2 * d)
print(res)

a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
d = int(input('Четвертое число: '))
q1q2, q3q4 = a + b, c + d
res = q1q2 / q3q4
print(res)

numb = int(input('Введите число: '))
next_res = numb + 1
prev_res = numb - 1
print('После числа', numb, 'идёт число', next_res)
print('До числа', numb, 'идёт число', prev_res)

a = int(input('Введите длину катета А:'))
b = int(input('Введите длину катета В:'))
s = (a * b) / 2
print('Площадь треугольника равна ', s)

minutes = int(input('Введите количество минут: '))
res_h = minutes // 60
res_m = minutes % 60
print(minutes, 'минут это ', res_h, 'часов', res_m, 'минут')

numb1 = 111
numb2 = 904
res = numb1 % 100 + numb2 % 100
print(res)

v = 58
t = 2
s = v * t % 115
print(s)

a = int(input('4zch: '))
print(a // 1000, a // 100 % 10, a % 100 // 10, a % 10)

a = int(input('4zch: '))
print(a % 10, a % 100 // 10, a // 100 % 10, a // 1000)

a = int(input('4zch: '))
print(a % 10 * 1000 + a % 100 // 10 * 100 + a // 100 % 10 * 10 + a // 1000)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a, b = a + b - a, b + a - b
print(a, b)