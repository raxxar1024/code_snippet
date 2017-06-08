# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # tmp1 = l1
        # tmp2 = l2
        jinwei = 0
        tmp_result = ListNode(0)
        result = tmp_result
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            val = val1 + val2 + jinwei
            if val >= 10:
                val -= 10
                jinwei = 1
            else:
                jinwei = 0
            tmp_result.next = ListNode(val)
            tmp_result = tmp_result.next
        if jinwei == 1:
            tmp_result.next = ListNode(1)
        return result.next

if __name__ == "__main__":
    l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
    l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
    print "{0}-->{1}-->{2}".format(result.val, result.next.val, result.next.next.val)

    l1 = ListNode(5)
    l2 = ListNode(5)
    result = Solution().addTwoNumbers(l1, l2)
    assert result.val == 0
    assert result.next.val == 1




