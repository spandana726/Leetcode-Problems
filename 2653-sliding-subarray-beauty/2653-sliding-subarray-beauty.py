class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        l = []
        i = 0
        n = len(nums)
        dic = {}
        for j in range(0,n):
            dic[nums[j]] = dic.get(nums[j],0)+1
            if j-i+1>k:
                dic[nums[i]]-=1
                if dic[nums[i]]==0:
                    del dic[nums[i]]
                i+=1
            if j-i+1==k:
                count = 0
                for num in sorted(dic.keys()):
                    if num<0:
                        count+=dic[num]
                        if count>=x:
                            l.append(num)
                            break
                else:
                    l.append(0)
        return l


        
        
        