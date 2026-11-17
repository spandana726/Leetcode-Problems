class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = (n*(n+1))//2
        sumk = 0
        for i in range(0,n):
            sumk+=nums[i]
        return ans-sumk

        