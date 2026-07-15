class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        count = n
        i = 0
        j = 0
        if(m<n):
            return False
        while(i<m and j<n):
            character = str1[i]
            if(character=='z'):
                nextc = 'a'
            else:
                nextc = chr(ord(character)+1)
            if(character == str2[j] or nextc==str2[j]):
                i+=1
                j+=1
                count-=1
            else:
                i+=1
        if(count==0):
            return True
        else:
            return False

        