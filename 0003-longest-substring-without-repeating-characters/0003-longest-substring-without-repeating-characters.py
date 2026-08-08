class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        l = set()
        n = len(s)
        maxlen = 0
        for j in range(0,n):
            while s[j] in l:
                l.remove(s[i])
                i+=1
            l.add(s[j])
            maxlen = max(maxlen,j-i+1)
        return maxlen