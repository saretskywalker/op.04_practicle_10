number_1 = int(input("Введите первое число "))


while True:
    number_2 = int(input("Введите второе число"))
    if number_2 > number_1:
        break
    else:
        print("Введите число большее", number_1)
while True:
    number_3 = int(input("Введите третье число"))
    if number_3 > number_2:
        break
    else:
        print("Введите число большее", number_2)
print("Последовательность принята")
