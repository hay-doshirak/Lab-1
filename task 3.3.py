year = int(input("Введите год: "))
if year>0 and year<=9999:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("Год", year, "- високосный.")
    else: print("Это год не високосный")
else: print("Ошибка ввода")
