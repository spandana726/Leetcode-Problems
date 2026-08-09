class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans = 0
        i = 0
        n = len(s)
        ans = 0
        dic = {}
        maps = {}
        for j in range(0,n):
            dic[s[j]] = dic.get(s[j],0)+1
            if j-i+1>minSize:
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
                i+=1
            if j-i+1==minSize and j-i+1<=maxSize and len(dic)<=maxLetters:
                maps[s[i:j+1]] = maps.get(s[i:j+1],0)+1
                ans = max(ans,maps[s[i:j+1]])
        return ans
