def even_and_odd_in_list(lst):
    even = []
    odd = []
    for i in range(0,len(st)-1):
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)

lst = [2,4,3,7,9,15,23]
print (even_and_odd_in_list(lst))
