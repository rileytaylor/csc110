# Allison Obourn and Janalee O'Bagy
# CSc 110, Spring 2017
# Lecture 22

# Blackbox testing program for function remove_bad_pairs(plist)

def main():
    # removing one pair
    test(1, [9, 2], [])
    # removing multiple pairs in a row
    test(2, [5, 3, 8, 1, 7, 0], [])
    # empty list
    test(3, [], [])
    # list of an odd size
    test(4, [10], [])
    # list containing an equal pair
    test(5, [2, 4, 8, 8], [2, 4, 8, 8])
    # containing negative numbers
    test(6, [-2, -3, 7, 8], [7, 8])


# Calls the tested function with the passed in list and
# prints a success message if the list is the expected
# passed in value. Otherwise prints a failure message
def test(num, list, expected):
    remove_bad_pairs(list)
    print("Test" + str(num)  + ": ", end="")
    if(list == expected):
        print("pass")
    else:
        print("fail: list should have been " + str(expected))


# Takes a list and removes adjacent pairs where the first of the pair
# is greater than the second
def remove_bad_pairs(pairs_list):
    if (len(pairs_list) % 2 != 0):  # remove the last element if length is odd
        pairs_list.pop()

    i = 0
    while (i < len(pairs_list)):
        if (pairs_list[i] > pairs_list[i+1]):
            pairs_list.pop(i+1)     # remove the second of the pair
            pairs_list.pop(i)       # remove the first of the pair
        else:
            i += 2


 

main()