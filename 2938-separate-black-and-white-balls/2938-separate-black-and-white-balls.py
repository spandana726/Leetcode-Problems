class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        n = len(s)

        while j < n:
            if s[j] == '0':
                ans += j - i
                i += 1
            j += 1

        return ans