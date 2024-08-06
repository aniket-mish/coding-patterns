# O(n) time | O(n) space

# Input [3, 9, 20, null, null, 15, 7]
def binary_tree_level_order_traversal(root):

  if root is None:
    return []

    q = deque()
    q.append(root)

    result = []

    while len(q) != 0:
      numnodes = len(q)
      temp = []
      for _ in range(numnodes):
          node = q.popleft()
          temp.append(node.val)

          if node.left is not None:
              q.append(node.left)

          if node.right is not None:
              q.append(node.right)
      result.append(temp)

  return result
# Output [[3],[9,20],[15,7]]
