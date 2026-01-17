from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()
    
    def enqueue(self, val):
        self.elements.append(val)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.elements.popleft()
    
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.elements[0]
    
    def rear(self):
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self.elements[-1]
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)
    
    def clear(self):
        self.elements.clear()

# Example usage
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print(q1.dequeue())
print(q1.dequeue())
print(q1.front())
print(q1.rear())
print(q1.size())
print(q1.is_empty())
q1.clear()
print(q1.is_empty())

# LeetCode Problem 1: Implement Stack using Queues
class MyStack:
    def __init__(self):
        # Initialize a queue to simulate stack behavior
        self.q = deque()
    
    def push(self, x):
        # Add the new element to the end of the queue
        self.q.append(x)
        # Rotate the queue so that the new element is at the front
        # This ensures that the most recently added element is always at the front,
        # simulating the "top" of a stack
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        # Remove and return the element from the front of the queue,
        # which is the "top" of the stack
        return self.q.popleft()
    
    def top(self):
        # Return the element at the front of the queue without removing it,
        # representing the "top" of the stack
        return self.q[0]
    
    def empty(self):
        # Return True if the queue is empty, meaning the stack is empty
        return not self.q

# LeetCode Problem 2: Number of Recent Calls (LeetCode 933)
class RecentCounter:
    def __init__(self):
        # Initialize a queue to store the timestamps of pings
        self.q = deque()
    
    def ping(self, t):
        # Add the new ping timestamp to the queue
        self.q.append(t)
        # Remove timestamps that are older than 3000 milliseconds from the current ping
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        # The number of elements in the queue is the number of recent calls
        return len(self.q)
