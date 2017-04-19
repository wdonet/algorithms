a_list = [6, 8, 12, 11, 15, 13, 20, 3, 10]
print 'ORIGINAL: %s' % a_list
swapped = True
step = 1
while swapped:
    swapped = False
    for i in range(1, len(a_list)):
        if a_list[i-1] > a_list[i]:
            temp = a_list[i]
            a_list[i] = a_list[i-1]
            a_list[i-1] = temp
            swapped = True
        print 'Step(%d,%d): %s' % (step, i, a_list)
    step+=1