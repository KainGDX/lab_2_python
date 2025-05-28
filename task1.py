# Задание 1: Работа с файлами

import random

# Запись 10 случайных чисел в файл
with open("data.txt", "w") as f:
    for _ in range(10):
        f.write(f"{random.randint(1, 100)}\n")

# Чтение чисел
with open("data.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]

# Расчёты
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Запись результата
with open("result.txt", "w") as f:
    f.write(f"Сумма: {total}\n")
    f.write(f"Среднее: {average}\n")
    f.write(f"Максимум: {maximum}\n")
    f.write(f"Минимум: {minimum}\n")

print("Готово. Смотри result.txt")
