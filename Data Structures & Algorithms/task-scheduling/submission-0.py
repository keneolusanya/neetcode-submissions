from collections import defaultdict
from collections import deque
import heapq as hq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count of every character from tasks added to a max heap
        # also have a q
        # when you pop from max heap, decrement by 1
        # then add that decremented number to queue, along time + n:
        # basically, at what time is that task going to be available to use to
        # process again?
        # keep track of time variable
        # then at each time, you check the queue and add back all available tasks
        # when a task becomes 0, we don't add it back to the queue, you just pop 
        # from heap
        # then return time
        counts = Counter(tasks)
        maxHeap = list(counts.values())
        hq.heapify_max(maxHeap)
        
        time = 0
        q = deque()
        
        while maxHeap or q:
            time += 1
            if len(maxHeap) > 0:
                t = hq.heappop_max(maxHeap)
                t -= 1
                if t != 0:
                    q.append((t, time + n))

            while q and q[0][1] == time:
                nt = q.popleft()
                hq.heappush_max(maxHeap, nt[0])

        return time





        


        

        