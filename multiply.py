def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
print(multiply([1,2,3,-4]))
