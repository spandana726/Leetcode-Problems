class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxans = float('-inf')
        summ = float('-inf')
        ans = 0
        i = 0
        n = len(nums)
        for j in range(0,n):
            ans+=nums[j]
            if j-i+1>k:
                ans-=nums[i]
                i+=1
            if j-i+1==k:
                summ = ans/k
            maxans = max(maxans,summ)
        return maxans
            

        