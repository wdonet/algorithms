import time
from random import randint

from src.selection_algorithm import selection_sort
from src.validations import validate_sorted_array

input_array = [randint(0,10000) for _ in range(10000)]

start = time.time()
selection_sort(input_array)
end = time.time()
print('Time: ', end - start)

if validate_sorted_array(input_array):
    print ("Sort OK")
else:
    print ("Failing Sort ")