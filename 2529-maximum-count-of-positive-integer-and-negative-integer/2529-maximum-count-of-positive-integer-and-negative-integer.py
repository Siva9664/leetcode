class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c1 = sum(1 for i in nums if i < 0)
        c2 = sum(1 for i in nums if i > 0)
        return max(c1,c2)