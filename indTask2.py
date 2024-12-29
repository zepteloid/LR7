from functools import reduce

# Ввод списка вещественных элементов
A = list(map(float, input("Введите вещественные элементы списка через пробел: ").split()))

# 1. Сумма отрицательных элементов
negative_sum = sum(x for x in A if x < 0)
print(f"Сумма отрицательных элементов: {negative_sum}")

# 2. Произведение элементов между максимальным и минимальным элементами
max_index = A.index(max(A))
min_index = A.index(min(A))

# Определяем границы между максимальным и минимальным
start, end = sorted([max_index, min_index])

# Вычисляем произведение элементов между ними
if end - start > 1:  # Проверяем, есть ли элементы между max и min
    product = reduce(lambda x, y: x * y, A[start + 1:end])
else:
    product = 0  # Если между max и min нет элементов
print(f"Произведение элементов между максимальным и минимальным: {product}")

# 3. Упорядочивание элементов списка по возрастанию
A.sort()
print(f"Упорядоченный список: {A}")
