# =======================================================================
#  Author: Oswaldo Herrera (@wdonet)
#  Title: Heapsort
#  Package: algorithms
# =======================================================================


def heap_sort(a_list):
    print 'ORIGINAL:'
    print a_list

    print '\nCREATING HEAP:'
    the_heap = []
    for element in a_list:
        add_to_heap(the_heap, element)

    print '\n SORTING HEAP:'

    for last in range(len(the_heap) - 1, 0, -1):
        swap(the_heap, 0, last)
        print ('swap', the_heap, last)
        fix_heap_down(the_heap, 0, last)

    print '\nRESULT:'
    print the_heap
    return the_heap


def add_to_heap(source, element):
    source.append(element)
    fix_heap_up(source, len(source) - 1)


def fix_heap_up(heap, target_index):
    offset = 1 if target_index % 2 > 0 else 2
    parent_index = (target_index - offset) / 2
    if parent_index >= 0\
            and heap[parent_index] < heap[target_index]:
        swap(heap, parent_index, target_index)
        print heap
        fix_heap_up(heap, parent_index)


def fix_heap_down(heap, parent_index, last_index):
    left_child = left(heap, parent_index)
    if left_child is not None:
        right_child = right(heap, parent_index) if get_child_right_index(parent_index) < last_index else None
        is_left_grater = left_child > right_child
        child_index = 2 * parent_index + (1 if is_left_grater else 2)
        if child_index < last_index and heap[parent_index] < heap[child_index]:
            swap(heap, parent_index, child_index)
            print ('fix-', heap, last_index)
            fix_heap_down(heap, child_index, last_index)


def left(a_list, parent_index):
    return get_child(a_list, get_child_left_index(parent_index))


def get_child_left_index(parent):
    return 2 * parent + 1


def right(a_list, parent_index):
    return get_child(a_list, get_child_right_index(parent_index))


def get_child_right_index(parent):
    return 2 * parent + 2


def get_child(a_list, calculated_index):
    if calculated_index < len(a_list):
        return a_list[calculated_index]
    else:
        return None


def swap(a_list, source, target):
    length = len(a_list)
    if source < length and target < length:
        temporal = a_list[target]
        a_list[target] = a_list[source]
        a_list[source] = temporal