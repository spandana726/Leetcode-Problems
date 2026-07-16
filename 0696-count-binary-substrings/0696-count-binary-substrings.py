class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        n = len(s)
        count1 = 0
        while(j<n):
            while(j<n and s[j]!='1'):
                j+=1
            count0 = (j-i)
            i = j
            ans+=min(count0,count1)
            while(j<n and s[j]!='0'):
                j+=1
            count1 = (j-i)
            i = j
            ans+=min(count0,count1)
        return ans

