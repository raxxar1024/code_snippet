"""
Given an Iterator class interface with methods: next() and hasNext(),
design and implement a PeekingIterator that support the peek() operation
-- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?

Credits:
Special thanks to @porker2008 for adding this problem and creating all test cases.

"""


# Below is the interface for Iterator, which is already defined for you.
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.have_next = iterator.hasNext()
        self.peeked = False
        self.val = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.val = self.iterator.next()
            self.peeked = True
        return self.val

    def next(self):
        """
        :rtype: int
        """
        self.val = self.peek()
        self.have_next = self.iterator.hasNext()
        self.peeked = False
        return self.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.have_next


if __name__ == "__main__":
    nums = [1, 2, 3]
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()  # Get the next element but not advance the iterator.
        iter.next()  # Should return the same value as [val].
