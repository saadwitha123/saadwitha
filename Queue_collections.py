from queue import Queue
q2 = Queue()
q = Queue()

# Add elements
q.put(10)
q.put(20)

# Remove elements
print(q.get())  # 10
print(q.get())  # 20




from collections import deque
# Create an empty queue
q = deque()

# Add elements (enqueue)
q.append(10)   # add to right
q.append(20)
q.append(30)
print("Queue after adding:", q)   # deque([10, 20, 30])

# Remove elements (dequeue)
print("Removed:", q.popleft())    # 10
print("Removed:", q.popleft())    # 20

# Peek at the front element (just see, not remove)
print("Front element:", q[0])     # 30

# Check if queue is empty
if not q:
    print("Queue is empty")
else:
    print("Queue is not empty")

# Add more elements and show queue behavior
q.append(40)
q.append(50)
print("Final Queue:", q)   # deque([30, 40, 50])