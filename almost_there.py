def almost_there(number):
    if number in range(89,111):
        return True
    elif number in range (189,211):
        return True
    else:
        return False
print(almost_there(209))