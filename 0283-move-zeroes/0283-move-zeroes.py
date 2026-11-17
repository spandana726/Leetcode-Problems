class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        n = len(nums)
        for j in range(0,n):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        while i<n:
            nums[i]=0
            i = i+1
        