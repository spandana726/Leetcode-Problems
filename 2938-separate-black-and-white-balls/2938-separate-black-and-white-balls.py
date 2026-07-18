class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        count = 0
        while(j<n):
            if(s[j]=='0'):
                count+=j-i
                i+=1
            j+=1
        return count
        