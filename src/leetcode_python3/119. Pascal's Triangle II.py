# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 33:
            res = []
            for i in range(rowIndex+1):
                temp = [1]*(i+1)
                res.append(temp)
                for j in range(1, i):
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
            return res[rowIndex]
        else:
            return False
