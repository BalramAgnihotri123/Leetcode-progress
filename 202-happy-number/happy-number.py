class Solution(object):
    def isHappy(self, n):
        seen = {}
        n = str(n)

        while True:
            isHappy = 0
            for s in n:
                isHappy += int(s) ** 2

            if isHappy == 1:
                return True
            elif isHappy in seen:
                return False                

            seen[isHappy] = n
            n = str(isHappy)
        