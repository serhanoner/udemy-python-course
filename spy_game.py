def spy_game(nums):

    searched_items = [0,0,7,'x']

    for num in nums:
        if num == searched_items[0]:
            searched_items.pop(0)
    
    return len(searched_items) == 1

print(spy_game([1,2,3,4,0,0,2,8,9]))
print()