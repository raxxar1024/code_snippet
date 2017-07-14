# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

if __name__ == "__main__":
    l1, l1.next, l1.next.next, l1.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    result = Solution().swapPairs(l1)
    assert result.val == 2
    assert result.next.val == 1
    assert result.next.next.val == 4
    assert result.next.next.next.val == 3


