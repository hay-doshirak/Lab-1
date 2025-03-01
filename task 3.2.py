nk=[i for i in range(1,36,2)]
vk=[i for i in range(2,37,2)]
nb=[i for i in range(37,54,2)]
vb=[i for i in range(38,55,2)]

n=int(input("Ведите номер места (1-55):"))

if n in nk:
    print("Ваше место - нижнее в купе.")

elif n in vk:
    print("Ваше место - верхнее в купе.")

elif n in nb:
    print("Ваше место - нижнее боковое.")

elif n in vb:
    print("Ваше место - верхнее боковое.")

else:print("Ошибка при вводе номера места.")
