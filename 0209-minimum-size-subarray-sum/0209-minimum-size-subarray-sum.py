class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        ans = float('inf')
        sums = 0
        dic = {}
        for j in range(0,n):
            dic[nums[j]] = dic.get(nums[j],0)+1
            sums+=nums[j]
            while sums>=target:
                ans = min(ans,j-i+1)
                sums-=nums[i]
                i+=1
        if ans==float('inf'):
            ans = 0
        return ans


            
        