import random  # импортируем модуль для генерации случайных чисел
# генерируем список из 25 случайных целых чисел от -50 до 50
random_numbers = [random.randint(-50, 50) for _ in range(25)] 
# инициализируем счетчики для положительных, отрицательных и нулевых чисел
positive_count = 0
negative_count = 0
zero_count = 0
# проходим по каждому числу в списке
for number in random_numbers:
    if number > 0:  # если число положительное
        positive_count += 1  # увеличиваем счетчик положительных
    elif number < 0:  # если число отрицательное
        negative_count += 1  # увеличиваем счетчик отрицательных
    else:  # если число равно нулю
        zero_count += 1  # увеличиваем счетчик нулей
# вычисляем общее количество чисел
total_count = len(random_numbers)  
# выводим результаты
print(f"Положительных: {positive_count} ({(positive_count / total_count) * 100:.2f}%)")  # количество и процент положительных
print(f"Отрицательных: {negative_count} ({(negative_count / total_count) * 100:.2f}%)")  # количество и процент отрицательных
print(f"Нулевых: {zero_count} ({(zero_count / total_count) * 100:.2f}%)")  # количество и процент нулей
# находим и выводим самое большое и самое маленькое значение
print(f"Самое большое значение: {max(random_numbers)}")  # максимальное число в списке
print(f"Самое маленькое значение: {min(random_numbers)}")  # минимальное число в списке
