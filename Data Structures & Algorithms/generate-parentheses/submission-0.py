class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(seq: List[str], balance: int):
            if balance < 0:
                return
            if len(seq) == n * 2:
                if balance == 0:
                    result.append("".join(seq))
                return

            seq.append(")")
            generate(seq, balance - 1)
            seq.pop()

            seq.append("(")
            generate(seq, balance + 1)
            seq.pop()


        generate([], 0)
        return result