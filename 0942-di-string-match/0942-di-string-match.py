class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        perm = [0]*(n+1)
        i = 0
        j = 0
        k = len(perm)-1
        l = 0
        while(i<n):
            if(s[i]=='I'):
                perm[l] = j
                j+=1
            else:
                perm[l] = k
                k-=1   
            i+=1
            l+=1 
            perm[n] = k
        return perm

        


        