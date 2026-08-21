class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        count = 0
        ans = 0
        for k in range(0,n):
            if grumpy[k]==0:
                count+=customers[k]
        for i in range(0,n-minutes+1):
            ng = 0
            for j in range(i,i+minutes):
                if grumpy[j]==1:
                    ng+=customers[j]
            ans = max(ans,ng)
        count+=ans
        return count

        
