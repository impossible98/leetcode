# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return[]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        
        ans = [[1],[1,1]]
        for i in range(2, numRows):
            tmp=[1]
            for j in range(i-1):
                tmp=tmp+[ans[i-1][j]+ans[i-1][j+1]]
            tmp=tmp+[1]
            ans.append(tmp)
            
        return ans