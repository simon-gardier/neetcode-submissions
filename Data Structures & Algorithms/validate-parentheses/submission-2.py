class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_opening = {"}": "{", ")": "(", "]": "["}
        for parenthesis in s:
            if parenthesis in "({[":
                stack.append(parenthesis)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != closing_to_opening[parenthesis]:
                    return False
        if len(stack) > 0:
            return False
        return True
