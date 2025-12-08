counter = 1
password = "admin"
while True:
    try_password = input("Введите пароль учитывая регистр ")
    if try_password == password:
        print("Пароль верный")
        break
    if counter > 2:
        print("Вход заблокирован")
        break
    counter += 1
