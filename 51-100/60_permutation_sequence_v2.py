"""
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:
Input: n = 3, k = 3
Output: "213"
Example 2:
Input: n = 4, k = 9
Output: "2314"
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 求n!
        product = 1
        for i in range(1,n+1):
            product *= i
        # 初始化输出的字符串
        output_string = ""
        # 从0开始计
        k = k - 1
        # 所有参与排列的数字
        candidates = [i for i in range(1,n+1)]
        for i in range(1,n+1):
            # 更新product，依次为(n-1)!、(n-2)! ...
            product /= n + 1 - i
            # 排第i位时，只需要将k除掉(n-i)!并取整，就能得到这个数字是candidates里的第几位
            index = int(round(k/product))
            # 更新k
            k = k - index * factorials(n-i)
            # 将第i位数字添加到输出的字符串中
            output_string += str(candidates[index])
            # 将这个数字移出candidates
            candidates.pop(index)
        return(output_string)
"""
思路：采用数字的规律而不是回溯法，大大降低了算法的时间复杂度。不再使用递归法定义阶乘函数，而是直接求n!，然后在每一轮循环中用除法求取(n-i)!，能够节省空间，并且加快运算。
"""
