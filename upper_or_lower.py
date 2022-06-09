def up_low(s):
    uppers = 0
    lowers = 0
    for word in s:
        if word.isupper():
            uppers += 1
        elif word.islower():
            lowers += 1
        else:
            pass
    print(f"Original string is {s}")
    print(f'number of uppers is {uppers}')
    print(f'number of lowers is {lowers}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))