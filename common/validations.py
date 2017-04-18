

def validate_sorted_array(input_array):
    for i in range(len(input_array) - 1):
        if input_array[i] > input_array[i + 1]:
            return False

    return True
