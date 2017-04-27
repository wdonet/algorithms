def swap(input_array, first_index, second_index):
    temp = input_array[first_index]
    input_array[first_index] = input_array[second_index]
    input_array[second_index] = temp