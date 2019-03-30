"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
Ex:
input: [1,8,6,2,5,4,8,3,7]
output: 49
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #My code starts here
        capacity=0
        index_1=0
        index_2=len(height)-1
        while index_1<index_2:
            capacity=max(capacity,min(height[index_1],height[index_2])*(index_2-index_1))
            if height[index_1]<height[index_2]:
                index_1+=1
            else:
                index_2-=1
        return capacity

"""
My thinking:采取动态规划的方法，我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。最初我们考虑由最外围两条线段构成的区域。现在如果我们试图将指向较长线段的指针向内侧移动，矩形区域的面积将受限于较短的线段而不会获得任何增加。但是，在同样的条件下，移动指向较短线段的指针尽管造成了矩形宽度的减小，但却可能会有助于面积的增大。
"""
