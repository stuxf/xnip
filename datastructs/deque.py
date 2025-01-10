

from collections import deque

#initialize double ended queue
l = deque(["hello", "boom", "dog", "cat", "goodbye"])
#fifo 
l.append("soggy")
l.pop()
#fifo
l.appendleft("poggy")
l.popleft()
#lifo
l.appendleft("doggy")
l.pop()
#lifo
l.append("doggy")
l.popleft()