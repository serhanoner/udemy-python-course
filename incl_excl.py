def ran_check(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False
print(ran_check(5,2,7))