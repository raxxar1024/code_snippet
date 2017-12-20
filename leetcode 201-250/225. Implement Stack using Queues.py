"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
You must use only standard operations of a queue
-- which means only push to back, peek/pop from front, size, and is empty operations are valid.

Depending on your language, queue may not be supported natively.

You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.

You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and all test cases.

"""


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.array.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return 0
        else:
            return self.array.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return 0
        else:
            return self.array[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.array) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    assert obj.top() == 1
    assert obj.empty() is False
