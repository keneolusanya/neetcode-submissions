class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        res = []

        for i in range(1, len(words)):
            newCnt = Counter(words[i])
            for c in cnt:
                cnt[c] = min(cnt[c], newCnt[c])

        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)

        return res

            