def has_33(array):
    for number in range(len(array)-1):
        if array[number] == 3:
            if array[number+1] == 3:
                return True
            else:
                return False
    pass
print(has_33([1, 3, 3]))