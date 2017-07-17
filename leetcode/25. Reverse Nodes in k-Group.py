# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result = []
        list_head = []
        while head:
            list_head.append(head.val)
            head = head.next

        count = len(list_head) / k

        for i in xrange(count):
            tmp1 = list_head[i*k:i*k+k]
            tmp1.reverse()
            result += tmp1
        result += list_head[(count-1)*k+k:]

        dummy = ListNode(-1)
        current = dummy

        for i in xrange(len(result)):
            current.next = ListNode(result[i])
            current = current.next

        return dummy.next


if __name__ == "__main__":
    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    result = Solution().reverseKGroup(l1, 2)
    assert result.val == 2
    assert result.next.val == 1
    assert result.next.next.val == 4
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 5

    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    result = Solution().reverseKGroup(l1, 3)
    assert result.val == 3
    assert result.next.val == 2
    assert result.next.next.val == 1
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5


