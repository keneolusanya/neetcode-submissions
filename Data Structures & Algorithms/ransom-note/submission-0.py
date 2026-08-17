class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)

        for m in magazine:
            mag[m] += 1
        
        for r in ransomNote:
            if r not in mag:
                return False
            elif mag[r] == 1:
                mag.pop(r)
            else:
                mag[r] -= 1
        
        return True
