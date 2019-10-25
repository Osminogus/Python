# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    previous_num = None
    for num in nums:
        if previous_num == num:
            previous_num = num
            return True
        else:
            previous_num = num
            continue
    return False


# Check
print(has_33([1, 3, 3]))

# Check
print(has_33([1, 3, 1, 3]))

# Check
print(has_33([3, 1, 3]))