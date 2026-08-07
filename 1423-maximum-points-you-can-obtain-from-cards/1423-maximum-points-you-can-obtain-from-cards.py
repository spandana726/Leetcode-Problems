class Solution:
    def maxScore(self, cardpoints: List[int], k: int) -> int:
        n = len(cardpoints)
        i = 0
        s = sum(cardpoints)
        if n==k:
            return s
        sumrem = 0
        minsum = s
        for j in range(0,n):
            sumrem+=cardpoints[j]
            if j-i+1==n-k:
                minsum = min(minsum,sumrem)
                sumrem-=cardpoints[i]
                i+=1
        return s-minsum


        