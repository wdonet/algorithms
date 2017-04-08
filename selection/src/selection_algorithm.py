
def selection_sort(input_list):
    for i in range(len(input_list) - 1):
        positionOfMin = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[positionOfMin]:
                positionOfMin = j

        if positionOfMin != i:
            temp = input_list[i]
            input_list[i] = input_list[positionOfMin]
            input_list[positionOfMin] = temp

    return input_list;






