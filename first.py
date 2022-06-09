def myfunc1(*args):
    list = []
    for i in args:
        if i % 2 == 0:
            list.append(i)
        else:
            list = list
    return list
print(myfunc1(4,5,6,7,8))

