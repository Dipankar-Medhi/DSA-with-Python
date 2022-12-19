epsilon = 0.000000000000001


def square_root(num):
    low = 0.0

    # square root can never be more than
    # half of number except if number is <= 1
    # so square root of any number always lie
    # between 0 and 1 + (num / 2)
    high = 1.0 + num / 2.0

    # binary search
    while low < high:
        mid = low + (high - low) // 2
        sqr = mid**2

        diff = abs(num - sqr)

        if diff <= epsilon:
            return mid

        if sqr < num:
            low = mid + 1.0
        else:
            high = mid - 1.0

    return -1


List = [16, 17, 2.25]
for i in List:
    print("Suare root of", i, "is", square_root(i))
