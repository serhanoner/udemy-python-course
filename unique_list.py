def unique_list(lst):
    uniquelist = []
    for number in lst:
        if number not in uniquelist:
            uniquelist.append(number)
    return uniquelist
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
def unique_list_2(lst):
    return list(set(lst))
print(unique_list_2([1,1,1,1,2,2,3,3,3,3,4,5]))
