class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        maxfreq = 0
        ans = 0
        dic = {}
        for j in range(0,n):
            dic[s[j]]  = dic.get(s[j],0)+1
            windowsize = j-i+1
            maxfreq = max(maxfreq,dic[s[j]])
            if windowsize-maxfreq>k:
                dic[s[i]]-=1
                i+=1
            if (j-i+1)-maxfreq<=k:
                ans = max(ans,j-i+1)
        return ans

        
        