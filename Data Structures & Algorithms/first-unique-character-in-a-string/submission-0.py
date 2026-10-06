class Solution:
    def firstUniqChar(self, s: str) -> int:
        # seen set
        # candidates set
        # second pass?
        seen = set()
        cand = set()

        for c in s:
            if c not in seen:
                cand.add(c)
            elif c in cand:
                cand.remove(c)
            seen.add(c)

        for i, c in enumerate(s):
            if c in cand:
                return i
        
        return -1
