
def insertion_sort(a_list):
    print 'ORIGINAL = %s' % a_list

    for index in range(1, len(a_list)):
        j = index - 1
        pivot = a_list[index]

        print '\nPivot : %d ' % pivot
        while j >= 0 and a_list[j] > pivot:
            print '%d ->' % a_list[j]
            a_list[j + 1] = a_list[j]
            j = j - 1
        a_list[j + 1] = pivot

        print a_list

    print 'RESULT %s' % a_list
    return a_list
