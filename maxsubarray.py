class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currsum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            currsum=max(nums[i],nums[i]+currsum)
            maxsum=max(maxsum,currsum)
        return maxsum
