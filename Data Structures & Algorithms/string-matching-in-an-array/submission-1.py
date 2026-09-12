class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j:
                    res.add(words[i])
                    break
        
        return list(res)

