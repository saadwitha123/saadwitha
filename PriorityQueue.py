from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, "code"))
pq.put((1, "eat"))
pq.put((3, "sleep"))

while not pq.empty():
    print(pq.get())  # (1, 'eat'), (2, 'code'), (3, 'sleep')





from queue import PriorityQueue

pq = PriorityQueue()

pq.put((4, "sleep"))
pq.put((2, "eat"))
pq.put((1, "wake up"))
pq.put((3, "use mobile"))
while not pq.empty():
    print(pq.get())