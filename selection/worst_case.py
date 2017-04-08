import time

from src.selection_algorithm import selection_sort

input_array = [x for x in range(10000, 0, -1)]

start = time.time()
selection_sort(input_array)
end = time.time()
print('Time: ', end - start)
