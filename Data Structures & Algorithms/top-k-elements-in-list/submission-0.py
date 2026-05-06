from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for n in nums:
            if n not in freq.keys():
                freq[n] = 0
            freq[n] += 1
        entries = sorted(freq.items(), key=itemgetter(1), reverse=True)
        return list(map(lambda x: x[0],entries))[:k]