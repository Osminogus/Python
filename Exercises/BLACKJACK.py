# #### BLACKJACK: Given three integers between 1 and 11,
# if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally,
# if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

def blackjack(a, b, c):
    summa = sum([a, b, c])
    if summa <= 21:
        return summa
    elif summa > 21 and (a == 11 or b == 11 or c == 11):
        return summa - 10
    else:
        return "BUST"


# Check
print(blackjack(5, 6, 7))

# Check
print(blackjack(9, 9, 9))

# Check
print(blackjack(9, 9, 11))
