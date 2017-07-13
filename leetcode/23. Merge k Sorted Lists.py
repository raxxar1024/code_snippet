# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


if __name__ == "__main__":
    l1 = ListNode(3)
    l2 = ListNode(4)
    l3, l3.next, l3.next.next = ListNode(1), ListNode(5), ListNode(7)
    l4, l4.next, l4.next.next = ListNode(2), ListNode(6), ListNode(8)
    l = [l1, l2, l3, l4]
    result = Solution().mergeKLists(l)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5
    assert result.next.next.next.next.next.val == 6
    assert result.next.next.next.next.next.next.val == 7
    assert result.next.next.next.next.next.next.next.val == 8

    