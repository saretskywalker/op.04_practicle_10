product = 1
while True:
    number = int(input("Введите число "))
    
    if number > 0:
        product *= number
    if number < 0:
        break
print (product)
