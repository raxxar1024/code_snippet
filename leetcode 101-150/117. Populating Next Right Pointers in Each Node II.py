"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_1(self, root):
        if root is None:
            return
        current = [root]
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            if len(next_level) > 1:
                for i in xrange(len(next_level) - 1):
                    next_level[i].next = next_level[i + 1]
        return

    def connect(self, root):
        if root is None:
            return
        head = root
        while head:
            pre, curr, next_head = None, head, None
            while curr:
                if next_head is None:
                    if curr.left:
                        next_head = curr.left
                    elif curr.right:
                        next_head = curr.right
                        
                if curr.left:
                    if pre:
                        pre.next = curr.left
                    pre = curr.left

                if curr.right:
                    if pre:
                        pre.next = curr.right
                    pre = curr.right

                curr = curr.next
            head = next_head


if __name__ == "__main__":
    tree_link_1 = TreeLinkNode(1)
    tree_link_1.left = TreeLinkNode(2)
    tree_link_1.left.left = TreeLinkNode(4)
    tree_link_1.left.right = TreeLinkNode(5)
    tree_link_1.right = TreeLinkNode(3)
    tree_link_1.right.right = TreeLinkNode(7)
    Solution().connect(tree_link_1)
    assert tree_link_1.left.next.val == tree_link_1.right.val
    assert tree_link_1.left.left.next.val == tree_link_1.left.right.val
    assert tree_link_1.left.right.next.val == tree_link_1.right.right.val
