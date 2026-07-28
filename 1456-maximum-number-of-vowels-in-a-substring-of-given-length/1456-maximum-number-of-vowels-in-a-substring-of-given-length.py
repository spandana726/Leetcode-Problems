class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = {}
        n = len(s)
        i = 0
        maxlen = 0
        a = set('aeiou')
        for j in range(0,n):
            count = 0
            dic[s[j]] = dic.get(s[j],0)+1
            if j-i+1>k:
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
                i+=1
            if j-i+1==k:
                for ch in dic.keys():
                    if ch in a:
                        count+=dic[ch]
            maxlen = max(maxlen,count)
        return maxlen
        