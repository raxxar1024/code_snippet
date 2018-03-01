"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 -> a2
                   |
                   |->
                        c1 -> c2 -> c3
                   |->
                   |
B:     b1 -> b2 -> b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        t1, t2, begin = None, None, None
        while p1 and p2:
            if p1 is p2:
                begin = p1
                break

            if p1.next:
                p1 = p1.next
            elif t1 is None:
                t1 = headA
                p1 = headB
            else:
                break

            if p2.next:
                p2 = p2.next
            elif t2 is None:
                t2 = headB
                p2 = headA
            else:
                break
        return begin


if __name__ == "__main__":
    a1, a2 = ListNode(11), ListNode(12)
    b1, b2, b3 = ListNode(21), ListNode(22), ListNode(23)
    c1, c2, c3 = ListNode(31), ListNode(32), ListNode(33)
    a1.next = a2
    b1.next, b2.next = b2, b3
    c1.next, c2.next = c2, c3
    a2.next = b3.next = c1
    assert Solution().getIntersectionNode(a1, b1) == c1
