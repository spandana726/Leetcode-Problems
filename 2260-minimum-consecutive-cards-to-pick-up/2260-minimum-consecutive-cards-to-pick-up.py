class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        n = len(cards)
        dic = {}
        mini = float('inf')
        for i in range(0,n):
            if cards[i] not in dic:
                dic[cards[i]] = i
            else:
                mini = min(mini,i-dic[cards[i]]+1)
                dic[cards[i]] = i
        if mini == float('inf'):
            mini = -1
        return mini
                
        