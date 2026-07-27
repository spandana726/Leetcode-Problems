class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        substr = 2**k
        i = 0
        count = 0
        dic = {}
        for j in range(0,n):
            if j-i+1>k:
                i+=1  
            if j-i+1==k:
                dic[s[i:j+1]] = dic.get(s[i:j+1],0)+1
        if(len(dic)>=substr):
            return True
        else:
            return False

               



        

        