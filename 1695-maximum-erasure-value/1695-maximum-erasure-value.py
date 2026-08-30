class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        sumi = 0
        i = 0
        dic = {}
        for j in range(0,n):
            dic[nums[j]] = dic.get(nums[j],0)+1
            sumi+=nums[j]
            while j-i+1>len(dic):
                sumi-=nums[i]
                dic[nums[i]]-=1
                if dic[nums[i]]==0:
                    del dic[nums[i]]
                i+=1
            if j-i+1==len(dic):
                ans = max(ans,sumi)
        return ans

        