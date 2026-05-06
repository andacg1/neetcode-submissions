"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0
        intervals.sort(key=lambda x: x.start)
        queue = deque(intervals)
        def overlaps(first_interval: Interval, second_interval: Interval) -> bool:
            return second_interval.start < first_interval.end
        while len(queue) > 0:
            temp_queue = []
            left = 0
            right = 1
            while left < right and right < len(queue):
                while right < len(queue) and overlaps(queue[left], queue[right]):
                    temp_queue.append(queue[right])
                    right += 1
                left = right
                right = left + 1
            rooms += 1
            queue = temp_queue
        return rooms


