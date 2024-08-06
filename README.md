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
8. Binary Search
9. Greedy
10. Stacks


> [!NOTE]
> 🐙 - Skipped/need to revisit


Core strategies for solving any problem:
1. Brute force
2. Decrease and conquer
3. Divide and conquer
4. Transform and conquer

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
