#Создаём переменную для суммы
sum = 0

#Вводим числа и суммируем их
try:
    while True:
        try:
            number = float(input("Вводите число: "))
        except ValueError:
            print("Вы ввели не число")
            continue
        sum = sum + number
        if sum == int(sum):
            print("Сумма всех введеных чисел:", int(sum))
        else:
            print("Сумма всех введеных чисел:", sum)

#Выводим результат при нажатии клавиши прерывния
except KeyboardInterrupt:
    if sum == int(sum):
        print("\nВы нажали на клавишу прерывания. Сумма всех введеных чисел:", int(sum))
    else:
        print("\nВы нажали на клавишу прерывания. Сумма всех введеных чисел:", sum)