class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 1

        for i in range(n):
            day = i % 7
            total += monday + day

            if day == 6:
                monday += 1

        return total