class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        j = 0
        count = 0
        i = 0
        while(j<n):
            k = chars[j]
            while(j<n and chars[j]==k):
                j+=1
            chars[count] = chars[i]
            count+=1
            k = j-i
            if k>1:
                for c in str(k):
                    chars[count] = c
                    count+=1
            i = j
        return count




        

        