# coding-patterns

## Cycle Sort

Strategy - _Decrease-and-conquer_

```python

def rank(x):
  numsmaller = 0
  for i in range(0, len(nums)):
    if nums[i] < numsmaller:
      numsmaller += 1
  return numsmaller + 1

nums = [9, 23, 2, 4, 15, 1]
for i in range(0, len(nums)):
  while nums[i] is not in its final spot (i.e. i != rank(nums[i]) - 1):
    let d <- destination index of nums[i] should go (i.e. d = (rank(nums[i]) - 1))
    swap nums[i], nums[d]
return sorted_nums

```

Time Complexity - O(n^2)
Space Complexity - O(1)

Next, if the numbers are distinct and consecutive, we can instantly calculate rank. So the time complexity reduces to O(n).

```python

for i from 0 to n - 1:
  if nums[i] is not the value expected at that spot (i.e. nums[i] != i):
    let d <- destination index to which nums[i] should be sent
  swap nums[i] and nums[d]

```

## Sorting

Strategy - _Decrease-and-conquer_

```
```

Strategy - _Divide-and-conquer_

```
```

Strategy - _Transform-and-conquer_

## Recursion

### Combinatorial Enumerations

```

```

## Trees

### BFS

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

### Top-Down DFS

```

```

### Bottom-Up DFS

```

```

### Tree Construction (Top-Down)

1. Figure out what the root is and construct it.
2. Recursively construct the left subtree.
3. Recursively construct the right subtree.

```

```

## Graphs

1. Build the graph

```python
n = number of vertices (generally convenient ids:  0 to n-1 as these ids can be treated as indexes in the adjacency list)
adjList = a 1D array of empty lists (of integers) of size n
visited = a 1D array of size n initialized to -1

for (src, dst) in edges:
  adjList[src].append(dst)
  adjList[dst].append(src) # only if its a undirected graph
```

2. Do either BFS/DFS

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

3. Outer loop

```python
for a vertex in 0 to n-1:
  if visited[vertex] == -1:
      bfs(vertex)
```

Time and Space Complexity:

| BFS | DFS |
| --- | --- |
| O(m + n) | O(m + n) |
| O(n) | O(n) |

