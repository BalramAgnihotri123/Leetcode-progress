class Solution(object):
    def isHappy(self, n):
        seen = set()
        n = str(n)

        while True:
            isHappy = 0
            for s in n:
                isHappy += int(s) * int(s)
            
            if isHappy == 1:
                return True
            elif isHappy in seen:
                return False
            else:
                seen.add(isHappy)
                n = str(isHappy)
        