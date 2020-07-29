"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate 
between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 如果这颗树的根节点为空，则直接返回[]
        if not root:
            return []
        # 定义一个队列，开始存放着根节点
        queue = [root]
        # 定义一个变量储存输出
        output = []
        # 定义一个布尔变量来设置遍历的方向
        flag = True
        # 当队列为空时，也就是遍历完最底层了，则结束遍历。
        while queue:
            # 定义一个临时的队列，存放孩子节点
            tmp = []
            # 定义数组存放这层的遍历结果
            zigzagLevel_result = []
            # 正向遍历
            if flag:
                # 对队列内的每个节点，储存它们的孩子节点到tmp队列，并且存放它们的val到zigzagLevel_result数组
                while queue:
                    # 弹出节点
                    node = queue.pop()
                    zigzagLevel_result.append(node.val)
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            # 反向遍历
            else:
                while queue:
                    node = queue.pop()
                    zigzagLevel_result.append(node.val)
                    if node.right:
                        tmp.append(node.right)
                    if node.left:
                        tmp.append(node.left)
                        
            """
            # 简化后的代码
            while queue:
                node = queue.pop()
                zigzagLevel_result.append(node.val)
                if flag and node.left:
                    tmp.append(node.left)
                if flag and node.right:
                    tmp.append(node.right)
                if not flag and node.right:
                    tmp.append(node.right)
                if not flag and node.left:
                    tmp.append(node.left)
            """
            
            # 改变遍历的方向
            flag = not flag
            # 把临时的队列赋给queue
            queue = tmp
            # 添加这层的遍历结果到最后的输出
            output.append(zigzagLevel_result)
        return output
 """
 思路：广度优先遍历（层层推进），详细步骤见注释，比起102题来说多了一个变量定义遍历的方向。时间复杂度为O(n)，空间复杂度为O(n)。如果采用深度优先遍历的话，空间复杂度可以达到O(h)，其中h为树的高度，
 但这种方法还没搞清楚。
 """
