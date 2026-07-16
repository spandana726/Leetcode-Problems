class Solution:
    def minimumLength(self, s: str) -> int:
        k = list(s)
        n = len(k)
        i = 0
        j = n-1
        while(i<j):
            if(s[i]!=s[j]):
                break
            p = s[i]
            q = s[j]
            while(i<=j and s[i]==p):
                i+=1
            while(i<=j and s[j]==q):
                j-=1
        return (j-i)+1


        