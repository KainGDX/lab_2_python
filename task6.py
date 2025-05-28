# Открываем файл и читаем содержимое
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

import re

# Ищем все даты в формате DD.MM.YYYY
dates_dd_mm_yyyy = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

# Преобразуем даты в формат YYYY-MM-DD
dates_yyyy_mm_dd = [
    f"{d[6:10]}-{d[3:5]}-{d[0:2]}" for d in dates_dd_mm_yyyy
]

# Сортируем даты по возрастанию с помощью лямбда-функции
sorted_dates = sorted(dates_yyyy_mm_dd, key=lambda x: x)

# Сохраняем результат в файл
with open("dates.txt", "w", encoding="utf-8") as output_file:
    for date in sorted_dates:
        output_file.write(date + "\n")

# Выводим результат в консоль
print("Найденные и отсортированные даты (YYYY-MM-DD):")
for date in sorted_dates:
    print(date)