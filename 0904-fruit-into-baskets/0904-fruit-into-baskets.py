class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = 0
        i = 0
        dic = {}
        for j in range(0,n):
            dic[fruits[j]] = dic.get(fruits[j],0)+1
            if len(dic)>2:
                dic[fruits[i]]-=1
                if dic[fruits[i]]==0:
                    del dic[fruits[i]]
                i+=1
            if len(dic)<=2:
                ans = max(ans,j-i+1)
        return ans
                

        

        
        