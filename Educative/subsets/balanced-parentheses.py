## iterative solution
from collections import deque


# def balanced_parentheses(num):
#     result = []
#     queue = deque()
#     queue.append(ParenthesesString("", 0, 0))

#     while queue:
#         ps = queue.popleft()
#         if ps.openCount == num and ps.closeCount == num:
#             result.append(ps.str)
#         else:
#             if ps.openCount < num:
#                 queue.append(
#                     ParenthesesString(ps.str + "(", ps.openCount + 1, ps.closeCount)
#                 )
#             if ps.openCount > ps.closeCount:
#                 queue.append(
#                     ParenthesesString(ps.str + ")", ps.openCount, ps.closeCount + 1)
#                 )

#     return result


## recursive solutions
def generate_valid_parentheses(num):
    result = []
    parenthesesString = [0 for x in range(2 * num)]

    recursion(num, 0, 0, parenthesesString, 0, result)
    return result


def recursion(num, openCount, closeCount, parenthesesString, index, result):
    if openCount == num and closeCount == num:
        result.append("".join(parenthesesString))
    else:
        if openCount < num:  # can add open pare
            parenthesesString[index] = "("
            recursion(
                num, openCount + 1, closeCount, parenthesesString, index + 1, result
            )

        if openCount > closeCount:  # add close )
            parenthesesString[index] = ")"
            recursion(
                num, openCount, closeCount + 1, parenthesesString, index + 1, result
            )


print(generate_valid_parentheses(3))
