
while True:

    action = input('1 - Войти \n2 - Зарегистрироваться\n')

    with open('database.txt', 'a') as f: 
        users = {'bektur': 123, 'bekzat': 1234}
        f.writelines(users)

    with open('database.txt', 'r') as f:
        f.read()
        log_user = input('введите логин: ')
        
        if log_user in f.read():
            log_pass = input('введите логин: ')

            if log_user in f.read() and loh_pass in f.read():
                
                print('Вход выполнен')

            else:
                print('Неверный логин или пароль')
        else:
            print('Такого пользователя не существует\n Для регистрации нажмите 2')



    



