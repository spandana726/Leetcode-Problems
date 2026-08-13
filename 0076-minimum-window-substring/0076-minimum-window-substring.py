class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        dic = {}
        tic = {}
        i = 0
        f = 0
        ans = float('inf')
        finalans = ""
        for num in range(0,n):
            tic[t[num]] = tic.get(t[num],0)+1
        for j in range(0,m):
            dic[s[j]] = dic.get(s[j],0)+1
            if s[j] in t and dic[s[j]]==tic[s[j]]:
                f+=1
            while f==len(tic):
                length = j-i+1
                if length<ans:
                    ans = length
                    finalans = s[i:j+1]
                dic[s[i]] -= 1
                if s[i] in tic and dic[s[i]] < tic[s[i]]:
                    f -= 1
                i+=1
                
        return finalans
                
                





            
                


            
        