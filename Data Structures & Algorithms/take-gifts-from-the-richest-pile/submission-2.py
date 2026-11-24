import math
import heapq as hq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hq.heapify_max(gifts)
        for _ in range(k):
            curr = hq.heappop_max(gifts)
            hq.heappush_max(gifts, math.floor(math.sqrt(curr)))

        return sum(gifts)
