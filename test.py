class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 1
        for j, k in enumerate(digits):
            num += k * 10 ** int(len(digits) - 1 - j)
        return [int(i) for i in str(num)]
