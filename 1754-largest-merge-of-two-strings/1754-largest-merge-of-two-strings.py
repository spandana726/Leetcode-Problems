class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        s = ""
        k = ""
        i = 0
        j = 0
        m = len(word1)
        n = len(word2)
        while(i<m and j<n):
            if(word1[i]==word2[j]):
                if(word1[i:]>word2[j:]):
                    s+=word1[i]
                    i+=1
                else:
                    s+=word2[j]
                    j+=1
            elif(word1[i]>word2[j]):
                s+=word1[i]
                i+=1
            else:
                s+=word2[j]
                j+=1
        while(i<m):
            k+=word1[i]
            i+=1
        while(j<n):
            k+=word2[j]
            j+=1
        return s+k
        