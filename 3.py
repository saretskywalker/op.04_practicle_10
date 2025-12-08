previous_number = -99999999
while True:
    number = int(input("Ввелите число "))
    if number > previous_number and number != 0:
        previous_number = number
    if number == 0:
        break
print("Самое большое число в последовательности", number)
