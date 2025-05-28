# task3_module.py

# Функция сложения
def add(a, b):
    return a + b

# Функция вычитания
def subtract(a, b):
    return a - b

# Функция умножения
def multiply(a, b):
    return a * b

# Функция деления с обработкой деления на ноль
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b