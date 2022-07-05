client = 'Петя'
pet = 'Кот'
print(client + ' и ' + pet)

r, g, b = 'Red', 'Green', 'Blue'
print(r, b, g, r + g + b, b, g + b)

first_animal, second_animal = input('Enter the first animal: '), input('Enter the second animal: ')
print('The ' + first_animal + ' is sleeping, the ' + second_animal + ' is walking')

first_name = input('Введите имя пользователя: ')
greeting = 'Привет, '
print(greeting, first_name)
print("К сожалению, у Вас нет доступа к системе.")
print("Пожалуйста, обратитесь к системному администратору.")

departure_city = input('Enter the departure city: ')
arrival_city = input('Enter the arrival city: ')
print(departure_city + ' - ' + arrival_city)

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
a, b = b, a
print(a, b)

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
city = input('Введите город проживания: ')
print('==========')
print('Вас зовут ' + name + ' ' + surname)
print('Вы живете в городе ' + city)

#C:/user/docs/folder/new_file.txt
user = input('Введите пользователя: ')
new_file = input('Введите имя файла: ')
print('C:/' + user + '/docs/folder/' + new_file + '.txt')