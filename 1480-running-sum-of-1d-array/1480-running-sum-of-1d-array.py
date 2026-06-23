class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = [0]*(len(nums))
        for i in range(len(nums)):
            temp[i] = nums[i]+temp[i-1]
        
        return temp