colors = ["красный", "желтый", "синий"]
print("Основные цвета доступные для смешивания -", '; '.join(colors))

color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color1.lower() in colors and color2.lower() in colors:
    newcolor = color1.lower() + color2.lower()

    match newcolor:
        case "красныйсиний"|"синийкрасный":
            print("Полученный цвет - фиолетовый.")

        case "красныйжелтый" | "желтыйкрасный":
            print("Полученный цвет - оранжевый.")

        case "желтыйыйсиний" | "синийжелтый":
            print("Полученный цвет - зеленый.")

        case "красныйкрасный" | "синийсиний"| "желтыйжелтый":
            print("Получен исходный цвет - ", color1)

else: print("Ошибка при вводе цветов.")