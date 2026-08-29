class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        i = 0
        ans = 0
        count = 0
        for j in range(0,n):
            if left<=nums[j]<=right:
                count=j-i+1
            if nums[j]>right:
                count = 0
                i = j+1
            ans+=count
        return ans
        



        