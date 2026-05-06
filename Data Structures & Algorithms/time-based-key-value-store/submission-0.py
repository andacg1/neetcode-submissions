class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        lo = 0
        hi = len(values) - 1
        if len(values) == 0:
            return ""
        candidate = (0, "")
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] <= timestamp:
                candidate = max(candidate, values[mid])
                lo = mid + 1
            else:
                hi = mid - 1
        return candidate[1]