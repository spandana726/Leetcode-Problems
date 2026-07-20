class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        l = 0
        mp = {}
        ls = []
        d = {}
        for i in range(0,m):
            d[p[i]] = d.get(p[i],0)+1
        for r in range(0,n):
            mp[s[r]] = mp.get(s[r],0)+1
            if r-l+1>m:
                mp[s[l]]-=1
                if(mp[s[l]]==0):
                    del mp[s[l]]
                l+=1
            if r-l+1==m and mp==d:
                ls.append(l)
        return ls

        