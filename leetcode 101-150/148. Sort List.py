"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":
    node_2 = ListNode(2)
    node_2.next = ListNode(1)
    node_2.next.next = ListNode(4)
    node_2.next.next.next = ListNode(3)
    node_r = Solution().sortList(node_2)
    assert node_r.val == 1
    assert node_r.next.val == 2
    assert node_r.next.next.val == 3
    assert node_r.next.next.next.val == 4
