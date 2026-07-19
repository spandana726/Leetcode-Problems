class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        k = ""
        count = 0
        for i in range(0,n-2):
            mp = {}
            for j in range(i,i+3):
                if s[j] in mp:
                    mp[s[j]]+=1
                else:
                    mp[s[j]] = 1
            if len(mp)==3:
                count+=1
        return count

        