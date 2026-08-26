class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        count = 0
        ans = 0
        n = len(nums)
        i,m = 0,0
        for j in range(0,n):
            if nums[j]%2!=0:
                count+=1
            while count>k:
                if nums[i]%2!=0:
                    count-=1
                i+=1
                m = i
            if count==k:
                while nums[m]%2==0:
                    m+=1
                ans+=(m-i)+1
        return ans


        