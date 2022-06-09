def summer_69(array):
    sum = 0
    for number in array:
        if number == 6 and 9 in range(len(array)-array[number]):
            sum += number
    return(sum)

print(summer_69(array=(1,2,3,4,5,6,7,8,9)))