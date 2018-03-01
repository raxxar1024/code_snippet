"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, head, reverse = reverse, head.next, head

        tail = head.next if fast else head
        while tail:
            if reverse.val != tail.val:
                return False
            reverse, tail = reverse.next, tail.next
        return True


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_1.next = ListNode(2)
    node_1.next.next = ListNode(3)
    node_1.next.next.next = ListNode(2)
    node_1.next.next.next.next = ListNode(1)
    assert Solution().isPalindrome(node_1) is True
