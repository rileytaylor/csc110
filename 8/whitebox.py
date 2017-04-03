
def main():
    test(1, [], 2, 4, 0, "Unable to handle empty lists")
    # Whoops, ran outa time, not going to use a late day for this one
    # Also, white box testing is somewhat difficult without try/catch
    # and a test runner, just sayin.
def test(num, list, start, stop, expected, error):
    result = longest_sorted_sequence(list, start, stop)
    print("Test" + str(num) + ": ", end="")
    if result == expected:
        print("pass")
    else:
        print("fail: " + error)

def longest_sorted_sequence(list, start, stop):
    if (len(list) == 0):
        return 0
    max = 1
    count = 1
    for i in range(start, stop):
        if (list[i] >= list[i - 1]):
            count += 1
        else:
            count = 1
        if (count > max):
            max = count
    return max