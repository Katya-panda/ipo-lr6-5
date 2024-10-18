import random  # Импортируем модуль для генерации случайных чисел

# Генерируем список из 25 случайных целых чисел от -50 до 50
random_numbers = [random.randint(-50, 50) for _ in range(25)] 

# Инициализируем счетчики для положительных, отрицательных и нулевых чисел
positive_count = 0
negative_count = 0
zero_count = 0

# Проходим по каждому числу в списке
for number in random_numbers:
    if number > 0:  # Если число положительное
        positive_count += 1  # Увеличиваем счетчик положительных
    elif number < 0:  # Если число отрицательное
        negative_count += 1  # Увеличиваем счетчик отрицательных
    else:  # Если число равно нулю
        zero_count += 1  # Увеличиваем счетчик нулей

# Вычисляем общее количество чисел
total_count = len(random_numbers)  

# Выводим результаты
print(f"Положительных: {positive_count} ({(positive_count / total_count) * 100:.2f}%)")  # Количество и процент положительных
print(f"Отрицательных: {negative_count} ({(negative_count / total_count) * 100:.2f}%)")  # Количество и процент отрицательных
print(f"Нулевых: {zero_count} ({(zero_count / total_count) * 100:.2f}%)")  # Количество и процент нулей

# Находим и выводим самое большое и самое маленькое значение
print(f"Самое большое значение: {max(random_numbers)}")  # Максимальное число в списке
print(f"Самое маленькое значение: {min(random_numbers)}")  # Минимальное число в списке
