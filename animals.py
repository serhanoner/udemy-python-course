def animal_crackers(string):
    x = string.split()
    x1 = x[0]
    x2 = x[1]
    if x1[0] == x2[0]:
        return True
    else:
        return False

print(animal_crackers('adasdasd asdadad'))
print(animal_crackers('Crazy Kangaroo'))

# PROBLEM IS, GENERALIZING THIS CODE FOR MULTIPLE WORDS