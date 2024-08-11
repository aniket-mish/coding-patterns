# Trees


## BFS Template

```python

def bfs(root):

  # handle an empty tree as a special edge case
  if root is None:
    return default value

  # create an empty queue and push the root of the tree into it
  q = deque()
  q.push(root)

  # initialize an empty result array
  result = []

  while q is not empty:

    # pop the next node from the front of the queue
    node = q.pop()

    # Process node.value
    result.append(node.value)

    # if the node has the left child, push it to the back of the queue
    if node.left is not None:
      q.push(node.left)

    # if the node has the right child, push it to the back of the queue
    if node.right is not None:
      q.push(node.right)

  return result

```

## DFS Template

```python

def main(root):
  
  def dfs(node):
  
    # Base case: leaf node
    if node.left is None and node.right is None:
      # Process the value
      return
  
    # Recursive case: internal node
    if node.left is not None:
      dfs(node.left)
  
    if node.right is not None:
      dfs(node.right)

  # Edge case
  if root is None:
    return

  dfs(root)

```

## Tree Construction - Top Down

1. Figure out what the root is and construct it.
2. Recursively construct the left subtree.
3. Recursively construct the right subtree.
