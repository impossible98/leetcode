# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        y = ''
        if str(x)[0] == '-':
            y += '-'
        y += str(x)[len(str(x))-1::-1].lstrip("0").rstrip("-")
        y = int(y)
        if -2**31 < y < 2**31-1:
            return y
        else:
            return 0