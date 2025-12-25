final_cost = 0
while True:
    cost = int(input("Введите цену товара"))
    if cost == 0:
        break
    elif cost < 0:
        print("ошибка цены")
        continue
    else:
        final_cost += cost
if final_cost > 1000:
    final_cost -= final_cost * 0.1
print("Итоговая сумма покупок составляет: ", final_cost)

