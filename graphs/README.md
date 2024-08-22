# graphs

1. build the graph

```python

# generally we're given convenient ids:  0 to n-1 as these ids can be treated as indexes in the adjacency list
n = no. of vertices

# a 1D array of empty lists (of integers) of size n
adjList = [[] for _ in range(n)]
visited = a 1D array of size n initialized to -1

for (src, dst) in edges:
  adjList[src].append(dst)
  adjList[dst].append(src) # only if its a undirected graph
```

2. do either bfs/dfs

```python
# bfs
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
# dfs
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

