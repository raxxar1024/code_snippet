"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack
-- which means only push to top, peek/pop from top, size, and is empty operations are valid.

Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.

You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.pop() == 1
    assert obj.peek() == 2
    assert obj.empty() is False
