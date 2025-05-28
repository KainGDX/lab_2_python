# Задание 5: Лямбда-функции

nums = list(range(1, 21))

# Чётные
even = list(filter(lambda x: x % 2 == 0, nums))

# +10
plus_ten = list(map(lambda x: x + 10, even))

# Сортировка по убыванию
sorted_desc = sorted(plus_ten, reverse=True)

print("Результат:", sorted_desc)
