f = open('user.txt', 'w')
a = input('Введите логин: ')
b = input('Введите пароль: ')
f.write(f'Ваш логин {a} \nВаш пароль {b}')
f.close()



