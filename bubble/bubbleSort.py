#a_list = [6, 8, 12, 11, 15, 13, 20, 3, 10]
a_list = [5, 1, 4, 2, 8]
print 'ORIGINAL: %s\n' % a_list
swapped = True
step = 1
while swapped:
    swapped = False
    for i in range(1, len(a_list)):
        info = ''
        if a_list[i-1] > a_list[i]:
            info = '< swap(%d,%d)' % (a_list[i-1], a_list[i])
            temp = a_list[i]
            a_list[i] = a_list[i-1]
            a_list[i-1] = temp
            swapped = True
        print 'Step(%d,%d): %s %s ' % (step, i, a_list, info)
    print '\n'
    step+=1