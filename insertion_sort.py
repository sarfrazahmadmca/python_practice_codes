def insertion_sort(alist):
    for index in range(1, len(alist)):
        curr_value = alist[index]
        position = index

        while position > 0 and alist[position-1] > curr_value:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = curr_value
    return alist


print insertion_sort([54,26,93,17,77,31,44,55,20])