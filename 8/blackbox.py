def main():
    # Remove 1 duplicate
    test(1, [3, 3], [3])
    # remove multiple duplicates
    test(2, [3, 3, 4, 4], [3, 4])
    # empty list
    test(3, [], [])
    # list with a triplet
    test(4, [4, 4, 4, 5], [4, 5])
    # list of no duplicates
    test(5, [1, 2, 3], [1, 2, 3])
    # list with strings
    test(6, ["1", "2", "5", "no", "3!"], ["1", "2", "5", "no", "3!"])


def test(num, list, expected):
    remove_consecutive_duplicates(list)
    print("Test" + str(num) + ": ", end="")
    if list == expected:
        print("pass")
    else:
        print("fail: list should have been " + str(expected))


# def remove_consecutive_duplicates(list):
#     stuff...

main()
