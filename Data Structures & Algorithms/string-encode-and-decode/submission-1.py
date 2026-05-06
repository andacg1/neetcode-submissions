class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return "".join(map(lambda x: f"\n{x}", strs))
    def decode(self, s: str) -> List[str]:
        return s.split("\n")[1:]