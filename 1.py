pin = "4590"
while True:
    try_pin = input("Введите пин код")
    if try_pin == pin:
        print("Пароль верный")
        break
    else:
        print("Пароль не верный попробуйте еще раз")
