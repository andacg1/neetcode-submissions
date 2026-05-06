class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        if len(s) <= 1:
            return len(s)
        
        seen = set(s[0])
        maxLength = len(seen)
        while right < len(s) and left < right:
            if s[right] in seen:
                while s[left] != s[right] and left < right:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                seen.add(s[right])
            maxLength = max(maxLength,len(seen))
            right += 1
        return maxLength

