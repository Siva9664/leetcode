class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        has_x = False

        while n > 9:
            if n % 10 == x:
                has_x = True

            n //= 10

        return has_x and n != x