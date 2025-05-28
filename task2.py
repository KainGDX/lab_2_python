# Задание 2: Обработка исключений

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
except ValueError:
    print("Ошибка: введите числа.")
else:
    print(f"Результат: {result}")
