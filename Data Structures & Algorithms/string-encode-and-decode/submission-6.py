class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for s in strs:
            encoded_string += f"{len(s)}#{s}"

        print(encoded_string)
        return(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            num_chars = ""
            while s[i] != '#':
                num_chars += s[i]
                i += 1
            i -= 1
            num_chars = int(num_chars)
            word = s[i + 2:(i + num_chars + 2)]
            decoded_strs.append(word)
            i += num_chars + 2

        return decoded_strs
        
