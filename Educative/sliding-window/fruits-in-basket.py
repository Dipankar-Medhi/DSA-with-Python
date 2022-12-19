
def fruitsIntoBusket(fruits):
    start = 0
    max_len = 0
    basket = {}

    for end in range(len(fruits)):
        right_fruit = fruits[end]

        if right_fruit not in basket:
            basket[right_fruit] = 0
        basket[right_fruit] += 1

        # shring window till we left 2 fruits in basket
        while len(basket) > 2:
            left_fruit = fruits[start]

            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            # move window forward
            start += 1

        max_len = max(max_len, end - start + 1)
    return max_len


print(fruitsIntoBusket(['A', 'B', 'C', 'B', 'B', 'C']))
