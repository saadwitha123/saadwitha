from collections import deque

dq = deque()

# Add elements
dq.append(1)         # Right side
dq.appendleft(2)     # Left side
print(dq)            # deque([2, 1])

# Remove elements
dq.pop()             # Removes from right (1)
dq.popleft()         # Removes from left (2)




from collections import deque

# Create an empty deque
dq = deque()

# Add elements
dq.append(10)        # Add to right
dq.append(20)
dq.appendleft(5)     # Add to left
print("After adding:", dq)   # deque([5, 10, 20])

# Remove elements
dq.pop()             # Removes from right (20)
dq.popleft()         # Removes from left (5)
print("After removing:", dq)  # deque([10])

# Extend with multiple values
dq.extend([30, 40, 50])         # Add list to right
dq.extendleft([0, -1])          # Add list to left (reversed order)
print("After extend:", dq)      # deque([-1, 0, 10, 30, 40, 50])

# Rotate elements
dq.rotate(2)   # Shift right by 2
print("After rotate right:", dq)   # deque([40, 50, -1, 0, 10, 30])

dq.rotate(-3)  # Shift left by 3
print("After rotate left:", dq)    # deque([0, 10, 30, 40, 50, -1])

# Clear all elements
dq.clear()
print("After clear:", dq)   # deque([])