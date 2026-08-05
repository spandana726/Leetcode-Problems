class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxsum = 0
        s = 0
        i = 0
        n = len(nums)
        dic = {}
        for j in range(0,n):
            dic[nums[j]] = dic.get(nums[j],0)+1
            s+=nums[j]
            if j-i+1>k:
                dic[nums[i]]-=1
                if dic[nums[i]]==0:
                    del dic[nums[i]]
                s-=nums[i]
                i+=1
            if len(dic)==k:
                maxsum = max(maxsum,s)
        return maxsum


        