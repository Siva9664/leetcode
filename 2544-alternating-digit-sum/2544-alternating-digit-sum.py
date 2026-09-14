class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        total = 0

        for i in range(len(digits)):
            if i % 2 == 0:
                total += int(digits[i])
            else:
                total -= int(digits[i])

        return total