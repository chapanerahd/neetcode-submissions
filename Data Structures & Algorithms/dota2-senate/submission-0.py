from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while r_queue and d_queue:
            ridx = r_queue.popleft()
            didx = d_queue.popleft()
            if ridx < didx:
                r_queue.append(ridx + n)
            else:
                d_queue.append(didx + n)

        return "Radiant" if r_queue else "Dire"