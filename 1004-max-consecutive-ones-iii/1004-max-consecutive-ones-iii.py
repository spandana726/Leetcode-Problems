class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        dic = {}
        ans = 0
        count1 = 0
        for j in range(0,n):
            dic[nums[j]] = dic.get(nums[j],0)+1
            if nums[j]==1:
                count1+=1
            windowsize = j-i+1
            if windowsize-count1>k:
                dic[nums[i]]-=1
                count1-=nums[i]
                if dic[nums[i]]==0:
                    del dic[nums[i]]
                i+=1
            if (j-i+1)-count1<=k:
                ans = max(ans,j-i+1)
        return ans
        