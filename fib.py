# -*- coding: utf-8 -*-
# Project: maxent-ml
# Author: llC create this file
# Time: 2019/1/16
# Email: yanhuayisan@126.com

class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == '__main__':
    a = Solution()
    print(a.fibonacci(40))
