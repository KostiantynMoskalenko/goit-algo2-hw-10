import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

sizes = [10_000, 50_000, 100_000, 500_000]

randomized_time = []
deterministic_time = []

randomized_avg_time = []
deterministic_avg_time = []

for i in sizes:
    for j in range(5):
        arr = [random.randint(1, i) for _ in range(i)]
        start = time.time()
        random_sorted_arr = randomized_quick_sort(arr)
        end = time.time()
        randomized_time.append(end - start)
        start = time.time()
        deterministic_sorted_arr = deterministic_quick_sort(arr)
        end = time.time()
        deterministic_time.append(end - start)
    randomized_avg_time.append(sum(randomized_time) / len(randomized_time))
    deterministic_avg_time.append(sum(deterministic_time) / len(deterministic_time))

for i in range(len(sizes)):
    print(f'Розмір масиву:', sizes[i])
    print(f'    Рандомізований QuickSort:', randomized_avg_time[i])
    print(f'    Детермінований QuickSort:', deterministic_avg_time[i])

plt.title('Порівняння рандомізованого та детермінованого QuickSort')
plt.plot(sizes, randomized_avg_time, color='blue', label='Рандомізований QuickSort')
plt.plot(sizes, deterministic_avg_time, color='orange', label='Детермінований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.legend()
plt.show()

'''
CONCLUSION
According to the theoretical point of view when comparing deterministic and randomized algorithms, 
the randomized algorithms of QuickSorf function should be a bit faster. But it seems that it does not 
depend only on algorithms, but system too. I suppose that modern processors and systems are adapted 
for such "classic" sorting task. I reseived results that show that the deterministic algorithm is faster 
than randomized algorithm for QuickSort. The results were the same for both my local host and the
Google Colab. And the larger the set of inputs, the greater the difference between the results.
'''