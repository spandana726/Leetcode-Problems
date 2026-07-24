class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = {}
        b = {}
        l = 0
        r = 0
        m = len(s1)
        n = len(s2)
        k = s1[::-1]
        for i in range(0,len(k)):
            a[k[i]] = a.get(k[i],0)+1
        for r in range(0,n):
            b[s2[r]] = b.get(s2[r],0)+1
            if r-l+1>m:
                b[s2[l]]-=1
                if(b[s2[l]]==0):
                    del b[s2[l]]
                l+=1       
            if a==b:
                return True
        return False
    
        


        