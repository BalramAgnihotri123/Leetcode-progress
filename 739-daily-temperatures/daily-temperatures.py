class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []
        nge = [0] * n
        
        for i in range(n-1, -1, -1):
            temp = temperatures[i]

            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()

            if stack:
                nge[i] = stack[-1] - i
            stack.append(i)
        
        return nge