class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        i = 0
        count = 0
        m = len(words)
        n = len(s)
        k = ""
        tic = {}
        ans = ""
        lenofw = len(words[0])
        l =[]
        totalen = len(words)*lenofw
        for character in words:
            tic[character] = tic.get(character,0)+1
        for j in range(0,n):
            if j-i+1>totalen:
                i+=1
            if j-i+1==totalen:
                temp = {}
                for a in range(i,j+1,lenofw):
                    ans = s[a:a+lenofw]
                    if ans not in tic:
                        break
                    temp[ans] = temp.get(ans,0)+1
                if temp==tic:
                    l.append(i)                
        return l


        