class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t = str1 if len(str1) < len(str2) else str2
        s = str1 if t == str2 else str2

        original_t = t
        while len(t) > 0:  
            if len(s) % len(t) != 0:
                t = t[:-1]
                continue
            
            num = int(len(s) / len(t))
            if t * num == s and len(original_t) % len(t) == 0:
                return t
            t = t[:-1]
            
        return ""