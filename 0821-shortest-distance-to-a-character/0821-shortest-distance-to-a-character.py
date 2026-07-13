class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        for i in range(0,len(s)):
            mini = float('inf')
            for j in range(0,len(s)):
                if c in s[j]:
                    mini = min(mini,abs(i-j))
            answer.append(mini)
        return answer

        