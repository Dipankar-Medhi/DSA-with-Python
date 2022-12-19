def power(x, n):
    is_negative = False
    if n < 0:
        is_negative = True
        n *= -1

    result = recurse(x, n)

    if is_negative:
        return 1 / result

    return result


def recurse(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    temp = recurse(x, n // 2)

    if n % 2 == 0:
        return temp * temp

    else:
        return x * temp * temp


print("Power(0, 0) =", power(0, 0))
print("Power(2, 5) =", power(2, 5))
print("Power(3, 4) =", power(3, 4))
print("Power(1.5, 3) =", power(1.5, 3))
print("Power(2, -2) =", power(2, -2))
