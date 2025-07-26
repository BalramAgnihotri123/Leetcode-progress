class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valids = {"{" : "}", "[" : "]", "(" : ")"}

        stack = []
        for char in s:
            if char not in valids:
                if not stack:
                    return False
                elif valids[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False