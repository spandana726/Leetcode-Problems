class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = 0
        answer2 = 0
        sol = [0]*2
        m = len(nums1)
        n = len(nums2)
        for i in range(0,m):
            if nums1[i] in nums2:
                answer1+=1
        for j in range(0,n):
            if nums2[j] in nums1:
                answer2+=1
        sol = [answer1,answer2]
        return sol

        