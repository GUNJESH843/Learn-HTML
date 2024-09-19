class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for n in range(len(expression)):
            if expression[n] in "+-*":
                left = self.diffWaysToCompute(expression[:n])
                right = self.diffWaysToCompute(expression[n+1:])
                for l in left:
                    for r in right:
                        if expression[n] == '+':
                            result.append(l+r)
                        elif expression[n] == '-':
                            result.append(l-r)
                        elif expression[n] == '*':
                            result.append(l*r)
        if not result:
            result.append(int(expression))
        return result