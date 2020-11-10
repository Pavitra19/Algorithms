from collections import deque

# Create a new empty deque object that will function as a queue 
queue = deque()

# Add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the queue contents
print(queue)

# Pop an item off the front of the queue
item_remove = queue.popleft()
print(item_remove)
print(queue)