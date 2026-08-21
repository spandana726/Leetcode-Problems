class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        i = 0
        count = 0
        ans = 0
        ng = 0
        for k in range(0,n):
            if grumpy[k]==0:
                count+=customers[k]
        for j in range(0,n):
            if grumpy[j]==1:
                ng+=customers[j]
            if j-i+1>minutes:
                if grumpy[i]==1:
                    ng-=customers[i]
                i+=1
            if j-i+1==minutes:
                ans = max(ans,ng)
        return count+ans


        
