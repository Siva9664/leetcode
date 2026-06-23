class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if len(str(i))%2==0:
                l.append(i)
        return len(l)