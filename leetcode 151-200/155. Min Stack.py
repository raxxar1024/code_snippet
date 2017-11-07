"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

    def pop(self):
        """
        :rtype: void
        """

    def top(self):
        """
        :rtype: int
        """

    def getMin(self):
        """
        :rtype: int
        """


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    ret = minStack.getMin()
    assert ret == -3
    minStack.pop()
    ret = minStack.top()
    assert ret == 0
    ret = minStack.getMin()
    assert ret == -2
