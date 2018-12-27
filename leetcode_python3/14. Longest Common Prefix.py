# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sameTitle = ''
        if strs:
            head = strs[0]
        else:
            return ''
        for i in strs:
            for j in range(len(i)):
                if j < len(head) and i[j] == head[j]:
                    sameTitle += head[j]
                else:
                    break
            head = sameTitle
            sameTitle = ''
        return head
