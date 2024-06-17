# Popular Coding Patterns

workbook - https://bit.ly/3WI9Bja

**Index**

1. Sorting
2. Recursion
3. Trees
4. Graphs
5. Dynamic Programming
6. Sliding Window
7. Matrices

# Sorting

1. pre-sorting + binary search/linear scan/two-pointer pass or hash tables (space vs time tradeoff)
2. extension of merge phase in merge sort - Union or intersection of two arrays
3. extension of quicksort - quick select and 3-way partitioning
4. extension of heapsort


> [!TIP]
> get the mid of a python list, to avoid overflow `mid = start + (end - start) / 2`


## Divide-and-conquer

_work upfront_

- quick sort

_work at the end_

- merge sort

## Transform-and-conquer

_presorting_

- searching
- closest pair
- check for duplicates
- frequency distribution
- select kth largest/kth smallest/median

_common patterns_

- presorting and binary search
- presorting and one pass
- presorting and two-pointer pass

## Two-pointer pass

- should have sorted lists
- code is similar to merge sort's merge phase
- whichever element is smaller, that pointer is incremented

*This is a coding pattern and pointer increments are tweeks*

```python
# initialization
i = 0
j = 0
res = []

# while loop
for i < len(nums1) and j < len(nums2):

  # if both are same
  if nums1[i] == nums2[j]:
    res.append(nums1[i])
    i += 1
    j += 1

  # if one of them is smaller
  elif nums1[i] < nums2[j]:
    i += 1

  else:
    j += 1

# potentially a gather phase

# return result
return res
```

## Decrease-and-conquer

1. binary search

a type of decrease-and-conquer but instead of decreasing the size of the list by 1, we're decreasing it by a factor of 2 (n --> n/2)

2. randomized quick select

we decrease the size of list by a variable number and end up with O(n) time complexity

> [!NOTE]
> quick select is best when entire data is given

[problem] kth largest element

*usign quick sort*

```python
def helper(array, start, end):

  # base case: leaf node
  # subproblem of size 0 or 1
  if start >= end: 
    return

  # recursive case: intermediate node

  # LOMUTO'S PARTITIONING
  pivot_index = a random number in range start...end
  swap array[pivot_index], array[start]

  orange_ptr = start

  for green_ptr in start + 1 to end:
    if array[green_ptr] <= array[pivot_index]:
      orange_ptr ++
      swap array[green_ptr], array[orange_ptr]

  swap array[start], array[orange_ptr]

  helper(nums, start, orange_ptr - 1)
  helper(nums, orange_ptr + 1, end)

def quick_sort(nums):
  helper(nums, 0, len(nums) - 1)
```

*using quick select*

```python
def helper(array, start, end, index):

  # base case: leaf node
  if start == end:      # runs into error on leetcode: should be start >= end
    return

  # recursive case: intermediate node

  call LOMUTO'S PARTITIONING code

  if orange_ptr == index:
    return

  elif index < orange_ptr:
    helper(array, start, orange_ptr - 1, index)

  else:
    helper(array, orange_ptr + 1, end, index)


def quick_select(nums, k):
  helper(nums, 0, len(nums) - 1, len(nums) - k)
  return nums[len(nums) - k]
```

3. extension of heap operations

[problem] kth largest element in a stream

> [!NOTE]
> in streaming, quick select is not the best solution
> if k is constant, a single heap would do
> if k is function of n like the median, we need a maxheap and minheap

space - O(k)
time - O(log k)

```python

arr = initialize an array
minheap = heapq.heapify(arr) # build a minheap on arr

for each number in the stream:
  heapq.heappush(minheap, number) # insert the number in the minheap
  heapq.heappop(minheap) # extract mininum number
  return minheap[0] # root element kth element
```

similarly, to find the kth smallest element, use maxheap

[problem] median in a stream

space - O(n)
time - O(log n)

```python
initialize minheap and maxheap to empty collections
median = 0.0

for each number in the stream:
  if number > median:
    insert the number in the minheap

    if (size of minheap - size of maxheap) == 2:
      # rebalance
      extract root of the minheap and insert it into the maxheap

  else:
    insert the number in the maxheap

    if (size of maxheap - size of minheap) == 2:
      # rebalance
      extract root of the maxheap and insert it into the minheap
  

  # median computation

  if size of minheap == size of maxheap:
    median = average of the two roots

  elif size of minheap > size of maxheap:
    median = root of the minheap

  elif size of maxheap > size of minheap:
    median = root of the maxheap
```

---

# Recursion

## Combinatorial Enumerations

---

# Trees

## BFS

```python
handle an empty tree as a special edge case
initialize an empty result array
create an empty queue and push the root of the tree into it

while the queue is not empty:
  count how many nodes there are in the queue

  repeat that many times:
    pop the next node from the front of the queue
    append it to the result
    if the node has the left child, push it to the back of the queue
    if the node has the right child, push it to the back of the queue
```

## Top-down DFS


## Bottom-up DFS


## Tree Construction(top-down)

1. Figure out what the root is and construct it.
2. Recursively construct the left subtree.
3. Recursively construct the right subtree.

---

# Graphs

1. build the graph

```python
n = number of vertices (generally convenient ids:  0 to n-1 as these ids can be treated as indexes in the adjacency list)
adjList = a 1D array of empty lists (of integers) of size n
visited = a 1D array of size n initialized to -1

for (src, dst) in edges:
  adjList[src].append(dst)
  adjList[dst].append(src) # only if its a undirected graph
```

2. do either bfs/dfs

```python
def bfs(source):
  q = collections.deque()
  q.append(source)
  visited[source] = 1
  while q is not empty:
    node = q.popleft()
    for neighbour in adjList[node]:
      if visited[neighbour] == -1:
        visited[neighbour] = 1
        q.append(neighbour)
```

```python
def dfs(source):
  visited[source] = 1
  for neighbour in adjList[source]:
      if visited[neighbour] == -1:
        dfs(neighbor)
```

3. outer loop

```python
for a vertex in 0 to n-1:
  if visited[vertex] == -1:
      bfs(vertex)
```

time, space complexity:

| BDS | DFS |
| --- | --- |
| O(m + n) | O(m + n) |
| O(n) | O(n) |

---

# Dynamic Programming

---

# Sliding Window

---

# Matrices
