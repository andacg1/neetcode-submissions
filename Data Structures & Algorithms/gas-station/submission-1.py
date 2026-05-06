class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def next_index(i: int) -> int:
            return (i + 1) % len(cost)
        last_start = 0
        def can_travel(start: int) -> bool:
            curr_gas = 0
            curr_pos = start
            target = (start + len(cost) - 1) % len(cost)
            while curr_pos != target:
                curr_gas += gas[curr_pos]
                if cost[curr_pos] > curr_gas:
                    return False
                curr_gas -= cost[curr_pos]
                curr_pos = next_index(curr_pos)
            curr_gas += gas[curr_pos]
            return cost[curr_pos] <= curr_gas
        for i in range(len(gas)):
            if can_travel(i):
                return i
        return -1
