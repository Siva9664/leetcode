class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res  = []
        for i in range(len(nums)):
            c = 0
            for j in nums:
                if j < nums[i]:
                    c+=1
            res.append(c)

        return res