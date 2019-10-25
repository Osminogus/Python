#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even,
# but returns the greater if one or both numbers are odd
    # lesser_of_two_evens(2,4) --> 2
    # lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens2(a,b):
        if (a>b) and (a%2 == 0 and b%2 == 0) or (a % 2 != 0 or b % 2 != 0):
            return b
        elif (a<b and a%2 == 0 and b%2 == 0) or (a>b and (a%2 !=0 or b%2 !=0)):
            return a




# Check
print(lesser_of_two_evens(2,4))

# Check
print(lesser_of_two_evens(2,5))