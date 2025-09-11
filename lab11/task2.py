import timeit
from collections import deque

# 🚀 Version 1: Queue using Python List
class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # O(1)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # O(n)
        return None

    def is_empty(self):
        return len(self.queue) == 0

# ⚡ Version 2: Queue using collections.deque
class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)  # O(1)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # O(1)
        return None

    def is_empty(self):
        return len(self.queue) == 0

# 🧪 Performance Test Setup
def test_list_queue():
    q = ListQueue()
    for i in range(1000):
        q.enqueue(i)
    for _ in range(1000):
        q.dequeue()

def test_deque_queue():
    q = DequeQueue()
    for i in range(1000):
        q.enqueue(i)
    for _ in range(1000):
        q.dequeue()

# ⏱️ Time Comparison
list_time = timeit.timeit(test_list_queue, number=10)
deque_time = timeit.timeit(test_deque_queue, number=10)

# 📊 Output Results
print("ListQueue time (10 runs):", round(list_time, 4), "seconds")
print("DequeQueue time (10 runs):", round(deque_time, 4), "seconds")

# ✅ Functional Demo
print("\nFunctional Demo:")
lq = ListQueue()
dq = DequeQueue()

lq.enqueue("List Item")
dq.enqueue("Deque Item")

print("ListQueue Dequeue:", lq.dequeue())
print("DequeQueue Dequeue:", dq.dequeue())