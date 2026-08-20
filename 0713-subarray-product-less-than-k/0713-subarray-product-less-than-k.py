class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        ans = 1
        count = 0
        if k<=1:
            return 0
        for j in range(0,n):
            ans = ans*nums[j]
            while ans>=k:
                ans = ans//nums[i]
                i+=1
            if ans<k:
                count+=j-i+1
        return count
