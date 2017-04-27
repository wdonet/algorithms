from common.swap import swap


def choose_pivot(input_list, left, right):
    return input_list[(left + right) // 2]
#    return input_list[right]
#    return input_list[left]


def quick_sort(input_list, left=None, right=None):
    if left is None or right is None:
        left = 0
        right = len(input_list) - 1

    if right - left < 1:
        return

    i = left
    j = right
    pivot = choose_pivot(input_list, left, right)

    while i <= j:
        while input_list[i] < pivot:
            i += 1
        while input_list[j] > pivot:
            j -= 1
        if i <= j:
            swap(input_list, i, j)
            i += 1
            j -= 1

    if left < j:
        quick_sort(input_list, left, j)
    if i < right:
        quick_sort(input_list, i, right)


def quick_sort_2(input_list, left=None, right=None):
    if left is None or right is None:
        left = 0
        right = len(input_list)

    if right - left < 1:
        return

    pivot = (left + right) // 2
    p_index = left
    print('I: ', input_list, ',left:', left, ',right:', right, ',p_index:', p_index, 'pivot:',
          input_list[pivot])
    for i in range(left, right):
        if input_list[i] < input_list[pivot]:
            if i != p_index:
                swap(input_list, i, p_index)
            if p_index == pivot:
                pivot = i
            p_index += 1
        print('S: ', input_list, ',left:', left, ',right:', right, ',p_index:', p_index, 'pivot:',
              input_list[pivot])

    if input_list[p_index] > input_list[pivot]:
        swap(input_list, p_index, pivot)

    print('O: ', input_list, ',left:', left, ',right:', right, ',p_index:', p_index, 'pivot:',
          input_list[pivot])

    if p_index > left:
        quick_sort_2(input_list, left, p_index)
    if right > p_index:
        quick_sort_2(input_list, p_index + 1, right)


def quick_sort_non_recursive(input_list):

    stack_indexes = [{"left": 0, "right": len(input_list) - 1}]

    while len(stack_indexes) > 0:
        index = stack_indexes.pop()
        i = left = index['left']
        j = right = index['right']

        pivot = choose_pivot(input_list, left, right)

        while i <= j:
            while input_list[i] < pivot:
                i += 1
            while input_list[j] > pivot:
                j -= 1
            if i <= j:
                swap(input_list, i, j)
                i += 1
                j -= 1

        if left < j:
            stack_indexes.append({"left": left, "right": j})
        if i < right:
            stack_indexes.append({"left": i, "right": right})
