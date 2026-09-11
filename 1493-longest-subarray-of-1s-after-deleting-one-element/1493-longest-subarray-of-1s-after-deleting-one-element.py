class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        n = len(nums)
        count0=0
        for j in range(0,n):
            if nums[j]==0:
                count0+=1
            if count0>1:
                if nums[i]==0:
                    count0-=1
                i+=1  
            if count0<=1:
                ans = max(ans,j-i)
        return ans
        

        