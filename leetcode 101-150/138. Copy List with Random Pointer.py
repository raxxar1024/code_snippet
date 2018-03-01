"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        copies = {}

        def copyRandomList_recu(node):
            if node in copies:
                copy = copies[node]
                return copy
            else:
                copy = RandomListNode(node.label)
                copies[node] = copy
            if node.next:
                copy.next = copyRandomList_recu(node.next)
            if node.random:
                copy.random = copyRandomList_recu(node.random)
            return copy

        return copyRandomList_recu(head)


if __name__ == "__main__":
    node_1 = RandomListNode(1)
    node_2 = RandomListNode(2)
    node_3 = RandomListNode(3)
    node_4 = RandomListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_1.random = node_3
    node_4.random = node_2
    new_node_1 = Solution().copyRandomList(node_1)
    assert new_node_1.label == 1
    assert new_node_1.next.label == 2
    assert new_node_1.next.next.label == 3
    assert new_node_1.next.next.next.label == 4
    assert new_node_1.random.label == 3
    assert new_node_1.next.next.next.random.label == 2
