class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        uniqueChars = {c for c in f"{s1}{s2}"}
        testChars = {c: 0 for c in uniqueChars}
        chars = {c: 0 for c in uniqueChars}
        
        left = 0
        right = 0
        for c in s1:
            testChars[c] += 1
        while right < len(s1):
            chars[s2[right]] += 1
            right += 1
        # print(uniqueChars,)

        def isSame() -> bool:
            for k,v in chars.items():
                if testChars[k] != v:
                    return False
            return True
        while right < len(s2):
            # print( testChars, )
            # print(chars)
            if isSame():
                print(s2[left:right])
                return True
            # print("not same")

            chars[s2[left]] -= 1
            left += 1
            chars[s2[right]] += 1
            right += 1
        if isSame():
            print(s2[left:right])
            return True
        return False
