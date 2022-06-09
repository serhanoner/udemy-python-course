def blackjack(*args):
    sum = 0
    for number in args:
        sum += number
    print (sum)   
    if sum <= 21:
        return sum
    elif sum > 21:
        for i in args:
            if i == 11:
                return sum-10
            elif i !=11:
                return ("BUST")
    pass
print(blackjack(9,9,11))

# LAST CASE DIDNT WORK AND I CAN IMPROVE IT
# TO A REAL BLACKJACK GAME 