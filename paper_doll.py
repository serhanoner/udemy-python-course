def paper_doll(string):
    newstring = list(string)
    print(newstring)
    laststring = ""
    for word in newstring:
        word = word*3
        laststring +=  word 
    return laststring
print(paper_doll("Mississippi"))