
def selection_sort(input_list):
    for i in range(len(input_list) - 1):
        position_of_min = i

        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[position_of_min]:
                position_of_min = j

        if position_of_min != i:
            temp = input_list[i]
            input_list[i] = input_list[position_of_min]
            input_list[position_of_min] = temp

    return input_list;






