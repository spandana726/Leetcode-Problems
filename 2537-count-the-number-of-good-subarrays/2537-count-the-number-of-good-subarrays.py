class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        i = 0
        dic = {}
        n = len(nums)
        count = 0
        ans = 0
        for j in range(0,n):
            dic[nums[j]] = dic.get(nums[j],0)+1
            count+=dic[nums[j]]-1
            while count>=k:
                dic[nums[i]]-=1
                count-=dic[nums[i]]
                i+=1
            ans+=i
        return ans
        