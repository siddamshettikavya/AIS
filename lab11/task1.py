from collections import deque

class Stack:
    """A basic stack (LIFO) implementation using Python list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack.

        Args:
            item: The item to be added.
        """
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Returns:
            The top item if stack is not empty; otherwise, None.
        """
        if self.is_empty():
            return None  # Avoid popping from empty list
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it.

        Returns:
            The top item if stack is not empty; otherwise, None.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            True if stack is empty; False otherwise.
        """
        return len(self.items) == 0


# Sample test
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top item:", stack.peek())  # 30
print("Pop item:", stack.pop())   # 30
print("Top after pop:", stack.peek())  # 20
print("Is empty?", stack.is_empty())   # False


# Optional: Optimized version using deque
class StackDeque:
    """Stack using collections.deque for efficient pop operations."""

    def __init__(self):
        """Initialize an empty deque-based stack."""
        self.items = deque()

    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return top item."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return top item without removing."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty."""
        return not self.items


# Sample test
stack = StackDeque()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top item:", stack.peek())  # 30
print("Pop item:", stack.pop())   # 30
print("Top after pop:", stack.peek())  # 20
print("Is empty?", stack.is_empty())   # False