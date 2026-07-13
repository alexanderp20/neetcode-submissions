class Solution:
    def isValid(self, s: str) -> bool:
        stringStack = []
        if len(s) <= 1:
            return False

        for i in range(len(s)):
            match s[i]:
                case ')':
                    if len(stringStack) > 0 and stringStack[-1] == '(':
                        stringStack.pop()
                    else:
                        return False
                case '}':
                    if len(stringStack) > 0 and stringStack[-1] == '{':
                        stringStack.pop()
                    else:
                        return False 
                case ']':
                    if len(stringStack) > 0 and stringStack[-1] == '[':
                        stringStack.pop()
                    else:
                        return False
                case _:
                    stringStack.append(s[i])

        return len(stringStack) == 0