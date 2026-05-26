class Solution:
    def isValid(self, s: str) -> bool:
        # use stack, O(n)
        stack = []
        closetoopen = {")": "(", "]": "[","}": "{"}

        for c in s:
            if c in closetoopen: # if c is close we pop
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False 
        