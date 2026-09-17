class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for a in s:
            if a.isdigit() or a.isalpha():
                string += a.lower()

        l, r = 0, len(string) - 1
        print(string)
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        
        return True