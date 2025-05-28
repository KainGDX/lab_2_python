# task3_main.py

# Импортируем наш модуль
import task3_module

# Задаем числа для примера
x = 15
y = 5

# Выполняем операции и выводим результаты
print("Сложение:", task3_module.add(x, y))       # 20
print("Вычитание:", task3_module.subtract(x, y)) # 10
print("Умножение:", task3_module.multiply(x, y)) # 75
print("Деление:", task3_module.divide(x, y))     # 3.0

# Проверяем деление на ноль
y = 0
print("Деление на ноль:", task3_module.divide(x, y))