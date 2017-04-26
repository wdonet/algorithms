# =======================================================================
#  Author: Antonio Hernandez
#  Title: Mergesort
#  Package: algorithms
# =======================================================================


def merge_sort(array):
    print 'Working with: %s' % array
    if len(array) >= 2:
        middle = len(array) / 2
        left = array[:middle]
        right = array[middle:]
        print 'left: %s' % left
        print 'right: %s' % right
        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)


def merge(left, right, array):
    print 'Merge %s and %s' % (left, right)
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1