class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        mini = 0
        l = float('-inf')
        r = 0
        n = len(s)
        while s[r] != c:
            r+=1
        i = 0
        while(i<n):
            ans.append(min(i-l,r-i))
            if(i==r):
                l = r
                r+=1
                while(r<n and s[r]!=c):
                    r+=1
                if(r==n):
                    r = float('inf')
            i+=1
        return ans


            





            
        