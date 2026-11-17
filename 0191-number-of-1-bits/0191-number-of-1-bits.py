class Solution:
    def hammingWeight(self, n: int) -> int:
        k = n
        count = 0
        while k!=0:
            ans = k%2
            if ans==1:
                count+=1
            k = k//2
        return count
