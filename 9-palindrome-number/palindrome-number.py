class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)
        for i in range(0, n//2):
            if x[i] != x[n-i-1]:
                return False
        return True
        