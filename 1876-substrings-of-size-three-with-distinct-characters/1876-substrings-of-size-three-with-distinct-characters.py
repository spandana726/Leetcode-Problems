class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        n = len(s)
        mp = {}
        count = 0
        for r in range(0,n):
            mp[s[r]] = mp.get(s[r],0)+1
            if r-l+1>3:
                mp[s[l]]-=1
                if(mp[s[l]]==0):
                    del mp[s[l]]
                l+=1
            if r-l+1==3 and len(mp)==3:
                count+=1
        return count
    
            
