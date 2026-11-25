class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            bits = 0
            num = i

            if num >= 512:
                num -= 512
                bits += 1
            if num >= 256:
                num -= 256
                bits += 1
            if num >= 128:
                num -= 128
                bits += 1
            if num >= 64:
                num -= 64
                bits += 1
            if num >= 32:
                num -= 32
                bits += 1
            if num >= 16:
                num -= 16
                bits += 1
            if num >= 8:
                num -= 8
                bits += 1
            if num >= 4:
                num -= 4
                bits += 1
            if num >= 2:
                num -= 2
                bits += 1
            if num >= 1:
                num -= 1
                bits += 1
            
            res.append(bits)

        return res


            
