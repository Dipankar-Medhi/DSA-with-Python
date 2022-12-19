class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []
        phone_comb = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        self.recursion(phone_comb, digits, result, [], 0)
        return result

    def recursion(self, phone_comb, digits, result, track, index):
        if len(track) == len(digits):
            result.append("".join(track))

        if index < len(digits):
            for char in phone_comb[digits[index]]:
                track.append(char)
                self.recursion(phone_comb, digits, result, track, index + 1)
                track.remove(char)


print(Solution().letterCombinations("23"))
