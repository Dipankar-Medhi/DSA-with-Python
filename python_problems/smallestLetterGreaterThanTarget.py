

# return of start using binary search gives the answer

# def ceilingOfNumber(arr, target):

#     ans = ceilingbinarySearch(arr, target)  # return the start
#     return arr[ans]


# # return index of smallest number > = target
# def ceilingbinarySearch(arr, target):

#     start = 0
#     end = len(arr) - 1

#     # what if the target element is greater than greatest element in arr

#     while (start <= end):
#         # find the middle element // mid = (start + end) / 2
#         mid = int(start + (end - start)/2)

#         if (target < arr[mid]):             # search on the 1st half
#             end = mid - 1

#         else:
#             start = mid + 1

#     return start % len(arr)


from typing import List


# print(ceilingOfNumber(arr, target))


class Solution:
    def __init__(self, letters, target):
        self.letters = letters
        self.target = target

    def nextGreatestLetter(self):

        self.start = 0
        self.end = len(self.letters) - 1

        while (self.start <= self.end):
            # find the middle element // mid = (start + end) / 2
            self.mid = int(self.start + (self.end - self.start)/2)

            # search on the 1st half
            if (self.target < self.letters[self.mid]):
                self.end = self.mid - 1

            else:
                self.start = self.mid + 1

        return self.letters[self.start % len(self.letters)]


letter = Solution(["c", "f", "j"],  "e")
print(letter.nextGreatestLetter())
