from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for s in strs:
            anagrams[tuple(sorted(s))].append(s)

        for v in anagrams.values():
            res.append(v)

        return res