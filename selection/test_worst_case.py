import time

from src.selection_algorithm import selection_sort
from src.validations import validate_sorted_array

input_array = [x for x in range(10000, 0, -1)]

start = time.time()
selection_sort(input_array)
end = time.time()
print('Time: ', end - start)

if validate_sorted_array(input_array):
    print ("Sort OK")
else:
    print ("Failing Sort")
