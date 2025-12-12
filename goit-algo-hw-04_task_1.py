import random
import timeit


# ---------- Алгоритми сортування ----------
def insertion_sort(arr):
    a = arr[:]  # робимо копію, щоб не змінювати початковий масив
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def timsort(arr):
    return sorted(arr)  # вбудований алгоритм Python (Timsort)


# ---------- Генерація тестових даних ----------
def random_array(n):
    return [random.randint(0, 100000) for _ in range(n)]


def nearly_sorted_array(n):
    arr = list(range(n))
    for _ in range(n // 20):  # трохи порушуємо порядок
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# ---------- Вимірювання часу ----------

def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data), number=1)


# ---------- Основний експеримент ----------
sizes = [1000, 5000, 10000]

algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Timsort (sorted)": timsort
}

for size in sizes:
    print(f"\nРозмір масиву: {size}")

    data_random = random_array(size)
    data_near = nearly_sorted_array(size)

    print("  Випадковий масив:")
    for name, func in algorithms.items():
        t = measure_time(func, data_random)
        print(f"    {name}: {t:.4f} сек")

    print("  Майже відсортований масив:")
    for name, func in algorithms.items():
        t = measure_time(func, data_near)
        print(f"    {name}: {t:.4f} сек")
