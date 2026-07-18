class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i = 0
        j = 0
        m = len(start)
        n = len(target)
        while(i<m and j<n):
            while(i<m and start[i]=='_'):
                i+=1
            while(j<n and target[j]=='_'):
                j+=1
            if(i==m and j==n): # for input a = ____ , b = ______ a lenght is 3 b length is 4
                return True
            if(i==m or j==n): # # after increment i is 4 j is 4 (RTE out of bounds)
                return False
            if(start[i]!=target[j]):
                return False
            if(start[i]=='L' and j>i):
                return False
            if(start[i]=='R' and j<i):
                return False
            i+=1
            j+=1
        while i<m:
            if(start[i]!='_'):
                return False
            i+=1
        while j<n:
            if(target[j]!='_'):
                return False
            j+=1
        return True

   # start  = "L_" target = "__" return i == m and j == n  return False and True

        