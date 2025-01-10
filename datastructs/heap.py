import heapq

# make heap (default is min-heap)
h = [1,2,5,6,8,10]
heapq.heapify(h)

# remove root and return
heapq.heappop(h)
# add new element 
heapq.heappush(h, 7)