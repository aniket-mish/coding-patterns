# We need to use the heapq library
# O(nlogn) time
def heap_sort(arr):
  # Build a minheap on the array
  heapq.heapify(arr)

  # Keep popping the successive elements from the minheap until it is empty
  result = []
  while len(arr) > 0:
    result.append(heapq.heappop(arr))

  return result
