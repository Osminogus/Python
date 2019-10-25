# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    i=0
    for item in nums:
        if item ==0 and i<=2:
            i += 1
        elif i ==2 and item == 7:
            return True
    return False

# Check
print (spy_game([1,2,4,0,0,7,5]))

# Check
print (spy_game([1,0,2,4,0,5,7]))

# Check
print (spy_game([1,7,2,0,4,5,0]))