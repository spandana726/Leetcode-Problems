class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        i = 0
        sum = 0
        for j in range(0,n):
            sum+=arr[j]
            if j-i+1>k:
                sum-=arr[i]
                i+=1
            if j-i+1==k:
                if sum/k>=threshold:
                    count+=1
        return count
            
            
        

        