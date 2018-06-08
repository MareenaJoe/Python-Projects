def sorting_numbers_list_ascend(lst):
    for passnum in range(0,len(lst)-1):
        for i in range(passnum):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

lst = [54,26,93,17,77,31,44,55,20]

sorting_numbers_list_ascend(lst)
print (lst)


