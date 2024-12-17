import random
from itertools import combinations
# Создание списка случайных чисел от -10 до 10 размером 20 элементов
random_list = [random.randint(-10, 10) for _ in range(20)]
print("Список случайных чисел:", random_list)
# Создание всех возможных комбинаций по 4 элемента
combinations_list = list(combinations(random_list, 4))
# Удаление дубликатов комбинаций (порядок не учитывается) и создание списка уникальных комбинаций
unique_combinations = []
for comb in combinations_list:
    sorted_comb = tuple(sorted(comb))
    if sorted_comb not in unique_combinations:
        unique_combinations.append(sorted_comb)
print("Уникальные комбинации из 4 элементов:")
for comb in unique_combinations:
    print(comb)
# Запрос целого числа у пользователя
while True:
    try:
        user_value = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
# Подсчёт количества пар, чья сумма меньше заданного пользователем значения
pair_count = 0
for i in range(len(random_list)):
    for j in range(i + 1, len(random_list)):
        if random_list[i] + random_list[j] < user_value:
            pair_count += 1
print(f"Количество пар, чья сумма меньше {user_value}: {pair_count}")