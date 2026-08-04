class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            if i == len(words) or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
            else:
                spaces = maxWidth - length
                gaps = len(line) - 1
                even = spaces // gaps
                extra = spaces % gaps

                s = ""
                for j in range(gaps):
                    s += line[j]
                    s += " " * (even + (1 if j < extra else 0))
                s += line[-1]

            res.append(s)

        return res