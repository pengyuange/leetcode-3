# -*- coding:utf-8 -*-


#
# Given two binary trees, write a function to check if they are equal or not.
#
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if None in (node1, node2) or node1.val != node2.val:
                return False
            if node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        
        return True
