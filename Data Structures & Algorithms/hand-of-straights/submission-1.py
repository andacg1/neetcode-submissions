from heapq import *
from queue import *
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # freq = Counter(hand)
        # heapify(hand)
        # while len(hand) > 0:
        hand.sort()
        queue = deque(hand)
        while len(queue) > 0:
            curr = queue.popleft()
            temp = deque()
            group = 1
            while group < groupSize and len(queue) > 0:
                next_number = queue.popleft()
                if next_number == curr + 1:
                    curr = next_number
                    group += 1
                elif next_number > curr + 1:
                    return False
                else:
                    temp.appendleft(next_number)
            queue.extendleft(temp)
            # print(queue)
            if 0 < len(queue) < groupSize:
                return False
            
        return len(queue) == 0
