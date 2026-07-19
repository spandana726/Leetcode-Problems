class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()
        m = len(a)
        n = len(b)
        i = 0
        j = m-1
        k = n-1
        prefix = 0
        suffix = 0
        while(i<m and i<n and a[i]==b[i]):
            prefix+=1
            i+=1
        while( j>=i  and k>=i and a[j]==b[k]):
            suffix+=1
            j-=1
            k-=1
        ans = prefix+suffix
        if(m<n):
            return ans>=m
        else:
            return ans>=n

        

        