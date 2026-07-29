class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l = [-1]*n
        s = 2*k+1
        sums = 0
        i = 0
        for j in range(0,n):
            sums+=nums[j]
            if j-i+1>s:
                sums-=nums[i]
                i+=1
            if j-i+1==s:
                l[j-k] = sums//s
        return l
            

            



        