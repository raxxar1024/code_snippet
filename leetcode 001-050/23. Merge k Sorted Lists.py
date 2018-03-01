# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        return self.merge_two_parts(lists[:length/2], lists[length/2:])

    def merge_two_parts(self, part1, part2):
        length1, length2 = len(part1), len(part2)
        if length1 > 1:
            p1 = self.merge_two_parts(part1[:length1/2], part1[length1/2:])
        elif length1 == 1:
            p1 = part1[0]
        else:
            p1 = None

        if length2 > 1:
            p2 = self.merge_two_parts(part2[:length2/2], part2[length2/2:])
        elif length2 == 1:
            p2 = part2[0]
        else:
            p2 = None
        return self.merge_two_list(p1, p2)

    def merge_two_list(self, p1, p2):
        result = dummy = ListNode(-1)
        while p1 and p2:
            if p1.val > p2.val:
                dummy.next = p2
                p2 = p2.next
            else:
                dummy.next = p1
                p1 = p1.next
            dummy = dummy.next
        dummy.next = p1 or p2
        return result.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap_list = []
        dummy = current = ListNode(-1)
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap_list, (sorted_list.val, sorted_list))

        while heap_list:
            smallest = heapq.heappop(heap_list)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap_list, (smallest.next.val, smallest.next))

        return dummy.next

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

