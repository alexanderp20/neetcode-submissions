class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            match c:
                case '+':
                    number2 = stack.pop()
                    number1 = stack.pop()
                    stack.append(number1 + number2)
                case '-':
                    number2 = stack.pop()
                    number1 = stack.pop()
                    stack.append(number1 - number2)
                case '*':
                    number2 = stack.pop()
                    number1 = stack.pop()
                    stack.append(number1 * number2)
                case '/':
                    number2 = stack.pop()
                    number1 = stack.pop()
                    stack.append(int(number1 / number2))
                case _:
                    stack.append(int(c))

        return int(stack[-1])