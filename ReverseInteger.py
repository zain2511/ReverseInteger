class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            posrev = int(str(x)[::-1])
            if posrev > 2147483647:
                return 0
            else:
                return posrev
        else:
            negrev = int(str(x)[1:][::-1])
            if negrev > 2147483647:
                return 0
            else:
                return negrev * -1