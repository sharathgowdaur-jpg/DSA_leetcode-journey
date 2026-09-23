class Solution:
    def calPoints(self, operations: list[str]) -> int:
        answer = []

        for op in operations:
            if op.lstrip("-").isdigit():
                answer.append(int(op))

            elif op == "+":
                answer.append(answer[-1] + answer[-2])

            elif op == "D":
                answer.append(answer[-1] * 2)

            elif op == "C":
                answer.pop()
        return sum(answer)