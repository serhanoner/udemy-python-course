

def makes_twenty(x,y):
    if x == 20:
        return True
    elif y == 20:
        return True
    elif x+y == 20:
        return True
    else:
        return False
print(makes_twenty(20,13123))