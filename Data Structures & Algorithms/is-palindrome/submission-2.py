class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for l in s:
            if l != " " and l.isalnum():
                new_string += l
        new_string = new_string.lower()

        half_len = int(len(new_string) / 2)
        for i in range(half_len):
            if new_string[i] != new_string[len(new_string) - i - 1]:
                return False
        return True
        